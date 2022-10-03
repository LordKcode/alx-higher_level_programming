#!/usr/bin/python3
""" Base class module
"""
import json


class Base:
    """ Base class
    """

    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries.
        list_dictionaries: a list of dictionaries.
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation.
        json_string: a string representing a list of dictionaries.
        """
        if json_string is None or json_string is "":
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to a file.
        list_objs: a list of instances who inherits of Base.
        """
        with open(cls.__name__ + ".json", 'w', encoding="UTF-8") as myfile:
            mylist = []
            if list_objs is not None:
                for obj in list_objs:
                    mylist.append(obj.to_dictionary())
            myfile.write(cls.to_json_string(mylist))

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set.
        dictionary: key/value pairs of attributes of the class.
        """
        if cls.__name__ is 'Square':
            instance = cls(1)
        else:
            instance = cls(1, 1)
        instance.update(**dictionary)
        return instance

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances of the class."""
        try:
            with open(cls.__name__ + ".json", 'r', encoding="UTF-8") as myfile:
                dict_list = cls.from_json_string(myfile.read())
                instance_list = []
                for obj in dict_list:
                    instance_list.append(cls.create(**obj))
                return instance_list
        except FileNotFoundError:
            return []
