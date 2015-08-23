import networkx as nx
import matplotlib.pyplot as plt

def validmove(j,i,x,y):
	if(j>=0 and i>=0 and j<x and i<y):
		return True
	return False

def colors(G,edgeList=[]):
    colors = []
    for node1,node2,_ in G.edges_iter(data=True):
        colors.append('red' if (node1,node2) in edgeList else 'blue')
    return colors

G=nx.Graph()
temp=map(int,raw_input().split())
x=temp[1]
y=temp[0]
source=input()#(temp[0],temp[1])
sourceNode=source #temp[0]*x+temp[1]
destination=input()#(temp[0],temp[1])
destinationNode=destination #temp[0]*x+temp[1]
direction=[(-1,-1),(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1)]
for i in xrange(y):
	for j in xrange(x):
		node1=i*x+j
		for y1,x1 in direction:
			if validmove(j+x1,i+y1,x,y):
				node2=(i+y1)*x+(j+x1)
				G.add_edge(node1,node2)

l=nx.shortest_path(G,source=sourceNode,target=destinationNode)
edgeList=[]
for i in xrange(len(l)-1):
	edgeList.append((l[i],l[i+1]))
nx.draw(G,edge_color=colors(G,edgeList=edgeList),width=2)
plt.show()