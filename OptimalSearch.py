graph={'s':[[],-1],'g'=[[],0]}
extensionlist=[]
pathqueue=[['s',0,-1]]

def inputnode():
	print('Enter all the node present in the graph apart from the starting node s and the Goal node g : ')
	nodes=input().split()
	for node in nodes:
		graph[node]=[[],-1]
		
def inputnodebranch():
	print('Enter all the node and the corresponding distance from the current node...')
	for node in graph.keys():
		print('Enter the number of nodes connected to node '+node+' : ')
		n=int(input())
		print('Enter the nodes and the corressponding distance : ')
		for i in range(n):
			innode,distance=input().split()
			distance=int(distance)
			graph[node][0].append((innode,distance))

def inputgoaldistance():
	for node in graph.keys():
		print('Enter the distance from the the goal for the node '+node)
		goaldistance=int(input())
		graph[node][1]=goaldistance
		if node=='s': pathqueue[0][2]=goaldistance
		
def graphinput():
	inputnode()
	inputnodebranch()
	inputgoaldistance()

def findpath():
	shortestpath=pathqueue[0]
	index=0
	for i in range(1,len(pathqueue)):
		if pathqueue[i][1]+pathqueue[i][2]<=shortestpath[1]+shortestpath[2]:
			shortestpth=pathqueue[i]
			index=i
	return index
	
def search():
	while len(pathqueue)!=0:
		index=findpath()
		detailedpath=pathqueue.pop(index)
		path=detailedpath[0]
		if path[len(path)-1]=='g': return path
		distancecovered=detailedpath[1]
		distanceleft=detailedpath[2]
		currentnode=path[len(path)-1]
		try:
			index=extensionlist.index(currentnode)
			continue
		except:
			extensionlist.append(currentnode)
			for (nextnode,distance) in graph[currentnode][0]:
				temppath=path+nextnode
				tempdistancecovered=distancecovered+distance
				tempdistanceleft=graph[nextnode][1]
				pathqueue.append([temppath,tempdistancecovered,tempdistanceleft])

print('The nodes is represented as letters. The starting node is represented as s and the goal node in represented as g')
graphinput()
path=search()
print('The optimal path from the start to the goal is : ')
path=list(path)
for i in range(len(path)):
	if i==len(path)-1: print(path[1])
	else: print(path[i]+' -> ', end=' ')