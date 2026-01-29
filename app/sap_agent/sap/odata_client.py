import requests
from app.sap_agent.sap.base import SAPClientBase


class ODataSAPClient(SAPClientBase):

    def __init__(self, base_url, username, password):
        self.base_url = base_url
        self.auth = (username, password)

    def get_user_roles(self, user_id: str):
        url = f"{self.base_url}/UserRoles?$filter=UserId eq '{user_id}'"
        response = requests.get(url, auth=self.auth)
        response.raise_for_status()
        data = response.json()
        return [r["Role"] for r in data["value"]]

    def check_sod_conflict(self, roles: list):
        # Usually handled via GRC → simplified here
        return []

    def create_access_request(self, user_id: str, role: str):
        url = f"{self.base_url}/AccessRequests"
        payload = {"UserId": user_id, "Role": role}
        response = requests.post(url, json=payload, auth=self.auth)
        response.raise_for_status()
        return response.json()

    def get_request_status(self, request_id: str):
        url = f"{self.base_url}/AccessRequests('{request_id}')"
        response = requests.get(url, auth=self.auth)
        response.raise_for_status()
        return response.json()["Status"]
