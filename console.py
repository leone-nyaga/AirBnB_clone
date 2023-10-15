#!/usr/bin/python3
# AirBnB_clone

"""
This module contains the entry point of the command interpreter.
"""
import cmd
import shlex
import models
from models.base_model import BaseModel
from models.user import User
from models.engine.file_storage import FileStorage
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

classes = {"BaseModel": BaseModel, "User": User}

class HBNBCommand(cmd.Cmd):
    """
    This class contains the command interpreter.
    """
    prompt = "(hbnb) "
    file = None

    def do_create(self, arg):
        """
        Creates a new instance of BaseModel, saves it (to the JSON file),
        and prints the id.

        Usage: create <class name>
        """
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in classes:
            print("** class doesn't exist **")
            return
        new_instance = classes[class_name]()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        """
        Prints the string representation of an instance
        based on the class name and id.

        Usage: show <class name> <id>
        """
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in classes:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        instance_id = args[1]
        key = "{}.{}".format(class_name, instance_id)
        if key not in models.storage.all():
            print("** no instance found **")
            return
        print(models.storage.all()[key])

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id
        (save the change into the JSON file).

        Usage: destroy <class name> <id>
        """
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in classes:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        instance_id = args[1]
        key = "{}.{}".format(class_name, instance_id)
        if key not in models.storage.all():
            print("** no instance found **")
            return
        del models.storage.all()[key]
        models.storage.save()

    def do_all(self, arg):
        """
        Prints all string representation of all instances
        based or not on the class name.

        Usage: all <class name> or all
        """
        args = shlex.split(arg)
        obj_list = []
        if len(args) == 0:
            for key, value in models.storage.all().items():
                obj_list.append(str(value))
            print(obj_list)
            return
        class_name = args[0]
        if class_name not in classes:
            print("** class doesn't exist **")
            return
        for key, value in models.storage.all().items():
            if key.startswith(class_name):
                obj_list.append(str(value))
        print(obj_list)

    def do_update(self, arg):
        """
        Updates an instance based on the class name and id
        by adding or updating attribute (save the change into the JSON file).

        Usage: update <class name> <id> <attribute name> "<attribute value>"
        """
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in classes:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        instance_id = args[1]
        key = "{}.{}".format(class_name, instance_id)
        if key not in models.storage.all():
            print("** no instance found **")
            return
        if len(args) == 2:
            print("** attribute name missing **")
            return
        attribute_name = args[2]
        if len(args) == 3:
            print("** value missing **")
            return
        attribute_value = args[3]
        obj = models.storage.all()[key]
        setattr(obj, attribute_name, attribute_value)
        obj.save()

    def do_EOF(self, arg):
        """
        Handles the EOF signal.
        """
        print()
        return True

    def do_quit(self, arg):
        """
        Quit command to exit the program.
        """
        return True

    def emptyline(self):
        """
        Do nothing on an empty line.
        """
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()

