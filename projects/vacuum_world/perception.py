

class Perception:

    def __init__(self, location: bool, is_dirty: bool) -> None:
        self._location = location
        self._is_dirty = is_dirty

    @property
    def location(self) -> bool:
        return self._location

    @property
    def is_dirty(self) -> bool:
        return self._is_dirty

    