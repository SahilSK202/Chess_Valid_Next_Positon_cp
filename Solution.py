

def validPos(piece , currentpos , nextpos):
    letters = ['a','b','c','d','e','f','g','h']
    
    currLetIndex = letters.index(currentpos[0])
    nextLetindex = letters.index(nextpos[0])
    currNumIndex = int(currentpos[1])
    nextNumindex = int(nextpos[1])
    
    if(piece == "Bishop"):
        if(abs(currLetIndex - nextLetindex) == abs(currNumIndex - nextNumindex)):
            return True
        else:
            return False
            
    elif(piece == "Knight"):
        if(abs(currLetIndex - nextLetindex) == 2):
            if(abs(currNumIndex - nextNumindex) == 1):
                return True
            else:
                return False
        elif(abs(currLetIndex - nextLetindex) == 1):
            if(abs(currNumIndex - nextNumindex) == 2):
                return True
            else:
                return False
        else:
            return False
    else:
        return False
        
               
        
        
