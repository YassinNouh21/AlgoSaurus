from abc import ABC, abstractmethod
import model.user as User
from typing import Dict


class IAuthentication(ABC):
    """
     Interface for Firebase authentication.
    """

    @abstractmethod
    def sign_in(self, email: str, password: str) -> User:
        """
        Signs in a user using email and password.

        Args:
            email (str): The user's email.
            password (str): The user's password.

        Returns:
            User: The newly signed-up user.
        """
        raise NotImplementedError("Subclasses must implement the sign_in method.")
    
    @abstractmethod
    def sign_up(self, email: str, password: str, handles: Dict[str, str]) -> User:
        """
        Signs up a new user using email and password.

        Args:
            email (str): The user's email.
            password (str): The user's password.
            handles (Dict[str, str]): A dictionary of handles for competitive programming websites.
                The keys are the names of the websites (e.g. "Codeforces", "Atcoder", "Codechef"),
                and the values are the handles for the user on those websites.

        Returns:
            User: The newly signed-up user.
        """
        raise NotImplementedError("Subclasses must implement the sign_up method.")
    
    @abstractmethod
    def sign_out(self) -> None:
        """
        Signs out the current user.
        """
        raise NotImplementedError("Subclasses must implement the sign_out method.")

    @abstractmethod
    def reset_password(self, email: str) -> None:
        """
        Sends a password reset email to the specified email address.

        Args:
            email (str): The email address to send the password reset email to.
        """
        raise NotImplementedError("Subclasses must implement the reset_password method.")
