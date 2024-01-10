#!/usr/bin/python3
"""CLI"""

import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """Entry point to CI"""

    prompt = "(hbnb) "
    actual_class = ["BaseModel"]

    def do_quit(self, *args):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, *args):
        """Exit program"""
        return True

    def emptyline(self):
        """Execute nothing"""
        pass

    def do_create(self, line):
        """Create instance of BaseModel & save json file"""
        args = line.split()

        if len(args) == 0:
            print("** class name missing **")

        elif args[0] not in HBNBCommand.actual_class:
            print("** class doesn't exist**")

        else:
            target_class = globals()[args[0]]
            new = target_class()
            print(new.id)
            new.save()

    def do_show(self, line):
        """Prints the string representation of instance based on class name & id"""
        args = line.split()

        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.actual_class:
            print("** class doesn't exist **")
        elif len(args) <= 1:
            print("** instance id missing **")
        else:
            target_class = globals()[args[0]]
            inst_id = args[1]
            if target_class:
                key = f"{args[0]}.{inst_id}"
                obj = storage.all()
                if key in obj:
                    print(obj[key])
                else:
                    print("** no instance found **")

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id"""
        args = line.split()

        if not args == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.actual_class:
            print("** class doesn't exist **")
        elif len(args) <= 1:
            print("** instance id missing **")
        else:
            target_class = globals()[args[0]]
            inst_id = args[1]
            key = f"{args[0]}.{inst_id}"
            obj = storage.all()
            if key in obj:
                del obj[key]
                storage.save()
            else:
                print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
