board = ["-","-","-","-",
         "-","-","-","-",
         "-","-","-","-",
         "-","-","-","-",]
def display_board():
    print(board[0],"|",board[1],"|",board[2],'|',board[3])
    print(board[4],"|",board[5],"|",board[6],'|',board[7])
    print(board[8],"|",board[9],"|",board[10],'|',board[11])
    print(board[12],"|",board[13],"|",board[14],'|',board[15])
display_board() #to display a 4*4 board

score = [0,0]

def play(): # takes an input from user and puts it into a slot
   
   letter = input("Please enter either 'S'or'O': ")
   while letter not in ["S","O","s","o"]:
        letter = input("Invalid input... Please enter either S or O: ")
   else: 
        slot = int(input("Please enter slot number: "))
   while slot > 16 or slot < 0:
      slot = int(input("Invalid input... Please enter slot number: "))
   while board[slot - 1] in ["S","O","s","o"]:
      slot = int(input("Invalid input... Please enter slot number: "))
   else:    
      board[slot - 1] = letter.upper()
      display_board()
   #-----------------------------------------------------------------------------------------------------------------------------------
   # "S" check
   if turn in [1,3,5,7,9,11,13,15] and slot in [1,2,5,6]: # "S" player 1       #group 1
      
      if board[slot-1:slot+2] == ['S','O','S']: #horizontal check
        score[0] += 1
        
      if board[slot-1] and board[slot+7] == "S" and board[slot+3] =='O': # vertical check.
        score[0] += 1
        
      if board[slot-1] and board[slot+9] == "S" and board[slot+4] == 'O': #diagonal check
        score[0] += 1
     
   
   elif turn in [1,3,5,7,9,11,13,15] and slot in [3,4,7,8]: #group 2
      
      if board[slot-1] and board[slot-3] == 'S' and board[slot-2]=='O':#horizontal check
          score[0] += 1
      
      if board[slot-1] and board[slot+7] == "S" and board[slot+3] =="O": #vertical check.
        score[0] += 1
      
      if board[slot-1] and board[slot+5] == 'S' and board[slot+2] =='O': #diagonal check
        score[0] += 1
      
     
   
   elif turn in [1,3,5,7,9,11,13,15] and slot in [9,10,13,14]:# group 3
      
      if board[slot-1:slot+2] == ['S','O','S']: #horizontal check
        score[0] += 1 
      
      if board[slot-1] and board[slot-9] == 'S'and board[slot-5] =="O": #vertical check
        score[0] += 1
      
      if board[slot-1] and board[slot-7] == "S" and board[slot-4] == "O":#diagonal check
        score[0] += 1
      
     
   elif turn in [1,3,5,7,9,11,13,15] and slot in [11,12,15,16]: #group 4
     
     if board[slot-1] and board[slot-3] == 'S' and board[slot-2]=='O':#horizontal check
        score[0] += 1
     
     if board[slot-1] and board[slot-9] == "S" and board[slot-5] == "O":#vertical check
        score[0] += 1
     
     if board[slot-1] and board[slot-11] == "S" and board[slot-6] == "O": # diagonal check
       score[0] += 1
     
  
   if turn in [2,4,6,8,10,12,14,16] and slot in [1,2,5,6]: # player 2  #group 1
      
      if board[slot-1:slot+2] == ['S','O','S']: #horizontal check
        score[1] += 1
        
      if board[slot-1] and board[slot+7] == "S" and board[slot+3] =='O': # vertical check.
        score[1] += 1
        
      if board[slot-1] and board[slot+9] == "S" and board[slot+4] == 'O': #diagonal check
        score[1] += 1
      
   
   elif turn in [2,4,6,8,10,12,14,16] and slot in [3,4,7,8]: #group 2
      
      if board[slot-1] and board[slot-3] == 'S' and board[slot-2]=='O':#horizontal check
          score[1] += 1
      
      if board[slot-1] and board[slot+7] == "S" and board[slot+3] =="O": #vertical check.
        score[1] += 1
      
      if board[slot-1] and board[slot+5] == 'S' and board[slot+2] =='O': #diagonal check
        score[1] += 1
      
     
   
   elif turn in [2,4,6,8,10,12,14,16] and slot in [9,10,13,14]: #group 3
      
      if board[slot-1:slot+2] == ['S','O','S']: #horizontal check
        score[1] += 1 
      
      if board[slot-1] and board[slot-9] == 'S'and board[slot-5] =="O": #vertical check
        score[1] += 1
      
      if board[slot-1] and board[slot-7] == "S" and board[slot-4] == "O":#diagonal check
        score[1] += 1
      
      
   elif turn in [2,4,6,8,10,12,14,16] and slot in [11,12,15,16]: #group 4
     
     if board[slot-1] and board[slot-3] == 'S' and board[slot-2]=='O':#horizontal check
        score[1] += 1
     
     if board[slot-1] and board[slot-9] == "S" and board[slot-5] == "O":#vertical check
        score[1] += 1
     
     if board[slot-1] and board[slot-11] == "S" and board[slot-6] == "O": #diagonal check
       score[1] += 1
     
#---------------------------------------------------------------------------------------------------------------------------------------
   if turn in [1,3,5,7,9,11,13,15] and slot in [2,3,14,15]: # checks if player one earned points playing "O".
      
      if board[slot-1] == 'O' and board[slot] and board[slot-2] =='S': # bottom and top case
        score[0] += 1
      
   
   elif [1,3,5,7,9,11,13,15] and slot in [5,9,8,12]: # side case
      if board[slot-1] == "O" and board[slot-5] and board[slot+3] == 'S':
        score[0] += 1
      
   
   elif [1,3,5,7,9,11,13,15] and slot in [6,7,10,11]: # middle case
     if board[slot-1] == 'O' and board[slot-2] and board[slot] == 'S': #horizontal check
       score[0] += 1
     
     if board[slot-1] == 'O' and board[slot+2] and board[slot-4] == 'S': # diagonal of slope y = -x check
       score[0] += 1
     
     if board[slot-1] == 'O' and board[slot-5] and board[slot+3] == 'S': # vertical check
       score[0] += 1
     
     if board[slot-1] == 'O' and board[slot-6] and board[slot+4] == 'S': #diagonal of slope y = x check
       score[0] += 1
     

   
   elif turn in [2,4,6,8,10,12,14,16] and slot in [2,3,14,15]: # checks if player two earned points playing "O".
      
       if board[slot-1] == 'O' and board[slot] and board[slot-2] =='S': # bottom and top case
          score[1] += 1
      
   
   elif [2,4,6,8,10,12,14,16] and slot in [5,9,8,12]: # side case
      if board[slot-1] == "O" and board[slot-5] and board[slot+3] == 'S':
         score[1] += 1
      
   
   elif [2,4,6,8,10,12,14,16] and slot in [6,7,10,11]: # middle case
     if board[slot-1] == 'O' and board[slot-2] and board[slot] == 'S': #horizontal check
        score[1] += 1
     
     elif board[slot-1] == 'O' and board[slot+2] and board[slot-4] == 'S': # diagonal of slope y = -x check
        score[1] += 1
     
     elif board[slot-1] == 'O' and board[slot-5] and board[slot+3] == 'S': # vertical check
        score[1] += 1
     
     elif board[slot-1] == 'O' and board[slot-6] and board[slot+4] == 'S': #diagonal of slope y = x check
        score[1] += 1
     
for turn in range(1,17): #make players take turns and tells them who's turn it is.
    if turn in[1,3,5,7,9,11,13,15]:
        print("its player one's turn" )
        play() 
        print(score)
       
    else:
        print("its player two's turn" )
        play()
        print(score)
        

