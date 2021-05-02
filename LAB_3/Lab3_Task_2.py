original_room = [[0,0,0],[0,0,0],[0,0,0]]
print("Original status of the rooms:",original_room)
dirty_room = [[0,1,0],[1,1,0],[0,1,1]]
print("Rooms after placing dirt(1) randomly:",dirty_room)
for i in range(0,3):
    print("Room #",i+1)
    for j in range(0,3):
        if dirty_room[i][j]==0:
            print("Tile %d already Clean"%(j+1))
        else:
            dirty_room[i][j]=0
            print("Tile %d Now Cleaned 0"%(j+1))
print("New status of room after cleaning:",dirty_room)