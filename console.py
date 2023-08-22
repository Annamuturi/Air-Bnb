#!/usr/bin/python3
"""Defines the HBNB console, a command-line interface for managing objects."""
import cmd
from shlex import split
from models import storage

# Import all the model classes
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

class HBNBCommand(cmd.Cmd):
    """Defines the HolbertonBnB command interpreter."""

    prompt = "(hbnb) "
    valid_classes = {
        "BaseModel",
        "User",
        "State",
        "City",
        "Amenity",
        "Place",
        "Review"
    }

    def emptyline(self):
        """Ignore empty input."""
        pass

    def do_quit(self, line):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, line):
        """EOF signal to exit the program."""
        print("")
        return True

    def do_create(self, line):
        """Create a new instance with given attributes and print its ID.
        Usage: create <class_name> [<key>=<value> ...]
        """
        try:
            if not line:
                raise SyntaxError("Class name is missing.")
            
            args = split(line)
            class_name = args[0]
            
            if class_name not in self.valid_classes:
                raise NameError("Invalid class name.")

            kwargs = {}
            for arg in args[1:]:
                key, value = arg.split("=")
                kwargs[key] = value

            obj = eval(class_name)(**kwargs)
            storage.new(obj)
            storage.save()
            
            print(obj.id)
            
        except SyntaxError as e:
            print(f"Error: {e}")
        except NameError:
            print("** Invalid class name **")
        except Exception as e:
            print(f"Error: {e}")

    def do_show(self, line):
        """Prints the string representation of an instance.
        Usage: show <class_name> <object_id>
        """
        try:
            if not line:
                raise SyntaxError("Class name and object ID are missing.")
            
            args = split(line)
            class_name = args[0]
            
            if class_name not in self.valid_classes:
                raise NameError("Invalid class name.")
            
            if len(args) < 2:
                raise IndexError("Object ID is missing.")

            objects = storage.all()
            key = f"{class_name}.{args[1]}"
            if key in objects:
                print(objects[key])
            else:
                print("** No instance found **")

        except SyntaxError as e:
            print(f"Error: {e}")
        except NameError:
            print("** Invalid class name **")
        except IndexError:
            print("** Object ID is missing **")

    # ... (similarly update the other methods)

if __name__ == '__main__':
    HBNBCommand().cmdloop()

