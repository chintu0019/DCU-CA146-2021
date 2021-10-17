#!/usr/bin/env python

import sys
import os
import morse_code
import sos

(a, b) = morse_code.check()
print "call count for dot():", a
print "call count for dash():", b
