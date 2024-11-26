from typing import List
from src.guess.GuessResult import GuessResult


class Renderer:
    """Renderer Class.

    This class makes the lobster show up on the user's screen
    and communicates with the user. It prints out various messages
    to the screen in order to guide the user through the game.
    """

    @staticmethod
    def print_hello() -> None:
        """Prints hello.

        This method welcomes the user to the guessing game in the terminal.

        Args:
            args: The command-line arguments provided to the program.
        """
        print("Welcome to Lobster!")

    @staticmethod
    def print_lobster(guesses: int) -> None:
        """Prints the lobster.

        This method prints parts of the lobster to the terminal based 
        on the number of wrong guesses.

        Args:
            args: The command-line arguments provided to the program.
        """
        lobster: List[str] = ["|~~~~~~~~|",
                              "| (]  [) |",
                              "|  \\oo/  |",
                              "| >{^^}< |",
                              "| >{^^}< |",
                              "|  {^^}  |",
                              "|  {^^}  |",
                              "|  /MM\\  |",
                              "|________|"]
        empty: List[str] = ["|~~~~~~~~|",
                            "|        |",
                            "|        |",
                            "|        |",
                            "|        |",
                            "|        |",
                            "|        |",
                            "|        |",
                            "|________|"]
        for i in range(0, guesses + 1):
            print(lobster[i])
        for i in range(guesses + 1, len(empty)):
            print(empty[i])

    @staticmethod
    def print_message(result: GuessResult) -> None:
        """Prints a message.

        This method prints a message to the terminal based on whether 
        the user's guess was correct, incorrect, a multiple, or not legal.

        Args:
            args: The command-line arguments provided to the program.
        """
        if result == GuessResult.CORRECT:
            print("Great Guess!")
        elif result == GuessResult.INCORRECT:
            print("Oh no! Things are heating up!")
        elif result == GuessResult.MULTIPLE:
            print("You've already guessed that letter!")
        elif result == GuessResult.NOTLEGAL:
            print("That's not a letter")

    @staticmethod
    def print_phrase(phrase: str) -> None:
        """Prints phrase to guess.

        This method prints the secret phrase to the terminal as underscores
        to show the user how many words and letters it has.

        Args:
            args: The command-line arguments provided to the program.
        """
        print("Your phrase to guess:")
        print(phrase)

    @staticmethod
    def print_guesses(guesses: List[str]) -> None:
        """Prints previous guesses.

        This method prints out the previous guesses made my the user.

        Args:
            args: The command-line arguments provided to the program.
        """
        print("Your previous guesses are:")
        print(guesses)

    @staticmethod
    def get_guess() -> str:
        """Gets the user's guess.

        This method prompts the user to enter a guess. Then, it returns
        that guess as c.

        Args:
            args: The command-line arguments provided to the program.
        """
        c: str = input("Enter a letter to guess: ")
        return c

    @staticmethod
    def clear_screen() -> None:
        """Clears the screen.

        This method clears the screen shown in the terminal, making 
        it easier for the user to see where they are at in the game.

        Args:
            args: The command-line arguments provided to the program.
        """
        print("\033\143")

    @staticmethod
    def print_win() -> None:
        """Prints win.

        This method prints You Won! to the terminal.

        Args:
            args: The command-line arguments provided to the program.
        """
        print("You Won!")

    @staticmethod
    def print_loss() -> None:
        """Prints loss.

        This method prints You Lost! to the terminal.

        Args:
            args: The command-line arguments provided to the program.
        """
        print("You Lost!")
