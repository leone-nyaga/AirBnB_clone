#!/usr/bin/python3

import json


class FileStorage:
    """Handles serialization and deserialization of objects
    to/from a JSON file."""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return the dictionary of objects."""
        return self.__objects

    def new(self, obj):
        """Add a new object to the objects dictionary."""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Serialize objects to JSON and save them to the file."""
        data = {}
        for key, obj in self.__objects.items():
            data[key] = obj.to_dict()
        with open(self.__file_path, 'w') as file:
            json.dump(data, file)

    def reload(self):
        """Deserialize JSON data from the file and load it into objects."""
        try:
            with open(self.__file_path, 'r') as file:
                data = json.load(file)
                for key, value in data.items():
                    class_name, obj_id = key.split(".")
                    self.__objects[key] = eval(class_name)(**value)
