class Emp:
    def __init__(self, num, name=None, phone=None): #self=java의 this
        self.num = num
        self.name = name
        self.phone = phone
        
    def __str__(self): #자바의 tostring
        return f"{self.num}\t{self.name}\t{self.phone}"
    
    def __eq__(self, other):
        return self.num == other.num
    
    def edit(self, name, phone):
        self.name = name
        self.phone = phone