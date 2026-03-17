import firebase_admin
from firebase_admin import credentials, firestore

cred_path = r'C:\ProgramData\Devise\service_account.json'
cred = credentials.Certificate(cred_path)
firebase_admin.initialize_app(cred)
db = firestore.client()

print("Listing all Profiles in Firestore...")
profiles = db.collection('profiles').get()

if not profiles:
    print("No profiles found.")
else:
    for p in profiles:
        data = p.to_dict()
        print(f"UID: {p.id}")
        print(f"  Email: {data.get('email')}")
        print(f"  Org ID: {data.get('org_id')}")
        print("-" * 20)
