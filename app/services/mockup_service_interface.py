from abc import ABC, abstractmethod

class MockupServiceInterface(ABC):
    @abstractmethod
    def process_mockup(self, payload: dict) -> dict:
        """
        Process the mockup image based on input payload.
        Returns a dictionary with at least:
            - preview_url: URL or base64 string
            - message: status message
        """
        pass
