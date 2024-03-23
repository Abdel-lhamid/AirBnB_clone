#!/usr/bin/python3
"""
Module Custom CMD
"""
import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """
    Command line inter class
    """

    prompt = "(hbnb) "
    classes = {"BaseModel": BaseModel}

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
        args = arg.split()

        if args[0] is not "BaseModel":
            print("** class doesn't exist **")
            return

        new_inst = BaseModel()
        new_inst.save()
        print(new_inst.id)

    def do_show(self, arg):
        """Prints the string representation of an instance
        based on the class name and id"""
        if not arg:
            print("** class name missing **")

        args = args.split()
        if args[0]

if __name__ == '__main__':
    HBNBCommand().cmdloop()
