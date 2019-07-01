from pack.PohamHandle import PohamHandle

class PohamCar:
    turnShow = "정지"
    
    def __init__(self, ownerName):
        self.ownerName = ownerName
        self.handle = PohamHandle() #클래스의 포함관계
        
    def TurnHandle(self, q):
        if q > 0:
            self.turnShow = self.handle.rightTurn(q)    
        elif q < 0:
            self.turnShow = self.handle.leftTurn(q)      
        elif q == 0:
            self.turnShow = "직진" 
