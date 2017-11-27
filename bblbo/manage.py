#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    sys.dont_write_bytecode = True
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bblbo.settings.dev")
    try:
        from django.core.management import execute_from_command_line
    except ImportError:
        try:
            import django
        except ImportError:
            raise ImportError()
        raise
    print sys.argv
    execute_from_command_line(sys.argv)
