from pymongo import MongoClient

MONGO_URI = "mongodb+srv://cyberadmin:cyberadmin12345@cyberthreatcluster.rakfyvd.mongodb.net/?appName=CyberThreatCluster"

client = MongoClient(MONGO_URI)

db = client["cyber_threat_db"]

users_collection = db["users"]
reports_collection = db["reports"]
uploads_collection = db["uploads"]