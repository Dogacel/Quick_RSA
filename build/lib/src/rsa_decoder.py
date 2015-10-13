#!/usr/bin/env python

import os, argparse, rsa, binascii


def main():
	parser = argparse.ArgumentParser(description='RSA decoder, encoder')
	
	subparsers = parser.add_subparsers(help='sub-command help')
	
	parser_generate_key = subparsers.add_parser('gkey', help='Helps you to create key')
	parser_generate_key.add_argument('--bsize', '-s', dest="bsize",default=512, type=int, help='Byte size for key')
	parser_generate_key.add_argument('--overwrite', '-o', default=False, action='store_true', help='Whether overwrite file or not')
	parser_generate_key.add_argument('--filepath', '-f', dest="fpath", default="~", type=str, help='File path to be saved')
	parser_generate_key.add_argument('--filename', '-n', dest="fname", default="mykey", type=str, help="File name to be saved, w/o extension")
	parser_generate_key.set_defaults(which='gkey')
	
	'''
	parser_decode = subparsers.add_parser('decode', help='Decode files')
	parser_decode.add_argument('--file','-f', type=str, help='File location , name , extension')
	parser_decode.add_argument('--privatekey','-p', type=str, help='Private key location , name , extension')
	parser_decode.set_defaults(which='decode')
	
	parser_encode = subparsers.add_parser('encode', help='b help')
	parser_encode.add_argument('--file','-f', type=int, help='bar help')
	parser_encode.add_argument('--file','-f', type=int, help='bar help')
	parser_encode.set_defaults(which='encode')
	'''
	
	args = parser.parse_args()
	
	if args.which == "gkey":
		if args.bsize < 16 or args.bsize > 4096:
			print("Too small or big key size")
		elif (os.path.exists(args.fpath + "/" + args.fname + "_private.pem") or os.path.exists(args.fpath + "/" + args.fname + "_public.pem")) and not args.overwrite:
			print("File(s) already exist !")
		else:
			if args.overwrite:
				try:
					os.remove(args.fpath + "/" + args.fname + "_private.pem")
					os.remove(args.fpath + "/" + args.fname + "_public.pem")
					print("Deleted old files.")
				except:
					print("Deleted old files.")
			(pubkey, privkey) = rsa.newkeys(args.bsize)
			try:
				ofile = open(args.fpath + "/" + args.fname + "_private.pem", "wb")
				ofile.write( privkey.save_pkcs1(format='PEM') )
				ofile.close()
				ofile = open(args.fpath + "/" + args.fname + "_public.pem", "wb")
				ofile.write( pubkey.save_pkcs1(format='PEM') )
			except:
				pass
			print("Created key files sucessfully")
	
	
	toenc = input().encode('utf-8')		
	print("\nWill be encrypted : " + toenc.decode('utf-8'))
	print("After encryption  : " + binascii.hexlify(rsa.encrypt(toenc, pubkey) ).decode('utf-8'))
	print("After decryption  : " + rsa.decrypt(rsa.encrypt(toenc, pubkey), privkey).decode('utf-8'))
	
	return 0


if __name__ == '__main__':
	main()

