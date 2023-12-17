class ValidationException(Exception):
    def __init__(self, error_msg):
        self._error_messages = error_msg

    @property
    def error_messages(self):
        return self._error_messages

    def __str__(self):
        return "Validation error:" + f"\n {self._error_messages}"


class NoBookExist(ValidationException):
    def __init__(self, error_msgs):
        ValidationException.__init__(self, error_msgs)

class OptionError(ValidationException):
    def __init__(self, error_msgs):
        ValidationException.__init__(self, error_msgs)

class ClientError(ValidationException):
    def __init__(self, error_msgs):
        ValidationException.__init__(self, error_msgs)
        
class RentalError(ValidationException):
    def __init__(self, error_msgs):
        ValidationException.__init__(self, error_msgs)
        
class TypeError(ValidationException):
  def __init__(self, error_msgs):
        ValidationException.__init__(self, error_msgs)