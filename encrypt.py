import os, subprocess, shutil

def combine_docs(directory):
	return shutil.make_archive(directory, format="zip", base_dir=directory)

def set_directory(path):
	workingDir, file = os.path.split(os.path.abspath(path))
	os.chdir(workingDir)
	return file

def encrypt(path, user):
	file = set_directory(path)

	zipFile = combine_docs(file)
	shutil.rmtree(file)

	cmd = f"gpg --output .{file}.gpg --user {user} --encrypt {zipFile}"
	subprocess.run(cmd.split(' '))
	os.remove(zipFile)

def decrypt(path, user):
	file = set_directory(path)

	cmd = f"gpg --output {file}.zip --user {user} --decrypt .{file}.gpg"
	subprocess.run(cmd.split(' '))
	os.remove(f".{file}.gpg")
	shutil.unpack_archive(f"{file}.zip", format="zip")
	os.remove(f"{file}.zip")