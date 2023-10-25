#!/usr/bin/python3

"""interactive shell"""

import cmd
import re
import models
from models.base_model import BaseModel
from models import storage
import json
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

class_home = {
    "BaseModel": BaseModel,
    "User": User,
    "Place": Place,
    "Amenity": Amenity,
    "City": City,
    "Review": Review,
    "State": State
}


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb)  '

    def do_EOF(self, line):
        """exits the console"""
        print("")
        return True

    def do_quit(self, line):
        """exits the program"""
        print("Good Bye!")
        return True

    def help_quit(self):
        """when two arguments involve"""
        print('\n'.join(["Quit command to exit the program"]))

    def emptyline(self):
        """ overwriting the emptyline method """
        return False
        # OR
        # pass

    def do_create(self, line):
        """Creates a new instances of a class"""
        if line:
            try:
                glo_cls = globals().get(line, None)
                obj = glo_cls()
                obj.save()
                print(obj.id)  # print the id
            except Exception:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_show(self, line):
        """Prints the string representation of an instance"""
        arr = line.split()    # split & assign to varia

        if len(arr) < 1:
            print("** class name missing **")
        elif arr[0] not in class_home:
            print("** class doesn't exist **")
        elif len(arr) < 2:
            print("** instance id missing **")
        else:
            new_str = f"{arr[0]}.{arr[1]}"
            if new_str not in storage.all():
                print("** no instance found **")
            else:
                print(storage.all()[new_str])

    def do_destroy(self, line):
        """Destroy command deletes an instance based on the class name and id
        """
        arr = line.split()
        if len(arr) < 1:
            print("** class name missing **")
        elif arr[0] not in class_home:
            print("** class doesn't exist **")
        elif len(arr) < 2:
            print("** instance id missing **")
        else:
            new_str = f"{arr[0]}.{arr[1]}"
            if new_str not in storage.all().keys():
                print("** no instance found **")
            else:
                storage.all().pop(new_str)
            #    del (storage.all()[new_str])
                storage.save()

    def do_all(self, line):
        """ Print all instances in string representation """
        objects = []
        if line == "":
            print([str(value) for key, value in storage.all().items()])
        else:
            st = line.split(" ")
            if st[0] not in class_home:
                print("** class doesn't exist **")
            else:
                for key, value in storage.all().items():
                    clas = key.split(".")
                    if clas[0] == st[0]:
                        objects.append(str(value))
                print(objects)

    def do_update(self, line):
        """Update a class instance of a given id by adding or updating
        a given attribute key/value pair or dictionary.
        usage:  update <class> <id> <attribute_name> <attribute_value> or
                <class>.update(<id>, <attribute_name>, <attribute_value>) or
                <class>.update(<id>, <dictionary>)
        """
        arr = line.split()
        if len(arr) < 1:
            print("** class name missing **")
            return
        elif arr[0] not in class_home:
            print("** class doesn't exist **")
            return
        elif len(arr) < 2:
            print("** instance id missing **")
            return
        else:
            new_str = f"{arr[0]}.{arr[1]}"
            if new_str not in storage.all().keys():
                print("** no instance found **")
            elif len(arr) < 3:
                print("** attribute name missing **")
                return
            elif len(arr) < 4:
                print("** value missing **")
                return
            else:
                setattr(storage.all()[new_str], arr[2], arr[3])
                storage.save()

    def do_count(self, line):
        """Print the count all class instances"""
        kclass = globals().get(line, None)
        if kclass is None:
            print("** class doesn't exist **")
            return
        count = 0
        for obj in storage.all().values():
            if obj.__class__.__name__ == line:
                count += 1
        print(count)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
