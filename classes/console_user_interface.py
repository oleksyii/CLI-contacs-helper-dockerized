from classes.classes import AddressBook
from .user_interaction_interface import UserInteractionInterface
from colorama import Fore
from .inputs_parsing import parse_input
from typing import Tuple

class ConsoleUserInterface(UserInteractionInterface):
    
    def show_message(self, message: str):
        print(message)
        
    def show_help(self, commands: dict):
        print("List of all the available commands:")
        # Find the longest key to set the spacing
        longest_key = max(len(key) for key in commands.keys())
        for key, value in commands.items():
            print(f"{Fore.YELLOW}{key:<{longest_key}}{Fore.RESET} : {value}")
            
    def show_contacts(self, book: AddressBook):
        print("Your contacts are:")
        for person in book.values():
            print(" * " + str(person))
            
    def user_input(self, message: str|None = None) -> Tuple[str, list]:
        user_input = input(message if message else "\nEnter a command: ")
        command, *args = parse_input(user_input)
        return command, *args
    
    def show_birthdays(self, book: AddressBook):
        people_to_congrat = book.get_upcoming_birthdays()
        if people_to_congrat:
            for person in people_to_congrat:
                print(" * " + str(person))
        else:
            print("There are no people celebrating :'(")