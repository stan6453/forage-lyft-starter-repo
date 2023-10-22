from abc import ABC, abstractmethod


class ITire(ABC):
    """The tire interface"""

    @abstractmethod
    def needs_service(self):
        """returns true if tire needs servicing"""
        pass