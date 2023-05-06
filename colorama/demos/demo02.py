#!/usr/bin/python
# Copyright Jonathan Hartley 2013. BSD 3-Clause license, see LICENSE file.

# Simple demo of changing foreground, background and brightness.

from __future__ import print_function
import fixpath
from colorama_bin import just_fix_windows_console, Fore, Back, Style

just_fix_windows_console()

print(Fore.LIGHTYELLOW_EX + 'green, '
    + Fore.RED + 'red, '
    + Fore.RESET + 'normal, '
    , end='')
print(Back.GREEN + 'green, '
    + Back.RED + 'red, '
    + Back.RESET + 'normal, '
    , end='')
print(Style.DIM + 'dim, '
    + Style.BRIGHT + 'bright, '
    + Style.NORMAL + 'normal'
    , end=' ')
print()
