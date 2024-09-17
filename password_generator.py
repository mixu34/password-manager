import random

LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
NUMBERS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
SYMBOLS = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


class PasswordGenerator:
    def __init__(self):
        self.password_list = []
        self.password = ""

    def generate_random_password(self):
        password_letters = [random.choice(LETTERS) for _ in range(random.randint(8, 10))]
        password_symbols = [random.choice(SYMBOLS) for _ in range(random.randint(2, 4))]
        password_numbers = [random.choice(NUMBERS) for _ in range(random.randint(2, 4))]
        self.password_list = password_numbers + password_symbols + password_letters
        random.shuffle(self.password_list)

        self.password = "".join(self.password_list)
        return self.password
