#!/usr/bin/env python

import os, argparse, rsa, binascii
import rsa_handler as qrsa


def main():
	parser = argparse.ArgumentParser(description='RSA decoder, encoder')
	
	subparsers = parser.add_subparsers(help='sub-command help')
	
	parser_generate_key = subparsers.add_parser('gkey', help='Helps you to create key')
	parser_generate_key.add_argument('--bsize', '-s', dest="bsize",default=512, type=int, help='Byte size for key')
	parser_generate_key.add_argument('--overwrite', '-o', default=False, action='store_true', help='Whether overwrite file or not')
	parser_generate_key.add_argument('--filepath', '-f', dest="fpath", default=os.path.expanduser("~"), type=str, help='File path to be saved')
	parser_generate_key.add_argument('--filename', '-n', dest="fname", default="ukey", type=str, help="File name to be saved, w/o extension")
	parser_generate_key.set_defaults(which='gkey')
	
	
	parser_decode = subparsers.add_parser('decode', help='Decode files')
	parser_decode.add_argument('--infile','-f', type=str, help='File location , name , extension')
	parser_decode.add_argument('--privatekey','-p', type=str, help='Private key location , name , extension')
	parser_decode.set_defaults(which='decode')
	
	parser_encode = subparsers.add_parser('encode', help='b help')
	parser_encode.add_argument('--infile','-f', type=str, help='File location , name , extension')
	parser_encode.add_argument('--publickey','-p', type=str, help='Public key location , name , extension')
	parser_encode.set_defaults(which='encode')
	
	args = parser.parse_args()
	
	handler = qrsa.rsa_handler()
	handler.switch( args ) 
	
	return 0


if __name__ == '__main__':
	main()

