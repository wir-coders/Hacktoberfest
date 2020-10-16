class graph:
    def __init__(self,n):
        #self.vertices=int(input("Enter number of Vertices: "))
        self.vertices=n
        self.adj=[]
        for i in range(self.vertices):
            temp=[-1 for j in range(self.vertices)]
            self.adj.append(temp)
        print("The Nodes are Numbered as 0,1,2,3....{}".format(self.vertices))
    def add_edge(self,node1,node2,weight):
        #Vpair=list(map(int,input("Enter the Vertices: ").split()))
        #weight=int(input("Enter the Weight of the Edge. "))
        self.adj[node1][node2]=weight
        self.adj[node2][node1]=weight
    def print_edges(self):
        for i in range(self.vertices):
            for j in range(self.vertices):
                if self.adj[i][j]>=0:
                    print("({})---{}----({})".format(i,self.adj[i][j],j))
    def Dijkistra(self):
        self.source=0                                              #Source at each stage
        self.distance=[float('inf') for i in range(self.vertices)] #The Rows at each stage
        self.available=[True for i in range(self.vertices)]        #Is the node visited or not
        self.distance[0],self.available[0]=0,False                    #Initial Node values Entered
        self.nov=1                                                 #Count of Number of Nodes Visited
        self.curr_dist=0                                           #Current Smallest length
        self.path=[self.source]
        while(self.nov<self.vertices):
            vertice=self.adj[self.source]
            for i in range(len(vertice)):
                if(vertice[i]>0 and vertice[i]+self.curr_dist<self.distance[i]):
                    self.distance[i]=vertice[i]+self.curr_dist
            
            self.curr_dist=float('inf')
            for i in range(len(self.distance)):
                if(self.available[i]==True and self.distance[i]<self.curr_dist):
                    self.curr_dist=self.distance[i]
                    self.source=i
            self.available[self.source]=False
            self.nov+=1
            self.path.append(self.source)
        print("Shortest Distances from the Source Node(0) are :")
        for i in range(len(self.distance)):
            print("0----{}  => {}".format(i,self.distance[i]))
        print("The Path is :",end=" " )
        for i in self.path:
            print(i,end= " ")
        print("")




G=graph(8)
G.add_edge(0,1,8)#1
G.add_edge(0,2,2)#2
G.add_edge(0,3,5)#3
G.add_edge(1,3,2)#4
G.add_edge(1,5,13)#5
G.add_edge(2,3,2)#6
G.add_edge(2,4,5)#7
G.add_edge(3,4,1)#8
G.add_edge(3,5,6)#9
G.add_edge(3,6,3)#10
G.add_edge(4,6,1)#11
G.add_edge(5,6,2)#12
G.add_edge(5,7,3)#13
G.add_edge(6,7,6)#14
G.Dijkistra()
print("All OK")