import pickle
from classes import AddressBook, Record, Birthday, Phone, Name, Field

# from classes import *


def save_data(book, filename="./storage/addressbook.pkl"):
    with open(filename, "wb") as f:
        pickle.dump(book, f)


def load_data(filename="./storage/addressbook.pkl"):
    try:
        with open(filename, "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return AddressBook()  # Повернення нової адресної книги, якщо файл не знайдено
