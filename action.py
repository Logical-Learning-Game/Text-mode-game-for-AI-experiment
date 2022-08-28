
class Action:
    UP = "up"
    LEFT = "left"
    DOWN = "down"
    RIGHT = "right"

    @classmethod
    def from_string(cls, s: str):
        if s in {cls.UP, cls.LEFT, cls.DOWN, cls.RIGHT}:
            return s