class User:
    """
    Represents a user.

    Attributes:
        name (str): The name of the user.
        email (str): The email address of the user.
        handles (dict): A dictionary of handles for competitive programming websites.
            The keys are the names of the websites (e.g. "Codeforces", "Atcoder", "Codechef"),
            and the values are the handles for the user on those websites.
        history (list): A list of URLs representing the user's browsing history.
        bookmarks (list): A list of materials that the user bookmarked.
        favorites (list): A list of materials the user marked as favorites.
    """

    def __init__(self, name, email, handles, history, bookmarks, favorites, user_id):
        """
        Initializes a new instance of the User class.

        Args:
            name (str): The name of the user.
            user_id (str): The id of the user from the Firebase.
            email (str): The email address of the user.
            handles (dict): A dictionary of handles for competitive programming websites.
                The keys are the names of the websites (e.g. "Codeforces", "Atcoder", "Codechef"),
                and the values are the handles for the user on those websites.
            history (list): A list of the materials representing the user's browsing history.
            bookmarks (list): A list of the materials that the user bookmarked.
            favorites (list): A list of the materials that the user marked as favorites.
        """
        self.user_id = user_id
        self.name = name
        self.email = email
        self.handles = handles
        self.history = history
        self.bookmarks = bookmarks
        self.favorites = favorites

    def add_handle(self, website, handle):
        """
        Add a handle for a specific competitive programming website.

        Args:
            website (str): The name of the website.
            handle (str): The handle for the user on the website.
        """
        self.handles[website] = handle

    def remove_handle(self, website):
        """
        Remove the handle for a specific competitive programming website.

        Args:
            website (str): The name of the website.
        """
        del self.handles[website]

    def get_handle(self, website):
        """
        Get the handle for a specific competitive programming website.

        Args:
            website (str): The name of the website.

        Returns:
            str: The handle for the user on the website.
        """
        return self.handles.get(website)

    def get_all_handles(self):
        """
        Get all handles for the user on different competitive programming websites.

        Returns:
            dict: A dictionary of handles, where keys are the website names and values are the handles.
        """
        return self.handles

    def add_history(self, material):
        """
        Add an material URL to the user's browsing history.

        Args:
            material (str): The URL of the material.
        """
        self.history.append(material)

    def remove_history(self, material):
        """
        Remove an material URL from the user's browsing history.

        Args:
            material (str): The URL of the material.
        """
        self.history.remove(material)

    def get_history(self):
        """
        Get the user's browsing history.

        Returns:
            list: A list of URLs representing the user's browsing history.
        """
        return self.history
      
    def add_favorite(self, material):
        """
        Adds an material to the user's favorites.

        Args:
            material (Material): The material to add to the favorites.
        """
        self.favorites.append(material)

    def remove_favorite(self, material):
        """
        Removes an material from the user's favorites.

        Args:
            material (Material): The material to remove from the favorites.
        """
        self.favorites.remove(material)

    def get_favorites(self):
        """
        Retrieves the user's favorite materials.

        Returns:
            list: A list of the user's favorite materials.
        """
        return self.favorites

    def parse_data(self, data):
        """
        Parses user data from a dictionary and updates the user attributes.

        Args:
            data (dict): A dictionary containing the user data.
        """
        self.name = data['name']
        self.email = data['email']
        self.handles = data['handles']
        self.history = data['history']
        self.bookmarks = data['bookmarks']
        self.favorites = data['favorites']

    def __str__(self):
        """
        Returns a string representation of the User object.

        Returns:
            str: A string representation of the User object.
        """
        return f"Name: {self.name}\nEmail: {self.email}\nHandles: {self.handles}\nHistory: {self.history}\nBookmarks: {self.bookmarks}\nFavorites: {self.favorites}"

    @classmethod
    def from_dict(cls, data):
        """
        Creates a User object from a dictionary.

        Args:
            data (dict): A dictionary containing the user data.

        Returns:
            User: The User object.

        Raises:
            KeyError: If a required field is missing in the data dictionary.
        """
        try:
            user_id = data['user_id']
            name = data['name']
            email = data['email']
            handles = data['handles']
            history = data['history']
            bookmarks = data['bookmarks']
            favorites = data['favorites']

            return cls(name, email, handles, history, bookmarks, favorites, user_id)

        except KeyError as e:
            raise KeyError(f"Missing required field: {str(e)}") from e
