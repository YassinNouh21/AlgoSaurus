from abc import ABC, abstractmethod
from typing import Union, Dict
from authentication.model.user import User


class IFirestoreUser(ABC):
    @abstractmethod
    def create_user(self, user: User) -> None:
        """
        Creates a document for the user in Firestore.

        Args:
            user (User): The user object.

        Returns:
            None

        Raises:
            NotImplementedError: If the method is not implemented.
        """
        raise NotImplementedError(f"Subclasses must implement the create_user method.")

    @abstractmethod
    def remove_user(self, user_id: str) -> None:
        """
        Removes the document of the user from Firestore.

        Args:
            user_id (str): The ID of the user.

        Returns:
            None

        Raises:
            NotImplementedError: If the method is not implemented.
        """
        raise NotImplementedError(f"Subclasses must implement the remove_user method.")

    @abstractmethod
    def delete_user_field(self, user_id: str, attribute_name: str) -> None:
        """
        Deletes a specific attribute from the user document in Firestore.

        Args:
            user_id (str): The ID of the user.
            attribute_name (str): The name of the attribute to be deleted.

        Returns:
            None

        Raises:
            NotImplementedError: If the method is not implemented.
        """
        raise NotImplementedError(f"Subclasses must implement the delete_user_field method.")

    @abstractmethod
    def edit_user_field(self, user_id: str, attribute_name: str, value: Union[int, float, str, Dict]) -> None:
        """
        Edits a specific attribute of the user document in Firestore.

        Args:
            user_id (str): The ID of the user.
            attribute_name (str): The name of the attribute to be edited.
            value (Union[int, float, str, Dict]): The new value of the attribute.

        Returns:
            None

        Raises:
            NotImplementedError: If the method is not implemented.
        """
        raise NotImplementedError(f"Subclasses must implement the edit_user_attribute method.")

    @abstractmethod
    def get_user(self, user_id: str) -> User:
        """
        Retrieves the user document from Firestore and returns it as a User object.

        Args:
            user_id (str): The ID of the user.

        Returns:
            User: The user object.

        Raises:
            NotImplementedError: If the method is not implemented.
        """
        raise NotImplementedError(f"Subclasses must implement the get_user method.")

    @abstractmethod
    def get_user_field(self, user_id: str, field_name: str) -> Union[int, float, str, Dict]:
        """
        Retrieves a specific field from the user document in Firestore.

        Args:
            user_id (str): The ID of the user.
            field_name (str): The name of the field to be retrieved.

        Returns:
            Union[int, float, str, Dict]: The value of the field.

        Raises:
            NotImplementedError: If the method is not implemented.
        """
        raise NotImplementedError(f"Subclasses must implement the get_user_field method.")
