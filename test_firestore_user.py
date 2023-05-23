from authentication.error.firestore_user_error import UserNotFoundError, FirestoreError, UserAlreadyExistsError, InvalidUserInputError
from authentication.model.user import User
from authentication.service.firestore_user import FirestoreUser

# Create an instance of the FirestoreUser class
firestore_user = FirestoreUser()

user_list = [
    {
        "name": "test1",
        "email": "test1@example.com",
        "handles": ["handle1", "handle2"],
        "history": [],
        "favorites": [],
        "bookmarks": [],
        "user_id": "test1_id",
    },
    {
        "name": "test2",
        "email": "test2@example.com",
        "handles": ["handle3", "handle4"],
        "history": [],
        "favorites": [],
        "bookmarks": [],
        "user_id": "test2_id",
    },
]


# try:
#     user = User.from_dict(user_list[0])
#     firestore_user.create_user(user)
#     print("User created successfully.")
# except UserAlreadyExistsError as e:
#     print(f"User with ID {user.user_id} already exists.")
# except FirestoreError as e:
#     print("Error creating user:", str(e))

# #Test remove_user method
# try:
#     firestore_user.remove_user(User.from_dict(user_list[0]).user_id)
#     print("User removed successfully.")
# except UserNotFoundError as e:
#     print(f"User with ID {User.from_dict(user_list[0]).user_id} not found.")
# except FirestoreError as e:
#     print("Error removing user:", str(e))

# Test delete_user_field method
# user_id = "test1_id"
# attribute_name = "handles"
# try:
#     firestore_user.delete_user_field(user_id, attribute_name)
#     print(f"{attribute_name} field deleted successfully.")
# except UserNotFoundError as e:
#     print(f"User with ID {user_id} not found.")
# except InvalidUserInputError as e:
#     print(f"Field {attribute_name} does not exist.")
# except FirestoreError as e:
#     print("Error deleting user field:", str(e))

# # Test edit_user_field method
# user_id = "test1_id"
# attribute_name = "s"
# value = "test22@gmail.com"
# try:
#     firestore_user.edit_user_field(user_id, attribute_name, value)
#     print(f"{attribute_name} field edited successfully.")
# except UserNotFoundError as e:
#     print(f"User with ID {user_id} not found.")
# except InvalidUserInputError as e:
#     print(f"Field {attribute_name} does not exist.")
# except FirestoreError as e:
#     print("Error editing user field:", str(e))
#
# # Test get_user method
# user_id = "test1_id"
# try:
#     user = firestore_user.get_user(user_id)
#     print("User retrieved successfully:", user)
# except UserNotFoundError as e:
#     print(f"User with ID {user_id} not found.")
# except FirestoreError as e:
#     print("Error getting user:", str(e))

# Test get_user_field method
user_id = "test1_id"
field_name = "handles"
try:
    field_value = firestore_user.get_user_field(user_id, field_name)
    print(f"{field_name} field value:", field_value)
except UserNotFoundError as e:
    print(f"User with ID {user_id} not found.")
except InvalidUserInputError as e:
    print(f"Field {field_name} does not exist.")
except FirestoreError as e:
    print("Error getting user field:", str(e))
