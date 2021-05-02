graph={'A':['D','B'],
     'B':['E','C'],
     'C':[],
     'D':['G','H','E'],
     'E':['F','C'],
     'F':[],
     'G':['H']}
visited=[]
queue=[]
def bfs(visited,graph,node):
    visited.append(node)
    queue.append(node)
    while queue:
        element=queue.pop(0)
        print(element,end=" ")
        if(element=='G'):
            print("\nGoal Node Found")
            return
        for neighbours in graph [element]:
            if neighbours not in visited:
                visited.append(neighbours)
                queue.append(neighbours)
bfs(visited,graph,'A')
