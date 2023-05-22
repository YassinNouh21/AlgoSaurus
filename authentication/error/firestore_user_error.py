# This file contains all custom exceptions related to the FirestoreUser class.

class FirestoreUserException(Exception):
    """Base class for all custom exceptions related to the FirestoreUser class."""
    USER_NOT_FOUND_ERROR = "UserNotFoundError"
    USER_ALREADY_EXISTS_ERROR = "UserAlreadyExistsError"
    INVALID_USER_INPUT_ERROR = "InvalidUserInputError"
    FIRESTORE_ERROR = "FirestoreError"
    EXCEPTION = "Exception"
    USER_ID_MODIFICATION_ERROR = "UserIdModificationError"

    def __init__(self, message: str):
        super().__init__(message)

    @staticmethod
    def create_exception(exception_type: str, message: str) -> Exception:
        """Creates a FirestoreUser exception to the specified type."""
        if exception_type == "UserNotFoundError":
            return UserNotFoundError(message)
        elif exception_type == "UserAlreadyExistsError":
            return UserAlreadyExistsError(message)
        elif exception_type == "InvalidUserInputError":
            return InvalidUserInputError(message)
        elif exception_type == "FirestoreError":
            return FirestoreError(message)
        elif exception_type == "Exception":
            return Exception(message)
        else:
            raise ValueError(f"Invalid exception type: {exception_type}")


class UserNotFoundError(FirestoreUserException):
    """Exception raised when a user with the specified ID is not found."""

    USER_NOT_FOUND_ERROR = "UserNotFoundError"

    def __init__(self, user_id: str):
        super().__init__(f"User with ID {user_id} not found.")


class UserAlreadyExistsError(FirestoreUserException):
    """Exception raised when a user with the specified ID already exists."""

    USER_ALREADY_EXISTS_ERROR = "UserAlreadyExistsError"

    def __init__(self, user_id: str):
        super().__init__(f"User with ID {user_id} already exists.")


class InvalidUserInputError(FirestoreUserException):
    """Exception raised when the user input is invalid."""

    INVALID_USER_INPUT_ERROR = "InvalidUserInputError"

    def __init__(self, message: str):
        super().__init__(message)


class FirestoreError(FirestoreUserException):
    """Exception raised when an error occurs while interacting with Firestore."""

    FIRESTORE_ERROR = "FirestoreError"

    def __init__(self, message: str):
        super().__init__(message)


class UserIdModificationError(Exception):
    """Exception raised when an attempt is made to modify the user_id attribute."""

    def __init__(self):
        super().__init__("The user_id attribute cannot be modified.")
