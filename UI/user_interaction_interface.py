from abc import ABC, abstractmethod
from classes import AddressBook


class UserOutputInteface(ABC):
    
    @abstractmethod
    def show_message(self, message: str):
        """
        Show the whatever output you get from a function
        message: the message to show
        """
        pass
    
    @abstractmethod
    def show_help(self, commands: dict):
        """
        Display a dict of commands in a human readable way
        commands: to commands to print
        """
        pass
    
    @abstractmethod
    def show_contacts(self, book: AddressBook):
        """
        Display the whole list of contacts from an AddressBook
        contacts: the book of contacts to output
        """
        pass
    
    @abstractmethod
    def show_birthdays(self, book: AddressBook):
        """
        Print the people to give the congratulations to in upcoming 7 days

        Args:
            book (AddressBook): the contacts book
        """


class UserInputInterface(ABC):
    @abstractmethod
    def user_input(self, message: str| None = None) -> str:
        """
        Get the command and it's args from a user
        message: the message to show to a user (optional)
        """
        pass
    

class UserInputOutputInterface(UserInputInterface, UserOutputInteface):
    pass