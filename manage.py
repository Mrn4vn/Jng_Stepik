#!/usr/bin/env python

import os
import sys

def main():
    '''run administrative tasks.'''
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'library.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError (
            'Sorry!(())') from exc
    execute_from_command_line(sys.argv)


    if __name__ == '__main__':
        main()