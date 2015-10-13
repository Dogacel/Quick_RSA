import os, rsa
from rsa.bigfile import *

class rsa_handler:
	
	#def __init__(self):
	
	def file_exists(self, fpath):
		return os.path.exists(fpath)
	
	def generate_key(self, bsize):
		return rsa.newkeys(bsize)
	
	
	def switch(self, args):
		if hasattr(args, 'which'):
			sel = args.which
			if sel == 'gkey':
				(pubkey, privkey) = self.generate_key(args.bsize)
				if self.file_exists(args.fpath+"/"+args.fname) and not(args.overwrite):
					print("That file already exists ! Use -o to overwrite.")
				else:
					if self.file_exists(args.fpath+"/"+args.fname):
						os.remove(args.fpath + "/" + args.fname)
					save_file = open(args.fpath+"/"+args.fname, 'wb')
					save_file.write( pubkey.save_pkcs1(format='PEM') )
					save_file.close()
					#private
					save_file = open(args.fpath+"/pv_"+args.fname, 'wb')
					save_file.write( privkey.save_pkcs1(format='PEM') )
					save_file.close()
					print("Written files sucessfully !")
			elif sel == 'encode':
				pubkey_f = open(args.publickey, 'rb')
				pubkey = rsa.PublicKey.load_pkcs1(pubkey_f.read(), format='PEM')
				with open(args.infile, 'rb') as infile, open(args.infile+'_out', 'wb+') as outfile:
					encrypt_bigfile(infile, outfile, pubkey)
			elif sel == 'decode':
				privkey_f = open(args.privatekey, 'rb')
				privkey = rsa.PrivateKey.load_pkcs1(privkey_f.read(), format='PEM')
				with open(args.infile, 'rb') as infile, open(args.infile+'_out', 'wb+') as outfile:
					decrypt_bigfile(infile, outfile, privkey)
				
		else:
			print("You must use a subparser to select a command")
			return 0
