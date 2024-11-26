import random
from src.guess.GuessingGame import GuessingGame
from src.guess.Renderer import Renderer
from typing import List


class Main:
    """Main Class.

    This class runs the guessing game.
    """

    @staticmethod
    def main(args: List[str]) -> None:
        """Runs the guessing game.

        This method welcomes the user, and then loops through the steps
        while the game is in progress. It prints out the lobster, the phrase 
        to guess, their previous guesses, it prompts them to enter a guess,
        and then prints a message based on guess.

        Args:
            args: The command-line arguments provided to the program.
        """
        with open("phrases.txt") as file:
            phrases: List[str] = [line.strip() for line in file]
        index: int = random.randrange(len(phrases))
        game: GuessingGame = GuessingGame(phrases[index])
        Renderer.clear_screen()
        Renderer.print_hello()

        while game.in_progress:
            Renderer.print_lobster(game.wrong_guesses)
            Renderer.print_phrase(game.revealed_phrase)
            Renderer.print_guesses(game.guesses)
            c: str = Renderer.get_guess()
            Renderer.clear_screen()
            Renderer.print_message(game.guess(c))

        if game.won:
            Renderer.print_win()
        if game.lost:
            Renderer.print_loss()
