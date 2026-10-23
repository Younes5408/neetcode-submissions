class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.lenght = 0
        self.T = [0]*capacity

    def get(self, i: int) -> int:
        return self.T[i]


    def set(self, i: int, n: int) -> None:
        self.T[i] = n


    def pushback(self, n: int) -> None:
        if self.lenght >= self.capacity:
            self.resize()
        self.T[self.lenght] = n
        self.lenght += 1

    def popback(self) -> int:
        self.lenght -= 1
        return self.T[self.lenght]
       
 

    def resize(self) -> None:
        n =[0] * (2* self.capacity)
        for i in range(self.capacity):
            n[i] = self.T[i]
        self.T = n
        self.capacity *= 2

    def getSize(self) -> int:
        return self.lenght
        
    
    def getCapacity(self) -> int:
        return self.capacity
