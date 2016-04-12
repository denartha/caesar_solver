import argparse
import sys
ap = argparse.ArgumentParser()
group = ap.add_mutually_exclusive_group(required=True)
group.add_argument('-f', nargs=2) # specify file where cipher is located, second arg is number of shifts
group.add_argument('-s', nargs=2) # specify the string to decode, second arg is number of shifts
group.add_argument('-b', nargs=1) # specify the string to decode, the b denotes brute force, so it will cycle through shifts of 1-25 and print each one

# Grab the opts from argv
opts = ap.parse_args()

#print "arg 1 is " + str(opts.f)
#print opts.f[1]


num = 0

def Shift(msg,key):
	for c in msg:
		if c.isalpha():
			num = ord(c)
			num += key
		if c.isupper():
			if num > ord('Z'):
				num -= 26
			elif num < ord('A'):
				num += 26
		elif c.islower():
			if num > ord('z'):
				num -= 26
			elif num < ord('a'):
				num += 26
		elif c.isspace:
				num = 32

		sys.stdout.write(chr(num))






if opts.s:
	msg = opts.s[0]
	key = int(opts.s[1])
	num = 0
	Shift(msg,key)
	print ""




# brute force function
if opts.f:
	file = opts.f[0] 
	key = int(opts.f[1])
	with open(file, 'r') as myfile:
		msg=myfile.read().replace('\n', ' ')
		Shift(msg,key)
		print ""
		
if opts.b:
	msg = opts.b[0]
	num = 0
	for key in range(26):
			print str(key) + ': ',
			Shift(msg,key)
			print ""

