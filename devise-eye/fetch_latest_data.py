import firebase_admin
from firebase_admin import credentials, firestore

cred_path = r'C:\ProgramData\Devise\service_account.json'
cred = credentials.Certificate(cred_path)
firebase_admin.initialize_app(cred)
db = firestore.client()

print("Fetching latest 5 detection events...")
docs = db.collection('detection_events').order_by('timestamp', direction=firestore.Query.DESCENDING).limit(5).get()

if not docs:
    print("No events found at all.")
else:
    for doc in docs:
        data = doc.to_dict()
        print(f"ID: {doc.id}")
        print(f"  Org ID: {data.get('org_id')}")
        print(f"  Timestamp: {data.get('timestamp')}")
        print(f"  Tool: {data.get('tool_name')}")
        print(f"  Category: {data.get('category')}")
        print(f"  Risk: {data.get('risk_level')}")
        print("-" * 20)
