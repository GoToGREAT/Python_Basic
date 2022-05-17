class User:
    def __init__(self, usernum, uid, phone, email):
        self.usernum = usernum
        self.uid = uid
        self.phone = phone
        self.email = email
        
    def __str__(self):
        return f"{self.usernum}\t{self.uid}\t{self.phone}\t{self.email}"
    
    def __eq__(self, other):
        return self.usernum == other.usernum
    
    def edit(self, phone, email):
        self.phone = phone
        self.email = email  