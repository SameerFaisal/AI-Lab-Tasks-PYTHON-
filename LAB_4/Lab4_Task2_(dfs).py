graph={'A':['D','B'],
     'B':['E','C'],
     'C':[],
     'D':['G','H','E'],
     'E':['F','C'],
     'F':[],
     'G':['H']}

visited=set()
stack=[]
def dfs(visited,graph,node):
    if stack not in stack:
        print(node,end=" ")
        if(node=='G'):
            print("\nGoal Found") 
            return
        stack.append(node)
        for neighbours in graph[node]:
            dfs(stack,graph,neighbours)
            return
dfs(stack,graph,'A')
