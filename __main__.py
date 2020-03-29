import os, stat, argparse, sys
from OWNHUSHED.encrypt import *

parser = argparse.ArgumentParser(description="Refer to README.md for program information. Note, depending on your current login, this program may require root user permissions. In this case, please run with sudo. (sudo python3 OWNHUSHED)")
subparsers = parser.add_subparsers()
protect = subparsers.add_parser("protect")
protect.add_argument("-f", type=str, required=True, help="File/directory to modify")
protect.add_argument("-p", type=str, required=True, choices=list("ARPST"), help="Permission to set")
protect.add_argument("--user", type=str, required=False, default=None, help="GnuPG user key initials. Only required for permission level S or T")# use `--user` because it is the gpg standard input method.
release = subparsers.add_parser("release")
release.add_argument("-f", type=str, required=True, help="Name of file to decrypt. Exclude beginning `.` and file format")
release.add_argument("--user", type=str, required=True, help="GnuPG user key initials. Required to decrypt level S or T files")

args = parser.parse_args()

def oct_perm(perm):
	val = 0
	if 'r' in perm: val |= 4
	if 'w' in perm: val |= 2
	if 'x' in perm: val |= 1
	return val

def full_perm(perm):
	USR = oct_perm(perm[:3]) << 6
	GRP = oct_perm(perm[3:6]) << 3
	OTH = oct_perm(perm[6:])
	return USR | GRP | OTH

octalPermission = {
	'A': full_perm("rwxrwxrwx"),
	'R': full_perm("rwxr--r--"),
	'P': full_perm("rwx------")
}

if not 'p' in vars(args):# release files
	user = args.user
	file = args.f
	decrypt(file, user)
else:# protect files
	file = args.f
	perm = args.p
	user = args.user

	if perm in "ST":
		if user:
			encrypt(file, user)
		else:
			raise Exception("Must specify GPG user for S and T level security.")
	else:
		os.chmod(file, octalPermission[perm])