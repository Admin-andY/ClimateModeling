import os
import requests
import geopandas as gpd
from fastapi import FastAPI, HTTPException
from shapely.geometry import Point
from dotenv import load_dotenv

load_dotenv()
GEOAPIFY_KEY = os.getenv("GEOAPIFY_API_KEY")

app = FastAPI(title="Climate Risk API - Geoapify Edition")

# Load climate risk data
DATA_PATH = "data/risk_zones.geojson"
try:
    risk_map = gpd.read_file(DATA_PATH)
    risk_map = risk_map.to_crs(epsg=4326) # Ensure CRS matches GPS
    print("✅ Climate risk data loaded.")
except Exception as e:
    print(f"⚠️ Data file error: {e}")
    risk_map = None

@app.post("/analyze")
async def analyze_address(address: str):
    if not risk_map:
        raise HTTPException(status_code=500, detail="Risk map not initialized.")

    # 1. GEOAPIFY GEOCODING
    # We use the 'search' endpoint for free-form addresses
    url = f"https://api.geoapify.com/v1/geocode/search?text={address}&apiKey={GEOAPIFY_KEY}"
    
    try:
        response = requests.get(url)
        data = response.json()
        
        if not data.get('features'):
            raise HTTPException(status_code=404, detail="Address not found.")
        
        # Geoapify results are in features[0]['geometry']['coordinates'] -> [lon, lat]
        lon, lat = data['features'][0]['geometry']['coordinates']
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Geoapify API error: {e}")

    # 2. SPATIAL CHECK (Point-in-Polygon)
    user_point = Point(lon, lat)
    is_at_risk = risk_map.contains(user_point).any()

    return {
        "address": address,
        "coordinates": {"lat": lat, "lon": lon},
        "risk_detected": bool(is_at_risk),
        "message": "Asset located in high-risk zone" if is_at_risk else "Asset is in a low-risk zone",
        "data_provider": "Geoapify"
    }