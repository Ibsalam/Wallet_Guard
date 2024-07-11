#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
# Import necessary modules
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'wallet_guard.settings')

    try:
        # Import the function to execute commands from the command line
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        # Raise an error if Django is not installed or not available in the environment
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    
    # Execute the command line utility with the given arguments    
    execute_from_command_line(sys.argv)


# If this script is run as the main program, call the main function
if __name__ == '__main__':
    main()
