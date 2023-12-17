class IdObject:
    def __init__(self, _id: int):
        if not isinstance(_id, int):
            raise TypeError("Id must be an integer")
        self._id = _id
    
    @property
    def id(self) -> int:
        return self._id