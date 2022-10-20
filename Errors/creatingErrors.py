
class MyCustomError(TypeError):
    """Exception raised when a specific code is needed
    
    Keyword arguments:
    message -- description
    code - error code
    Return: raises exception
    """
    def __init__(self, message, code) -> None:
        new_message = f"{message} : Error Code {code}"
        super().__init__(new_message)
        self.code = code


raiseException = MyCustomError('something went wrong !!',200)

print(raiseException.__doc__)