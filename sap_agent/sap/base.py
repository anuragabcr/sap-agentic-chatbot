from abc import ABC, abstractmethod

class SAPClientBase(ABC):

    @abstractmethod
    def get_user_roles(self, user_id: str):
        pass

    @abstractmethod
    def check_sod_conflict(self, roles: list):
        pass

    @abstractmethod
    def create_access_request(self, user_id: str, role: str):
        pass

    @abstractmethod
    def get_request_status(self, request_id: str):
        pass
