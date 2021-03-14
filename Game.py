import numpy as np

#board = np.zeros((4,4))
board = np.array([[2, 4, 4, 0],[0,4,2,2],[0,4,0,4],[0,2,0,0]])
def new_tile():
    new_tile_value=np.random.choice(5, 1, p=[0, 0, 0.8, 0, 0.2])

    column = np.random.randint(0,4,1)
    row = np.random.randint(0,4,1)

    if board[row,column] == 0 :
        board[row,column]= new_tile_value
        flag=1
    else:
        new_tile()



def game_start():
    new_tile()
    new_tile()
    print(board)
    return (board)

def move_left(board):
   for k in range(4):
       a=board[k,:]
       for i in range(3):
           for j in range(3):
               if(a[j])==0:
                   a[j]=a[j+1]
                   a[j+1]=0

       for x in range(3):
           if(a[x]==a[x+1]):
                a[x]=a[x+1]*2
                a[x+1]=0

       for i in range(3):
            for j in range(3):
                if(a[j])==0:
                    a[j]=a[j+1]
                    a[j+1]=0
   new_tile()
   print(board)


def move_right(board):
    for k in range(4):
        a=board[k,:]
        for i in range(3):
            for j in range(3,0,-1):
                if(a[j])==0:
                    a[j]=a[j-1]
                    a[j-1]=0

        for x in range(3,0,-1):
            if(a[x]==a[x-1]):
                a[x]=a[x-1]*2
                a[x-1]=0

        for i in range(3):
            for j in range(3,0,-1):
                if(a[j])==0:
                    a[j]=a[j-1]
                    a[j-1]=0
    #new_tile()
    print(board)
    print("Hello")
    print("Hello2")
    print("Hello3")
    print("Hello4")


game_start()
#move_left(board)
move_right(board)