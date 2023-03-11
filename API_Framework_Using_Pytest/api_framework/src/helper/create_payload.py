import random


class CreatePayload(object):

    def create_email(self):
        text = ""
        possible = "abcdefghijklmnopqrstuvwxyz0123456789"

        for i in range(5):
            text += text.join(random.choices(possible))

        mail = text + "@harakirimail.com"
        return mail


