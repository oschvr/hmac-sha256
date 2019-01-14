import hmac
import hashlib
import binascii
import getopt
import sys

key = ""
message = ""

def usage():
	print
	print "============================"
	print "Simple HMAC-SHA256 Signature"
	print "============================"
	print "Usage: ./hmac-sha256.py -k <key> -m <message>"
	print 
	print "-k --key 		Secure Key"
	print "-m --message             Message to Encrypt"
	print
	sys.exit(0)

def create_sha256_signature(key, message):
	byte_key = binascii.unhexlify(key)
	message = message.encode()
	print hmac.new(byte_key, message, hashlib.sha256).hexdigest().upper()

def main():
	global key
	global message

	# Call usage() if no args
	if not len(sys.argv[1:]):
		usage()

	# Read commandline args
	try:
		opts, args = getopt.getopt(sys.argv[1:], "k:m:", ["key", "message"])
	except getopt.GetoptError as err:
		print str(err)
		usage()

	for o,a in opts:
		if o in ("-k", "--key"):
			key = a
		elif o in ("-m", "--message"):
			message = a
		else:
			assert False, "Unhandled option"

	if len(key) and len(message):
		print "[*] Creating HMAC-SHA256 Signature"
		create_sha256_signature(key, message)
	else: 
		print "[x] Couldn't create HMAC-SHA256 Signature"


main()

