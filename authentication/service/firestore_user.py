from typing import Union, Dict
from authentication.error.firestore_user_error import UserNotFoundError, FirestoreError, UserAlreadyExistsError, \
    InvalidUserInputError, UserIdModificationError
from authentication.model.user import User
from authentication.api.i_firestore_user import IFirestoreUser
import config.firebase_init as firebase_init


class FirestoreUser(IFirestoreUser):

    def __init__(self):
        """
        Initializes the FirestoreUser class and sets up a connection to the Firestore database.
        """
        self.db = firebase_init.firestore

    def create_user(self, user: User) -> None:
        """
        Creates a document for the user in Firestore.

        Args:
            user (User): The user object.

        Returns:
            None

        Raises:
            UserAlreadyExistsError: If a user with the same ID already exists.
            FirestoreError: If an error occurs while interacting with Firestore.
        """
        try:

            get_user = self.db.collection('users').document(user.user_id).get()

            if get_user.exists:
                raise UserAlreadyExistsError(user.user_id)
            user_doc = self.db.collection('users').document(user.user_id)
            user_doc.set(user.__dict__)

        except UserAlreadyExistsError as e:
            raise UserAlreadyExistsError(user.user_id) from e
        except Exception as e:
            raise FirestoreError("Error creating user.") from e

    def remove_user(self, user_id: str) -> None:
        """
        Removes the document of the user from Firestore.

        Args:
            user_id (str): The ID of the user.

        Returns:
            None

        Raises:
            UserNotFoundError: If the user with the specified ID is not found.
            FirestoreError: If an error occurs while interacting with Firestore.
        """
        try:
            user_ref = self.db.collection('users').document(user_id)
            if not user_ref.get().exists:
                raise UserNotFoundError(user_id)
            user_ref.delete()
        except UserNotFoundError as e:
            raise UserNotFoundError(user_id) from e
        except Exception as e:
            raise FirestoreError("Error removing user.") from e

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
            UserNotFoundError: If the user with the specified ID is not found.
            InvalidUserInputError: If the attribute to be edited does not exist.
            UserIdModificationError: If the user ID is attempted to be modified.
            FirestoreError: If an error occurs while interacting with Firestore.
        """
        try:
            user_ref = self.db.collection('users').document(user_id)

            if not user_ref.get().exists:
                raise UserNotFoundError(user_id)
            if attribute_name not in user_ref.get().to_dict():
                raise InvalidUserInputError(attribute_name)
            if attribute_name == 'user_id':
                raise UserIdModificationError()

            user_ref.update({attribute_name: value})

        except UserIdModificationError as e:
            raise UserIdModificationError() from e
        except UserNotFoundError as e:
            raise UserNotFoundError(user_id) from e
        except InvalidUserInputError as e:
            raise InvalidUserInputError(attribute_name) from e
        except Exception as e:
            raise FirestoreError("Error editing user field.") from e

    def get_user(self, user_id: str) -> User:
        """
        Retrieves the user document from Firestore and returns it as a User object.

        Args:
            user_id (str): The ID of the user.

        Returns:
            User: The user object.

        Raises:
            UserNotFoundError: If the user with the specified ID is not found.
            FirestoreError: If an error occurs while interacting with Firestore.
        """
        try:
            user_ref = self.db.collection('users').document(user_id)
            user_doc = user_ref.get()
            if user_doc.exists:
                return User.from_dict(user_doc.to_dict())
            else:
                raise UserNotFoundError(user_id)

        except UserNotFoundError as e:
            raise UserNotFoundError(user_id) from e
        except Exception as e:
            raise FirestoreError("Error getting user.") from e

    def get_user_field(self, user_id: str, field_name: str) -> Union[int, float, str, Dict]:
        """
        Retrieves a specific field from the user document in Firestore.

        Args:
            user_id (str): The ID of the user.
            field_name (str): The name of the field to be retrieved.

        Returns:
            Union[int, float, str, Dict]: The value of the field.

        Raises:
            UserNotFoundError: If the user with the specified ID is not found.
            FirestoreError: If an error occurs while interacting with Firestore.
            InvalidUserInputError: If the field does not exist.
        """
        try:
            user_ref = self.db.collection('users').document(user_id)
            user_doc = user_ref.get()

            if user_doc.exists and field_name in user_doc.to_dict():
                return user_doc.to_dict()[field_name]

            elif user_doc.exists and field_name not in user_doc.to_dict():
                raise InvalidUserInputError(field_name)
            elif not user_doc.exists:
                raise UserNotFoundError(user_id)

            return user_doc.get(field_name)

        except UserNotFoundError as e:
            raise UserNotFoundError(user_id) from e
        except InvalidUserInputError as e:
            raise InvalidUserInputError(field_name) from e
        except Exception as e:
            raise FirestoreError("Error getting user field.") from e
