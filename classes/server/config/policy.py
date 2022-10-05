import enum


class Policy(enum.Enum):
    ACCEPT="ACCEPT",
    DENIED="DENIED",
    LOG="LOG",
    DROP="DROP",
    ALLOWED="ALLOWED"
