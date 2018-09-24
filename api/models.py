from . import entries


class User:
    """The User is the person who interacts with the application """
    def __init__(self, user_id, first_name, last_name, email, password):
        self.user_id = user_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.registered_users = dict()  # To keep track of the registered users


class Diary:
    """The Diary is where the user makes and views entries"""
    def __init__(self, diary_id, diary_name, date_created, date_modified):
        self.diary_id = diary_id
        self.diary_name = diary_name
        self.date_created = date_created
        self.date_modified = date_modified
        self.registered_diaries = dict()


class Entry:
    """This class represents all possible entries made by user"""
    def __init__(self, entry_id, date_added, date_modified, entry_text):
        self.entry_id = entry_id
        self.date_added = date_added
        self.date_modified = date_modified
        self.entry_text = entry_text

    def create_entry(self):
        "creates an entry"
        global entries
        new_entry = {
            "entry_id": self.entry_id,
            "date_added": self.date_added,
            "date_modified": self.date_modified,
            "entry_text": self.entry_text
        }
        entries.append(new_entry)
        return True
