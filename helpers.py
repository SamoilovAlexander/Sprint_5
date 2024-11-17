import random

class DataHelper:
    @staticmethod
    def get_name():
        return "Alexander"

    @staticmethod
    def get_email():
        number = random.randint(100, 999)
        return f'Alexander_Samoilov_15_{number}@yandex.ru'

    @staticmethod
    def get_password():
        return random.randint(100000, 9999999999)

    @staticmethod
    def get_uncorrect_password():
        return random.randint(1, 99999)