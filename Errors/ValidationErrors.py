__author__ = 'Osei'


class InputError(Exception):

    def __init__(self, expr, msg):
        self.expr = expr
        self.msg = msg


class noTagError(Exception):

    def __init__(self, expr, msg):
        self.expr = expr
        self.msg = msg
