class PohamHandle:
    quantity = 0
    
    def leftTurn(self, quantity):
        self.quantity = quantity
        return "좌회전"
    
    def rightTurn(self, quantity):
        self.quantity = quantity
        return "우회전"