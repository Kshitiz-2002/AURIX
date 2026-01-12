from enum import Enum, auto

class CognitiveState(Enum):
    INIT = auto()
    INTERPRET = auto()
    PLAN = auto()
    ACT = auto()
    OBSERVE = auto()
    DECIDE = auto()
    DONE = auto()
    ERROR = auto()