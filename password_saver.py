import json


class PasswordSaver:
    def __init__(self, website="", email="", password=""):
        self.website = website
        self.email = email
        self.password = password
        self.data = ""

    def read_file(self):
        with (open("passwords.json", "r")) as file:
            self.data = json.load(file)

    def write_file(self, data):
        with (open("passwords.json", "w")) as file:
            json.dump(data, file, indent=4)

    def check_if_website_not_in_file(self):
        try:
            self.read_file()
            for key in self.data.keys():
                if key == self.website:
                    return False
        except FileNotFoundError:
            return True
        else:
            return True

    def save_password(self):
        new_data = {
            self.website: {
                "email": self.email,
                "password": self.password,
            }
        }
        try:
            self.read_file()
        except FileNotFoundError:
            self.write_file(new_data)
        else:
            self.data.update(new_data)
            self.write_file(self.data)

    def get_password(self, website):
        try:
            self.read_file()
            for key in self.data.keys():
                if key == website:
                    return self.data[key]
        except FileNotFoundError:
            return "File not found."
        else:
            return "Website not found."
