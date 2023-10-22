from abc import ABC, abstractmethod


class IBattery(ABC):
    """The battery interface"""

    @abstractmethod
    def needs_service(self):
        """returns true if battery needs servicing"""
        pass

