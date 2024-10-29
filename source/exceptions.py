class BadRequest(BaseException):
    def __init__(self):
        super().__init__('BadRequest')

class InternalError(BaseException):
    def __init__(self):
        super().__init__('InternalError')
