#!/usr/bin/env python3
import os, subprocess
from exit_status import handle_cd, handle_export, handle_unset, handle_exit_status
from history import handle_history, handle_exclamation_mark_history
from path_expansion import handle_tidle, handle_parameter, get_variable
from command_substituation import command_substituation




def identify_command(command, dict_history, dic_var):

    # show history
    if command[0] == 'history':
        return handle_history(command, dict_history)

    # execute command with !
    elif command[0].startswith("!"):
        if len(dict_history) > 1:
            temp = handle_exclamation_mark_history(command, dict_history, dic_var)
            return identify_command(temp, dict_history, dic_var)
        else:
            return [' ']


    # show exit status
    if command[0] == "$?":
        return handle_exit_status()

    # work with tidle expansion
    elif command[0].startswith("~"):
        return handle_tidle(command)

    # save variable and ready to cal
    elif "=" in command[0]:
        return get_variable(command, dic_var)

    # work with paramater expansion
    elif "${" in ' '.join(command) or "$" in ' '.join(command):
        return handle_parameter(command, dic_var)
    elif check_backquote(command):
        return command_substituation(command)
        """
        many thing to handle be here and we can change the order later
        globbing
        handle_exit_status
        subshell with ()
        pipe and redirection >> << > <
        logical operators && and || ★
        quoting
        command substitution with the backquotes - ` `
        """
    else:
        return command

def check_backquote(command):
    for i in command:
        if i.startswith("`") or i.endswith("``"):
            return True
    return False
