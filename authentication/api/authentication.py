from abc import ABC, abstractmethod

class IAuthentication(ABC):
    """
     Interface for Firebase authentication.
    """

    @abstractmethod
    def sign_in(self, email, password):
        """
        Signs in a user using email and password.

        Args:
            email (str): The user's email.
            password (str): The user's password.

        Returns:
            str: The user ID or a token representing the signed-in user.
        """
        raise NotImplementedError("Subclasses must implement the sign_in method.")

    @abstractmethod
    def sign_up(self, email, password):
        """
        Signs up a new user using email and password.

        Args:
            email (str): The user's email.
            password (str): The user's password.

        Returns:
            str: The user ID or a token representing the newly signed-up user.
        """
        raise NotImplementedError("Subclasses must implement the sign_up method.")

    @abstractmethod
    def sign_out(self):
        """
        Signs out the current user.
        """
        raise NotImplementedError("Subclasses must implement the sign_out method.")

    @abstractmethod
    def reset_password(self, email):
        """
        Sends a password reset email to the specified email address.

        Args:
            email (str): The email address to send the password reset email to.
        """
        raise NotImplementedError("Subclasses must implement the reset_password method.")
