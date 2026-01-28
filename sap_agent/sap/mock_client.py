from sap.base import SAPClientBase

MOCK_USERS = {
    "anurag": ["Z_MM_DISPLAY", "Z_FI_AP_CLERK"],
    "john": ["Z_SD_USER"]
}

MOCK_SOD_CONFLICTS = [
    ("Z_FI_AP_CLERK", "Z_FI_AP_APPROVER")
]

MOCK_REQUESTS = {}

class MockSAPClient(SAPClientBase):

    def get_user_roles(self, user_id: str):
        return MOCK_USERS.get(user_id.lower(), [])

    def check_sod_conflict(self, roles: list):
        conflicts = []
        for r1, r2 in MOCK_SOD_CONFLICTS:
            if r1 in roles and r2 in roles:
                conflicts.append((r1, r2))
        return conflicts

    def create_access_request(self, user_id: str, role: str):
        request_id = f"REQ-{len(MOCK_REQUESTS)+1}"
        MOCK_REQUESTS[request_id] = {
            "user": user_id,
            "role": role,
            "status": "SUBMITTED"
        }
        return {"request_id": request_id, "status": "SUBMITTED"}

    def get_request_status(self, request_id: str):
        return MOCK_REQUESTS.get(request_id, {}).get("status", "UNKNOWN")
