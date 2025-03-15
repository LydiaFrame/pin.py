#!/usr/bin/env python3

"""Module to check user's pin against stored pin."""

__author__ = 'Lydia Frame'
__date__ = '3/14/2025'

import sys

def check_pin(file_name):
    """Check the user's pin against the stored pin."""
    try:
        with open(file_name, 'r') as in_file:
            stored_pin = in_file.readline().strip()
    except OSError:
        print('Could not open file - exiting')
        sys.exit()
    
    attempts = 0
    while attempts < 3:
        print()
        try:
            user_pin = int(input('Pin? '))
        except ValueError:
            print('Pin is an integer')
            continue
        
        if user_pin == int(stored_pin):
            print('\nAccess Granted')
            return
        
        attempts += 1
    
    print('\nDenied')

def main():
    """Main function to prompt for file name and check pin."""
    print()
    file_name = input('Pin file? ')
    print()
    check_pin(file_name)
    
if __name__ == '__main__':
    main()
