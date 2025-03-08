#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def main():
    """Run administrative tasks."""
    settings_module = os.getenv('DJANGO_SETTINGS_MODULE', 'gallarity.settings')
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gallarity.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        logger.error("Django import failed: %s", exc)
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
