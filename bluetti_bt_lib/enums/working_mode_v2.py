from enum import Enum, unique


@unique
class WorkingModeV2(Enum):
    CUSTOMIZED = 1
    SELF_USE = 2
    BACKUP = 4
    SCHEDULED = 5
