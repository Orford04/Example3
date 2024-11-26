from enum import Enum


class GuessResult(Enum):
    """GuessResult Class.

    This class represents a group of constants, which
    are the possible outcomes of a guess.
    """
    CORRECT = 1
    INCORRECT = 2
    MULTIPLE = 3
    NOTLEGAL = 4