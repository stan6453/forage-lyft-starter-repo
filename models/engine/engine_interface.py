from abc import ABC, abstractmethod


class IEngine(ABC):
    """The engine interface"""

    @abstractmethod
    def needs_service(self):
        """returns true if engine needs servicing"""
        pass
