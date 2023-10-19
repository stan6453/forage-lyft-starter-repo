from abc import ABC, abstractmethod


class IServiceable(ABC):
    """The Serviceable interface"""

    @abstractmethod
    def needs_service():
        """returns true if object needs servicing"""
        pass
