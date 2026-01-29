try:
    from pyrfc import Connection
except ImportError:
    Connection = None

from sap.base import SAPClientBase

class RFCSAPClient(SAPClientBase):

    def __init__(self, config: dict):
        if Connection is None:
            raise RuntimeError("pyrfc not installed")
        self.conn = Connection(**config)

    def get_user_roles(self, user_id: str):
        result = self.conn.call(
            "BAPI_USER_GET_DETAIL",
            USERNAME=user_id
        )
        return [r["AGR_NAME"] for r in result.get("ACTIVITYGROUPS", [])]

    def check_sod_conflict(self, roles: list):
        # Typically via SAP GRC tables
        return []

    def create_access_request(self, user_id: str, role: str):
        return {
            "request_id": "REQ_PROD_001",
            "status": "SUBMITTED"
        }

    def get_request_status(self, request_id: str):
        return "APPROVED"
