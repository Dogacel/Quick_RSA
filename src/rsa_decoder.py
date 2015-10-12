#!/usr/bin/env python

import os, argparse, hashlib, rsa, uuid


def main():
	parser = argparse.ArgumentParser(description='RSA decoder, encoder')
	
	subparsers = parser.add_subparsers(help='sub-command help')
	
	parser_generate_key = subparsers.add_parser('gkey', help='Helps you to create key')
	parser_generate_key.set_defaults(which='gkey')
	
	parser_decode = subparsers.add_parser('decode', help='Decode files')
	parser_decode.add_argument('--file','-f', type=str, help='File location , name , extension')
	parser_decode.set_defaults(which='decode')
	
	parser_encode = subparsers.add_parser('encode', help='b help')
	parser_encode.add_argument('--file','-f', type=int, help='bar help')
	parser_encode.set_defaults(which='encode')
	
	args = parser.parse_args()
	
	print(args.which)
	
	'''
	f = open(args.fl, "r")
	print(f.read().splitlines())
	'''
	return 0

if __name__ == '__main__':
	main()

