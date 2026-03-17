import firebase_admin
from firebase_admin import credentials, firestore
import json
import datetime

cred_path = r'C:\ProgramData\Devise\service_account.json'
config_path = r'C:\ProgramData\Devise\config.json'

cred = credentials.Certificate(cred_path)
firebase_admin.initialize_app(cred)
db = firestore.client()

with open(config_path, 'r') as f:
    config = json.load(f)
org_id = config.get('org_id')

print(f"DEBUG: Org ID from config is '{org_id}'")

# Query without order_by first to see what we have
docs = db.collection('detection_events').where('org_id', '==', org_id).limit(1).get()

if not docs:
    print("No documents found for this org_id.")
else:
    for doc in docs:
        print("DOCUMENT DATA:")
        data = doc.to_dict()
        # Convert datetime to string for printing
        for k, v in data.items():
            if isinstance(v, datetime.datetime):
                data[k] = v.isoformat()
        print(json.dumps(data, indent=2))
