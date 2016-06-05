import threading
import os
import time
import random

class Queue():

	def __init__(self, buf_size):
		self.sem_lock = threading.Semaphore(buf_size)
		self.buffer = []

	def put(self, data):
		with self.sem_lock:
			self.buffer.append(data)

	def get(self):
		

BUFFER_SIZE = 10
queue = Queue(BUFFER_SIZE)

class Consumer(threading.Thread):

	def stop(self):
		self.exit = True

	def __init__(self, queue, t_id, lock_mut):
		threading.Thread.__init__(self)
		self.exit = False
		self.queue = queue
		self.t_id = t_id
		self.lock_mut = lock_mut

	def run(self):
		while not self.exit:
			# if not self.queue.empty():
			st, j_id = self.queue.get()
			with self.lock_mut:
				print 'consumer recived task->', j_id, 'executed by thread->', self.t_id
			time.sleep(st)
			with self.lock_mut:
				print 'consumer performed task->', j_id, 'it took', st, 'completed by->', self.t_id
			self.queue.task_done()
		with lock_mut:
			print 'stoped thread->', self.t_id

if __name__ == '__main__':
	lock_mut = threading.Lock()
	# create 10 consumer thread
	cons_thread_list = []
	for t_id in xrange(10):
		t = Consumer(queue, t_id, lock_mut)
		cons_thread_list.append(t)
		t.start()

	# create jobs, this is "Producer"
	for j_id in xrange(100):
		queue.put((random.randint(5, 10), j_id))

	# send stop message to all thread once producer has done the job.
	for t in cons_thread_list:
		t.stop()

	for t in cons_thread_list:
		t.join()
	print "Exiting Main Thread"
