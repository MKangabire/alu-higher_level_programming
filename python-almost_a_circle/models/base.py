#!/usr/bin/python3
<<<<<<< HEAD
"""
This is a python module

that has the class base

This class will be the “base”

of all other classes in this project

The goal of it is to manage id attribute

in all your future classes and to avoid

duplicating the same code (by extension, same bugs)
"""


=======
'''Creates a class called Base
'''
>>>>>>> 9bca717da99d5c666cf05a40fab020738d7bae44
import json
import csv


class Base:
<<<<<<< HEAD
    """
    This class base has the following;

    private class attribute __nb_objects = 0

    class constructor: def __init__(self, id=None):
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        This is the initialization

        constructor method for each

        instance or object of this class
        """
        if id is not None:
=======
    '''This class will be the base of all other classes in this Project
    '''
    __nb_objects = 0

    def __init__(self, id=None):
        '''Initializes new base instance

        Args:
           id (int): Used as identifier for subclasses incase of debugging
        '''
        if id is None:
            self.__class__.__nb_objects += 1
            self.id = self.__class__.__nb_objects
        else:
>>>>>>> 9bca717da99d5c666cf05a40fab020738d7bae44
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries: dict):
        '''Converts a list containing dictionaries to JSON


        Args:
           list_dictionaries (list): List of dictionaries converted to JSON
        '''
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        else:
<<<<<<< HEAD
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        JSON is one of the standard formats for sharing data representation.

        the static method def to_json_string(list_dictionaries)

        that returns the JSON string representation of list_dictionaries

        list_dictionaries is a list of dictionaries

        If list_dictionaries is None or empty, return the string: "[]"

        Otherwise, return the JSON string representation of list_dictionaries
        """
        if list_dictionaries is None:
            return "[]"
        else:
=======
>>>>>>> 9bca717da99d5c666cf05a40fab020738d7bae44
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
<<<<<<< HEAD
        """
        the class method def save_to_file(cls, list_objs)

        that writes the JSON string representation of list_objs to a file

        list_objs is a list of instances who inherits of Base

        example: list of Rectangle or list of Square instances

        If list_objs is None, save an empty list

        The filename must be: <Class name>.json - example: Rectangle.json

        You must use the static method to_json_string (created before)

        You must overwrite the file if it already exists
        """
        if list_objs is None:
            data = cls.to_json_string(list_objs)
            data = json.loads(data)
            with open(f"{cls.__name__}.json", mode="w", encoding="utf-8") \
                    as classfile:
                json.dump(data, classfile)
            return 1
        else:
            new_list_objs = []
            for i in range(len(list_objs)):
                hash_maps = list_objs[i].to_dictionary()
                new_list_objs.append(hash_maps)
            data = cls.to_json_string(new_list_objs)
            data = json.loads(data)
            with open(f"{cls.__name__}.json", mode="w", encoding="utf-8") \
                    as classfile:
                json.dump(data, classfile)
            return 0

    @staticmethod
    def from_json_string(json_string):
        """
        the static method def from_json_string(json_string)

        that returns the list of the JSON string

        representation json_string
        """
        if json_string is None:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        the class method def create(cls, **dictionary)

        that returns an instance with all attributes already set

        **dictionary can be thought of as a double pointer to a dictionary

        To use the update method to assign all attributes,

        you must create a “dummy” instance before

        Create a Rectangle or Square instance with “dummy”

        mandatory attributes (width, height, size, etc.)

        Call update instance method to this “dummy”

        instance to apply your real values

        You must use the method def update(self, *args, **kwargs)

        **dictionary must be used as **kwargs of the method update

        You are not allowed to use eval
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(3, 4)
            update_dummy = dummy.update(**dictionary)
            return dummy
        else:
            dummy = cls(4)
            update_dummy = dummy.update(**dictionary)
            return dummy

    @classmethod
    def load_from_file(cls):
        """
        the class method def load_from_file(cls)

        that returns a list of instances

        The filename must be: <Class name>.json - example: Rectangle.json

        If the file doesn’t exist, return an empty list

        Otherwise, return a list of instances -

        the type of these instances depends on cls

        (current class using this method)

        You must use the from_json_string and

        create methods (implemented previously)
        """
        try:
            with open(f"{cls.__name__}.json", mode="r", encoding="utf-8") \
                    as classfile:
                new_object_list = []
                data = classfile.read()
                data = cls.from_json_string(data)
                for i in range(len(data)):
                    obj_data = data[i]
                    obj = cls.create(**obj_data)
                    new_object_list.append(obj)
                return new_object_list
        except FileNotFoundError:
            return []
=======
        '''Converts square, rectangle objects to json and saves them in files

        Args:
           list_objs (list): A list of Square of Rectangle objects
        '''
        class_name = cls.__name__
        with open(f"{class_name}.json", 'w') as f:
            if list_objs is None or list_objs == []:
                f.write("[]")
            else:
                dict_list = [value.to_dictionary() for value in list_objs]
                list_objs_json = cls.to_json_string(dict_list)
                f.write(list_objs_json)

    @staticmethod
    def from_json_string(json_string):
        '''Converts json string back into an object

        Args:
           json_string (str): JSON formatted string
        '''
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        '''Creates a new instance of Square, Rectangle based on dictionary

        Args:
           dictionary (dict): A dictionary containing values to set to instance
        '''
        if cls.__name__ == "Square":
            my_square = cls(1)
            my_square.update(**dictionary)
            return my_square
        elif cls.__name__ == "Rectangle":
            my_rectangle = cls(4, 4)
            my_rectangle.update(**dictionary)
            return my_rectangle

    @classmethod
    def load_from_file(cls):
        '''Loads a Square or Rectangle object from a json file
        if the file is not found an empty string is returned
        '''
        try:
            with open(f"{cls.__name__}.json", 'r') as f:
                f_json = f.read()
        except FileNotFoundError:
            return []
        obj_dict_list = cls.from_json_string(f_json)
        return [cls.create(**value) for value in obj_dict_list]

    @classmethod
    def save_to_file_csv(cls, list_objs):
        '''Stores rectangle/square objects to a .csv file

        Args:
           list_objs (list): A list of Square/Rectangle objects.
        '''
        name = cls.__name__
        with open(f"{name}.csv", 'w') as csv_file:
            csv_writer = csv.writer(csv_file, delimiter=",")
            if list_objs is None or list_objs == []:
                csv_writer.writerow("")
            else:
                for obj in list_objs:
                    if name == "Square":
                        csv_writer.writerow([obj.id, obj.size, obj.x, obj.y])
                    elif name == "Rectangle":
                        csv_writer.writerow([obj.id, obj.width,
                                             obj.height, obj.x, obj.y])

    @classmethod
    def load_from_file_csv(cls):
        '''Retrieves data from a .csv file and
        returns a list of Square/Rectangle Objects
        '''
        result = []
        name = cls.__name__
        with open(f"{name}.csv", 'r') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=",")
            for row in csv_reader:
                if name == "Square":
                    result.append(cls.create(id=int(row[0]), size=int(row[1]),
                                             x=int(row[2]), y=int(row[3])))
                elif name == "Rectangle":
                    result.append(cls.create(id=int(row[0]), width=int(row[1]),
                                             height=int(row[2]), x=int(row[3]),
                                             y=int(row[4])))
        return result
>>>>>>> 9bca717da99d5c666cf05a40fab020738d7bae44
