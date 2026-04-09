from flask import Flask, render_template, request, jsonify
import random
import math

app = Flask(__name__)

# --- Mock ML Engine ---

BORDER_ZONES = [
    {"name": "Sri Lanka Maritime Border", "lat": 9.5, "lon": 80.2, "radius": 0.8},
    {"name": "Myanmar Maritime Border",   "lat": 14.0, "lon": 98.0, "radius": 0.9},
    {"name": "Indonesia Maritime Border", "lat": 5.5,  "lon": 95.5, "radius": 0.7},
]

DANGER_ZONES = [
    {"name": "High Storm Zone A", "lat": 10.2, "lon": 79.8},
    {"name": "Rough Current Zone B", "lat": 11.0, "lon": 80.5},
    {"name": "Low Visibility Zone C", "lat": 9.8,  "lon": 80.9},
]

def haversine(lat1, lon1, lat2, lon2):
    R = 6371
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = math.sin(dlat/2)**2 + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dlon/2)**2
    return R * 2 * math.asin(math.sqrt(a))

def predict_risk(lat, lon, wind_speed, wave_height, visibility, experience):
    score = 0
    factors = []
    shap_values = {}

    # Wind speed factor
    wind_contrib = min(wind_speed / 80, 1) * 30
    score += wind_contrib
    shap_values["Wind Speed"] = round(wind_contrib, 1)
    if wind_speed > 40:
        factors.append(f"High wind speed ({wind_speed} km/h) significantly increases risk")

    # Wave height factor
    wave_contrib = min(wave_height / 8, 1) * 25
    score += wave_contrib
    shap_values["Wave Height"] = round(wave_contrib, 1)
    if wave_height > 3:
        factors.append(f"Wave height of {wave_height}m poses capsizing danger")

    # Visibility factor
    vis_contrib = max(0, (5 - visibility) / 5) * 20
    score += vis_contrib
    shap_values["Visibility"] = round(vis_contrib, 1)
    if visibility < 2:
        factors.append(f"Very low visibility ({visibility} km) increases collision risk")

    # Experience factor
    exp_contrib = max(0, (10 - experience) / 10) * 10
    score += exp_contrib
    shap_values["Experience"] = round(exp_contrib, 1)
    if experience < 3:
        factors.append("Low fishing experience increases accident probability")

    # Border proximity
    border_alert = None
    border_contrib = 0
    for zone in BORDER_ZONES:
        dist = haversine(lat, lon, zone["lat"], zone["lon"])
        if dist < zone["radius"] * 111:
            border_contrib = 15
            score += border_contrib
            border_alert = zone["name"]
            factors.append(f"Location is near {zone['name']} — border crossing risk!")
            break
    shap_values["Border Proximity"] = round(border_contrib, 1)

    # Danger zone proximity
    for zone in DANGER_ZONES:
        dist = haversine(lat, lon, zone["lat"], zone["lon"])
        if dist < 80:
            score += 10
            factors.append(f"Vessel is near {zone['name']}")

    score = min(round(score, 1), 100)

    if score >= 70:
        level = "HIGH"
        color = "#e74c3c"
        recommendation = "⚠️ Do NOT venture out. Seek shelter immediately and alert coast guard."
    elif score >= 40:
        level = "MEDIUM"
        color = "#f39c12"
        recommendation = "⚡ Exercise extreme caution. Monitor conditions closely and stay near shore."
    else:
        level = "LOW"
        color = "#2ecc71"
        recommendation = "✅ Conditions are relatively safe. Follow standard safety protocols."

    if not factors:
        factors.append("No major individual risk factors detected.")

    return {
        "score": score,
        "level": level,
        "color": color,
        "recommendation": recommendation,
        "factors": factors,
        "border_alert": border_alert,
        "shap_values": shap_values
    }

# --- Routes ---

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

@app.route("/predict", methods=["GET", "POST"])
def predict():
    if request.method == "POST":
        data = request.json
        result = predict_risk(
            float(data["lat"]),
            float(data["lon"]),
            float(data["wind_speed"]),
            float(data["wave_height"]),
            float(data["visibility"]),
            float(data["experience"])
        )
        return jsonify(result)
    return render_template("predict.html")

@app.route("/map")
def map_view():
    return render_template("map.html")

@app.route("/api/zones")
def get_zones():
    return jsonify({"border_zones": BORDER_ZONES, "danger_zones": DANGER_ZONES})

@app.route("/api/live-data")
def live_data():
    # Simulated live fleet data
    vessels = []
    base_positions = [
        (10.8, 79.8), (9.9, 80.3), (11.2, 79.5),
        (10.1, 80.7), (9.5, 79.9), (10.5, 80.1)
    ]
    names = ["MV Kaveri", "MV Selvi", "MV Aruna", "MV Priya", "MV Devi", "MV Ganga"]
    for i, (base_lat, base_lon) in enumerate(base_positions):
        lat = base_lat + random.uniform(-0.05, 0.05)
        lon = base_lon + random.uniform(-0.05, 0.05)
        risk = predict_risk(lat, lon, random.uniform(10, 60), random.uniform(0.5, 5),
                            random.uniform(1, 8), random.randint(1, 15))
        vessels.append({
            "name": names[i],
            "lat": round(lat, 4),
            "lon": round(lon, 4),
            "risk_level": risk["level"],
            "risk_score": risk["score"],
            "color": risk["color"]
        })
    return jsonify(vessels)

if __name__ == "__main__":
    app.run(debug=True, port=5000)
