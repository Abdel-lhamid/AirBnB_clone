#!/usr/bin/python3
"""
Module Custom CMD
"""
import cmd
import re
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage


class HBNBCommand(cmd.Cmd):
    """
    Command line inter class
    """

    prompt = "(hbnb) "
    classes = {"BaseModel": BaseModel,
               "User": User, "State": State,
               "City": City, "Amenity": Amenity,
               "Place": Place, "Review": Review}

    def do_quit(self, arg):
        """Quit command, exits the consol"""
        return True

    def do_EOF(self, arg):
        """ctrl+D to exit the program"""
        print()
        return True

    def emptyline(self):
        """empty line do nothing"""
        pass

    def do_create(self, arg):
        """Create a new instance of the BaseModel"""
        if not arg:
            print("** class name missing **")
            return

        if arg not in self.classes:
            print("** class doesn't exist **")
            return

        new_inst = self.classes[arg]()
        new_inst.save()
        print(new_inst.id)

    def do_show(self, arg):
        """Prints the string representation of an instance
        based on the class name and id"""
        if not arg:
            print("** class name missing **")
            return

        args = arg.split()
        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = args[0] + "." + args[1]
        objects = storage.all()
        if key not in objects:
            print("** no instance found **")
            return
        print(objects[key])

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class
        name and id (save the change into the JSON file)
        """
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return

        key = args[0] + "." + args[1]
        if key not in storage.all():
            print("** no instance found **")
            return
        objects = storage.all()
        del objects[key]
        storage.save()

    def do_all(self, arg):
        """Prints all string representation of all instances
        based or not on the class namie """
        objects = storage.all()
        if not arg:
            print([str(obj) for obj in objects.values()])
            return
        if arg not in self.classes:
            print("** class doesn't exist **")
            return
        else:
            print([str(obj) for key, obj in objects.items()
                   if key.startswith(arg)])

    def do_count(self, arg):
        """Counts the number of instances of a class."""
        if not arg:
            print("** class name missing **")
            return
        if arg not in self.classes:
            print("** class doesn't exist **")
            return
        count = 0
        objects = storage.all()
        for k in objects.keys():
            if k.startswith(arg):
                count += 1
        print(count)

    def do_update(self, arg):
        """
        Updates an instance based on the class name and id
        by adding or updating attribute (save the change into the JSON file)
        """
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = args[0] + "." + args[1]
        objects = storage.all()
        if key not in objects:
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        # Update the instance with the provided attribute-value pairs
        for i in range(2, len(args), 2):
            attribute = args[i]
            try:
                value = eval(args[i+1])
                setattr(objects[key], attribute, value)
            except (SyntaxError, NameError):
                setattr(objects[key], attribute, args[i+1])
                pass

        objects[key].save()

    def precmd(self, arg):
        """handles classname.function()"""
        args = re.search(r"^(\w*)\.(\w+)(?:\(([^)]*)\))$", arg)
        if not args:
            return arg

        class_name = args.group(1)
        if class_name not in self.classes:
            print("** class doesn't exist **")
            return
        method_name = args.group(2)
        arguments = args.group(3).replace('"', '')
        characters_to_remove = '{}",:\''
        for char in characters_to_remove:
            arguments = arguments.replace(char, '')
        correct_commande = method_name + ' ' + class_name + ' ' + arguments
        return correct_commande


if __name__ == '__main__':
    HBNBCommand().cmdloop()
