class SAPRFCClient:
    def get_user_roles(self, user_id):
        return ["Z_MM_DISPLAY", "Z_FI_AP_CLERK"]

    def check_sod_conflict(self, roles):
        return False

    def create_access_request(self, user, role):
        return {"request_id": "REQ12345", "status": "SUBMITTED"}

    def get_request_status(self, request_id):
        return "APPROVED"
