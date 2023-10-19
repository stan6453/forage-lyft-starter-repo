from abc import ABC, abstractmethod


class IBattery(ABC):
    """The battery interface"""

    @abstractmethod
    def needs_service():
        """returns true if battery needs servicing"""
        pass


if True:
    from .nubbin_battery import NubbinBattery
    from .spindler_battery import SpindlerBattery
