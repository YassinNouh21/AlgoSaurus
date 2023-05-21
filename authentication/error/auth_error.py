class AuthenticationError(Exception):
    """
    Base class for all authentication errors.
    """

    def __init__(self, message: str):
        super().__init__(message)


class InvalidCredentialsError(AuthenticationError):
    """
    Error raised when the provided credentials are invalid.
    """

    def __init__(self):
        super().__init__("Invalid credentials")


class UserNotFoundError(AuthenticationError):
    """
    Error raised when the user does not exist.
    """

    def __init__(self, email: str):
        super().__init__(f"User with email {email} not found")


class UserNotActiveError(AuthenticationError):
    """
    Error raised when the user is not active.
    """

    def __init__(self, email: str):
        super().__init__(f"User with email {email} is not active")


class UserNotVerifiedError(AuthenticationError):
    """
    Error raised when the user is not verified.
    """

    def __init__(self, email: str):
        super().__init__(f"User with email {email} is not verified")


class UserNotSignedInError(AuthenticationError):
    """
    Error raised when the user is not signed in.
    """

    def __init__(self):
        super().__init__("User is not signed in")


class PasswordResetLinkExpiredError(AuthenticationError):
    """
    Error raised when the password reset link has expired.
    """

    def __init__(self):
        super().__init__("Password reset link has expired")


class PasswordResetLinkInvalidError(AuthenticationError):
    """
    Error raised when the password reset link is invalid.
    """

    def __init__(self):
        super().__init__("Password reset link is invalid")


class UserAlreadyHasAccount(AuthenticationError):
    """
    Error raised when the user already has an account.
    """

    def __init__(self, email: str):
        super().__init__(f"User with email {email} already has an account")
