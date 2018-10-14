import fileinput

class DAG(object):

	def __init__(self, edges, size):
		self.size = size
		self.graph = [None]
		for i in range(1,size+1):
			self.graph.insert(i,set())

	def spath(self):
		distance = (self.size+1) * [float('inf')] 
		distance[1] = 0
		for v in range(1,self.size):
			for u in self.graph[v]:
				if u == None:
					break
				if distance[u] > (distance[v] + 1):
					distance[u] = distance[v] + 1
		return distance[self.size]

	def lpath(self):
		distance = [-1] * (self.size+1)
		distance[1] = 0
		for v in range(1,self.size):
			for u in self.graph[v]:
				if u == None:
					break
				if distance[u] < (distance[v] + 1):
					distance[u] = distance[v] + 1
		return distance[self.size]


	def numPaths(self):
		pcount = 0
		paths = [0] * (self.size+1)
		paths[1] = 1
		for v in range(1,self.size):
			for u in self.graph[v]:
				paths[u] += paths[v]
		pcount = paths[self.size]
		return pcount


	def addEdge(self, x, y):
		self.graph[x].add(y)


	def DAGsummary(self, number):
		print("graph number: "+str(number))
		print("shortest path: "+str(self.spath()))
		print("longest path: "+str(self.lpath()))
		print("number of paths: "+str(self.numPaths()))


def main():
	with fileinput.input() as f:
		numDAGs = int(f.readline().rstrip('\n'))

		for x in range(numDAGs):
			DAGsize = int(f.readline().rstrip('\n'))
			DAGedges = int(f.readline().rstrip('\n'))
			graph = DAG(DAGedges, DAGsize)

			for y in range(DAGedges):
				e = f.readline()
				u,v = [int(i) for i in e.split()]
				graph.addEdge(u,v)
			graph.DAGsummary(x+1)
			print("\n")


	fileinput.close()

if __name__ == '__main__':
	main()
