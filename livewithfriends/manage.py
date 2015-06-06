#!/usr/bin/env python
import os
import sys

# Enable tab completion in shell_plus
import readline
import rlcompleter
if 'libedit' in readline.__doc__:
    readline.parse_and_bind("bind ^I rl_complete")
else:
    readline.parse_and_bind("tab: complete")

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "livewithfriends.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
