import random

from data import TestData


class DataHelper:
    @staticmethod
    def get_name():
        return TestData.NAME

    @staticmethod
    def get_email():
        number = random.randint(100, 999)
        return f'alexander_samoilov_15_{number}@yandex.ru'

    @staticmethod
    def get_password():
        return random.randint(100000, 9999999999)

    @staticmethod
    def get_uncorrect_password():
        return random.randint(1, 99999)