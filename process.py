from flask import Response
import subprocess
import os

class ProcessWrapper(object):
	def __init__(self, process, buffer_size=8192):
		self.process = process
		self.buffer_size = buffer_size
	def close(self):
		if self.process.returncode is not None:
			return
		self.process.stdout.close()
		self.process.terminate()
		self.process.wait()
	def __iter__(self):
		return self
	def __del__(self):
		self.close()
	def next(self):
		try:
			data = self.process.stdout.read(self.buffer_size)
		except:
			self.close()
			raise StopIteration()
		if data:
			return data
		self.close()
		raise StopIteration()

def send_process(args):
	def close_fds():
		os.close(0)
		os.close(2)
	process = subprocess.Popen(args, close_fds=True, stdout=subprocess.PIPE, preexec_fn=close_fds)
	response = ProcessWrapper(process)
	return Response(response, direct_passthrough=True)
