#!/usr/bin/env python
import sys
from soundex import soundex


if __name__ == '__main__':

	arg = sys.argv[1]

	for txt in arg.split(','):
		sound = soundex(txt.strip())
		print(txt.strip(), sound)