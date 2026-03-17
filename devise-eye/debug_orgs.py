import firebase_admin
from firebase_admin import credentials, firestore
import json

cred_path = r'C:\ProgramData\Devise\service_account.json'
cred = credentials.Certificate(cred_path)
firebase_admin.initialize_app(cred)
db = firestore.client()

print("Listing unique Org IDs from recent events...")
docs = db.collection('detection_events').order_by('timestamp', direction=firestore.Query.DESCENDING).limit(20).get()

orgs = set()
for doc in docs:
    data = doc.to_dict()
    org_id = data.get('org_id')
    orgs.add(org_id)
    print(f"Doc: {doc.id} | Org: {org_id} | Tool: {data.get('tool_name')} | TS: {data.get('timestamp')}")

print("\nSummary of unique Org IDs found:")
for org in orgs:
    print(f"- {org}")
