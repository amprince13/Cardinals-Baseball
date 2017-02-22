import sys, os

if len(sys.argv) < 2:
	sys.exit("Usage: %s filename" % sys.argv[0])

filename = sys.argv[1]
if not os.path.exists(filename):
	sys.exit("Error: File '%s' not found" % sys.argv[1]

with open(sys.argv[1]) as f:
    f_contents = f.readlines[3:]
    print f_contents
