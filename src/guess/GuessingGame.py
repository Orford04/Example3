"""Guessing Game Program.

This is a Guessing Game program to demonstrate proper
Python coding style, testing, documentation, and more.

Author: Olivia Ford orford@mnu.edu
Version: 0.1
"""


from typing import List
from src.guess.GuessResult import GuessResult


class GuessingGame:
    """Guessing Game Class.

    This class has the necessary functions that takes the user 
    through a guessing game. It processes their input and responds 
    accordingly. It has the functions needed to keep track of the 
    phrase, both revealed and secret parts, keep track of the user's 
    guesses, tracks the number of wrong guesses, and whether the user
    has won or lost the game.
    """
    def __init__(self, secret: str) -> None:
        """Prints a secret phrase.

        This method prints the secret message to the terminal as underscores.
        Initializes a list for guesses to be displayed. Creates a counter for wrong guesses.

        Args:
            args: The command-line arguments provided to the program.
        """
        if len(secret) < 5:
            raise ValueError("Secret must be at least 5 characters")
        self.__secret_phrase: str = secret
        self.__revealed_phrase: List[str] = ["_" if x.isalpha()
                                             else x for x in
                                             self.__secret_phrase]
        self.__guesses: List[str] = []
        self.__wrong_guesses: int = 0

    @property
    def revealed_phrase(self) -> str:
        """Returns a revealed phrase.

        This method returns a revealed phrase.

        Args:
            args: The command-line arguments provided to the program.
        """
        return "".join(self.__revealed_phrase)

    @property
    def guesses(self) -> List[str]:
        """Returns the past guesses.

        This method returns the past guesses.

        Args:
            args: The command-line arguments provided to the program.
        """
        return self.__guesses.copy()

    @property
    def wrong_guesses(self) -> int:
        """Returns the number of wrong guesses.

        This method returns the number of wrong guesses that the user has made.

        Args:
            args: The command-line arguments provided to the program.
        """
        return self.__wrong_guesses

    @property
    def won(self) -> bool:
        """Returns that no more '_' are found in the revealed phrase.

        This method returns that no more '_' are found in the revealed phrase.
        This means that they have all been replaced with the correct letters.
        Thus, the user has won.
        Args:
            args: The command-line arguments provided to the program.
        """
        return '_' not in self.__revealed_phrase

    @property
    def lost(self) -> bool:
        """Returns that the number of wrong guesses is >= 7.

        This method returns that the number of wrong guesses is >= 7.
        This means that the user lost, since the game ends if they 
        make 7 wrong guesses.

        Args:
            args: The command-line arguments provided to the program.
        """
        return self.__wrong_guesses >= 7

    @property
    def in_progress(self) -> bool:
        """Returns not won or lost.

        This method returns that the user has not lost or won.
        Since they haven't won or lost, that means that the game
        is still in progress.

        Args:
            args: The command-line arguments provided to the program.
        """
        return not (self.won or self.lost)

    def guess(self, c: str) -> GuessResult:
        """Prints a secret phrase.

        This method makes all uppercase letters in a guess lowercase.
        If they haven't guessed the letter before, it adds the letter to
        the guesses list. It then goes through each letter in the phrase
        and sees if any match the user's guess. If it does match, it 
        reveals the letter and sets found to True. If their guess is not found
        in the phrase, wrong guesses gets increase by 1. It then returns whether
        the guess was incorrect, correct, multipl, or not legal.

        Args:
            args: The command-line arguments provided to the program.
        """
        if c.isalpha():
            c = c.lower()
            if c not in self.__guesses:
                self.__guesses.append(c)
                found: bool = False
                for i in range(0, len(self.__secret_phrase)):
                    if self.__secret_phrase[i].lower() == c:
                        self.__revealed_phrase[i] = self.__secret_phrase[i]
                        found = True
                if not found:
                    self.__wrong_guesses += 1
                    return GuessResult.INCORRECT
                else:
                    return GuessResult.CORRECT
            else:
                return GuessResult.MULTIPLE
        else:
            return GuessResult.NOTLEGAL
