import sys
import inspect
import re as Zek_Menu #Change this
#import random_module_to_try_on as Zek_Menu #Another Example
from typing import get_type_hints, Union

'''
Meant to create a menu driven program for the functions inside a module.
The functions need to have Annotations. Parameters who do not have annotations are treated as if they accept string.
Help on the functions will display the docstring.
If user leaves input empty, the default value will be used. If there is no default value,
    Invalid Input will be displayed and the menu will be reprinted.

Change the imported module namespaced as Zek_menu

Currently only shows functions that can be accessed as Zek_menu.func_name

Currently only supports -
    primitive types like int,str etc
    Unions of a single primitive type and None
    List/Other generic type of strings
'''

if __name__ == '__main__':
    name_func_tuples = inspect.getmembers(Zek_Menu, inspect.isfunction)
    #comment next line if you want all functions available (even those imported from elsewhere to be listed
    name_func_tuples = [t for t in name_func_tuples if inspect.getmodule(t[1]) == Zek_Menu]

    def get_default_args(func):
        signature = inspect.signature(func)
        return {
            k: v.default
            for k, v in signature.parameters.items()
            #if v.default is not inspect.Parameter.empty
        }

    choice = -1
    while choice != 0:
        print('Select Function - ')
        for i in range(len(name_func_tuples)):
            print(f'{i+1}\t{name_func_tuples[i][0]}')
        print('0\texit')
        print('-1\thelp')
        try:
            choice = int(input('Enter Choice - '))
            if choice == -1:
                help_choice = int(input('Enter Function Choice to get Help on - '))
                if help_choice == -1:
                    print("Get Help Text for the Function.")
                elif help_choice == 0:
                    print("Exit the Program.")
                else:
                    chosen_func = name_func_tuples[help_choice-1][1]
                    print(inspect.getdoc(chosen_func))
                print()
                continue
            if choice == 0:
                break
            chosen_func = name_func_tuples[choice-1][1]
            default_args = get_default_args(chosen_func)
            type_hints = get_type_hints(chosen_func)
            args = []
            for p in default_args.keys():
                user_input_arg = input(f'{p} - ') or default_args[p]
                try:
                    if type_hints[p].__origin__ is Union:
                        if user_input_arg == default_args[p]:
                            args.append(user_input_arg)
                        else:
                            args.append(type_hints[p].__args__[0](user_input_arg))
                    else:
                        if user_input_arg == default_args[p]:
                            args.append(user_input_arg)
                        else:
                            args.append(type_hints[p].__origin__(user_input_arg.split(",")))
                except:
                    if user_input_arg == default_args[p]:
                        args.append(user_input_arg)
                    else:
                        try:
                            args.append(type_hints[p](user_input_arg))
                        except:
                            args.append(user_input_arg)

            ans = chosen_func(*args) #Function
            if ans is not None:      #Output Stuff
                print(ans)           #you might want to edit
            print()
        except Exception as e:
            print(e,'Invalid Input')
            print()
            continue
