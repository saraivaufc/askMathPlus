#!/usr/bin/env python
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(sys.path[0])
sys.path.append(sys.path[0]+"/askMathPlus")

if __name__ == "__main__":
	os.environ.setdefault("DJANGO_SETTINGS_MODULE", "askMathPlus.settings")

	from django.core.management import execute_from_command_line
	execute_from_command_line(sys.argv)

#find . -name '*.pyc' -delete
