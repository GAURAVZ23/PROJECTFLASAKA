#! /usr/bin/python

import sys
import logging


logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/var/www/FlasakaApp/")

from FlasakaApp import app as application
application.secret_key = ";jhdsahdfk;kasbkak"
