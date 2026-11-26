#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
<<<<<<< HEAD
<<<<<<< HEAD

=======
>>>>>>> 4d3827e50b05cfeb8f64e227feeb48358fc9f862
=======
>>>>>>> 4d3827e50b05cfeb8f64e227feeb48358fc9f862
import os
import sys


def main():
    """Run administrative tasks."""
<<<<<<< HEAD
<<<<<<< HEAD
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "GestionCabinetMedical.settings")
=======
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
>>>>>>> 4d3827e50b05cfeb8f64e227feeb48358fc9f862
=======
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
>>>>>>> 4d3827e50b05cfeb8f64e227feeb48358fc9f862
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


<<<<<<< HEAD
<<<<<<< HEAD
if __name__ == "__main__":
=======
if __name__ == '__main__':
>>>>>>> 4d3827e50b05cfeb8f64e227feeb48358fc9f862
=======
if __name__ == '__main__':
>>>>>>> 4d3827e50b05cfeb8f64e227feeb48358fc9f862
    main()
