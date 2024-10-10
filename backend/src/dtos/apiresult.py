class ApiResult:
    def __init__(self, code: str = "200", data: object = None, msg: str = "success") -> None:
        self.code = code
        self.data = data
        self.msg = msg