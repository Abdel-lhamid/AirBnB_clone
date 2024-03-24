#!/usr/bin/python3
"""
Module Custom CMD
"""
import cmd
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from model.review import Review
from models import storage


class HBNBCommand(cmd.Cmd):
    """
    Command line inter class
    """

    prompt = "(hbnb) "
    classes = {"BaseModel": BaseModel,
               "User": User, "State": State,
               "City": City, "Amenity": Amenity
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
        args = arg.split()

        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return

        new_inst = self.classes[args[0]]()
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
        if not args[1]:
            print("** instance id missing **")
            return

        key = args[0] + "." + args[1]
        if key not in storage.all():
            print("** no instance found ** ")
            return
        objects = storage.all()
        del objects[key]
        storage.save()

    def do_all(self, arg):
        """Prints all string representation of all instances
        based or not on the class namie """
        args = arg.split()
        objects = storage.all()
        if not args:
            print([str(obj) for obj in objects.values()])
            return
        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        else:
            print([str(obj) for key, obj in objects.items()
                   if args[0] == key.split('.')[0]])

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
        setattr(objects[key], args[2], args[3])
        objects[key].save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
