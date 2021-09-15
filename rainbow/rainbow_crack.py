from multiprocessing import Process

_hash = '71f5c57eade7cc34c105ab158298e75be2f835b1'
PARTS = 10 

def find(i):
	fname = 'hash_'+str(i)+'.csv'
	f = open(fname, 'r')
	while True:
		line = f.readline().strip()
		if not line:
			break
			
		data = line.split(',')
		if data[1] == _hash:
			print(data[0])
			break
	f.close()

if __name__ == '__main__':
	procs = []

	for i in range(PARTS):
		proc = Process(target=find, args=(i,))
		procs.append(proc)
		proc.start()

	for proc in procs:
		proc.join()