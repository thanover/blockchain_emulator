import hashlib
import time


class User:
    def __init__(self, first_name, last_name, users):
        self.first_name = first_name
        self.last_name = last_name
        unvalidated = True
        while unvalidated:
            self.generate_id()
            unvalidated = self.validate_id(users)

    def generate_id(self):
        concat_name = self.first_name + self.last_name + str(time.time())
        m = hashlib.sha256()
        m.update(concat_name.encode('utf-8'))
        self.id = 'u_' + m.hexdigest()[0:10]

    def print_user_info_short(self):
        output = str(self.first_name + ' ' + self.last_name)
        return output

    def get_id(self):
        return self.id

    def get_name(self):
        return str(self.first_name + ' ' + self.last_name)

    def validate_id(self, users):
        for user in users:
            if user.get_id == self.id:
                self.generate_id
                return True

        return False

