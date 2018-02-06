# This is a list of basic python commands
# version 3.x
# Written Aug 2013 revised Jan 2018
# Author G Lee

# Getting started
# ---------------
print ("Hello")

# Variables:
# ----------
# String
address = '10.10.10.9'  

# Integer
port = 1234

print ("The Server %s" %address + " will listen on port %d" %port + ".")

# Code Blocks
# To define a code block, use indenting

# Decisions
# ---------
import datetime
now = datetime.datetime.now()
t = now.hour
if t < 12:		# note the colon:
   print ("Good morning")
else:
   print ("Good afternoon")
print (" It is now %d" %t + str(now.minute))

# Loops:
#-------
ctr = 1 
print (" I can count")
while (ctr < 11 ):
  print (str(ctr), end=" ")	# end= is ver 3 code
  ctr+=1
print ("")

# cmd line Parameters
#---------
import sys
if len(sys.argv) > 1: 	# check for a parameter
  print ("Hello " + sys.argv[1])
else:
  print ("Usage: Basic.py name")

print ("")

# References
# ------------
print ("References")
print ("http://www.tutorialspoint.com/python/")
print ("http://docs.python.org/2/library/index.html")

# end of file
