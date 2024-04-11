"""
	Simple Version Bump tool

	Version 0.0.0.0
			| | | |
	  Major_| | | |
	  Minor___| | |
	  Micro_____| |
	  Patch_______|

"""
import os, sys

class SimpleVersionBumper:

	def __init__(self, version_fn):
		self.version_fn = version_fn
		try:
			fh = open(self.version_fn, "r")
			version = fh.read()
			fh.close()
			v = version.split('.')
			self.major = int(v[0])
			self.minor = int(v[1])
			self.micro = int(v[2]) 
			self.patch = int(v[3])
		except FileNotFoundError:
			self.major = 0
			self.minor = 0
			self.micro = 0
			self.patch = 0
		
	def current_version(self):
		return "%s.%s.%s.%s" % (
			self.major,
			self.minor,
			self.micro,
			self.patch
			)

	def save(self):
		fh = open(self.version_fn, "w")
		fh.write("%s.%s.%s.%s" % (
			self.major,
			self.minor,
			self.micro,
			self.patch			
		))
		fh.close()

	def bump(self, part_id):
		match part_id:
			case 1:
				self.major += 1
			case 2:
				self.minor += 1
			case 3:
				self.micro += 1
			case 4:
				self.patch += 1
		self.save()
		self.add_git_tag()

	def add_git_tag(self):
		os.system("git tag %s" % self.current_version())
		

if __name__ == '__main__':
	
	bumper = SimpleVersionBumper("version.txt")
	print("Current version: %s" % bumper.current_version())
	
	if len(sys.argv) != 2:
		print("Which part of the version you want to bump?")
		print("\t1 = Major (x.?.?.?)")
		print("\t2 = Minor (?.x.?.?)")
		print("\t3 = Micro (?.?.x.?)")
		print("\t4 = Patch (?.?.?.x)")
		value = int(input(">"))
	else:
		value = int(sys.argv[1])
	if value in range(1,5):
		bumper.bump(value)
		print("Bumped version:  %s" % bumper.current_version())
