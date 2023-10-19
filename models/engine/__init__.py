from abc import ABC, abstractmethod


class IEngine(ABC):
    """The engine interface"""

    @abstractmethod
    def needs_service():
        """returns true if engine needs servicing"""
        pass


if True:
    from .capulet_engine import CapuletEngine
    from .sternman_engine import SternmanEngine
    from .willoughby_engine import WilloughbyEngine
