import json
import pandas as pd

def load_users_roles():
    with open("data/sap_users_roles.json") as f:
        return json.load(f)

def load_roles_tcodes():
    return pd.read_csv("data/sap_roles_tcodes.csv")

def load_sod_rules():
    with open("data/sod_rules.json") as f:
        return json.load(f)

def load_access_requests():
    with open("data/access_requests.json") as f:
        return json.load(f)

users = load_users_roles()
print(users["ANURAG_K"])

roles_df = load_roles_tcodes()
print(roles_df[roles_df["role"] == "Z_MM_USER"])

sod_rules = load_sod_rules()
print(sod_rules)
