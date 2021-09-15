#!/usr/bin/env python
from functions import *
def main(command=None,item=None):
    if command==None:
        how_to_use("How to use")
        len_argv=len(sys.argv)
        if len_argv==1:
            argv_1=input('command\n')
            if argv_1.count('/')>1:
                main(command='add',item=argv_1)
            elif argv_1!='start':
                argv_2=input('item\n')
                len_argv=2
        else:
            argv_1=sys.argv[1]
            try:
                argv_2=None if argv_1=='start' else sys.argv[2]
            except BaseException:
                argv_2 = input('item')
    else:
        argv_1=command
        argv_2=None if item==None else input('item?')
        len_argv=2 if argv_2==None else 3

    check_for_database()

    if argv_1 == "start":
        dl_start()

    elif argv_1 == "custom":
        if len(sys.argv) > 2 or len_argv>1:
            custom_dl(argv_2)
        else:
            how_to_use("Missing item")

    elif argv_1 == "add":
        if len(sys.argv) > 2 or len_argv>1:
            add_check(argv_2)
            main()
        else:
            how_to_use("Missing item")

    elif argv_1 == "delete":
        if len(sys.argv) > 2 or len_argv>1:
            type_check(argv_2)
            list_items(argv_2)
            u_input = input("Please enter the ID to delete (or c to cancel): ")
            if u_input == "c":
                print("Operation canceled.")
            else:
                delete_item(u_input)
        else:
            how_to_use("Missing item")

    elif argv_1 == "list":
        if len(sys.argv) > 2 or len_argv>1:
            type_check(argv_2)
            list_items(argv_2)
        else:
            how_to_use("Missing item")

    elif argv_1 == "help":
        help_command()

    else:
        how_to_use("Command not found!")



if __name__ == '__main__':
    while True:
        main()
