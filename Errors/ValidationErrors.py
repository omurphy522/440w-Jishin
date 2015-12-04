# Filename: ValidationErrors.py
# Author: Osei Seraphin
# Course: IST 440w
# Instructor: Professor Oakes


class InputError(Exception):

    def __init__(self, expr, msg):
        self.expr = expr
        self.msg = msg


class noTagError(Exception):

    def __init__(self, expr, msg):
        self.expr = expr
        self.msg = msg
