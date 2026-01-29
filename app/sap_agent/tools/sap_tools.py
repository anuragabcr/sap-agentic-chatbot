from app.sap_agent.sap.mock_client import MockSAPClient

sap_client = MockSAPClient()

def get_user_roles_tool(user_id: str):
    """Get SAP roles assigned to a user"""
    return sap_client.get_user_roles(user_id)

def check_sod_conflict_tool(roles: list):
    """Check SoD conflicts for given roles"""
    return sap_client.check_sod_conflict(roles)

def create_access_request_tool(user_id: str, role: str):
    """Create SAP access request"""
    return sap_client.create_access_request(user_id, role)

def get_request_status_tool(request_id: str):
    """Get SAP access request status"""
    return sap_client.get_request_status(request_id)
