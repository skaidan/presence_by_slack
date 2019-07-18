from properties import USER, TOKEN


class KeysHandler(object):
    user = ""
    token = ""
    def __init__(self):
        self.user = USER
        self.token = TOKEN
