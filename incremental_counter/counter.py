# coding:utf-8 Copy Right Atelier Grenouille © 2018 -
#
import os

class Counter:
	def __init__(self, counter_file):
		self.counter_file     = counter_file
		self.counter_file_dir = os.path.dirname(counter_file)

		if not os.path.exists(self.counter_file):
			if not os.path.exists(self.counter_file_dir):
				os.makedirs(self.counter_file_dir)
			with open(self.counter_file, 'w') as f:
				f.write("0")
				f.close()

	def set(self, val):
		with open(self.counter_file, 'w') as f:
			f.write(str(val))
			f.close
			return val


	def current(self):
		with open(self.counter_file, 'r') as f:
			counter = int(f.read())
			f.close()
			return counter

	def inc(self):
		counter = self.current() + 1
		self.set(counter)
		return counter

	def dec(self):
		counter = self.current()
		if counter is 0:
			return 0
		else:
			self.set(counter - 1)
			return counter - 1

	def reset(self):
		self.set(0)
		return 0

