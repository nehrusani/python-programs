class visa:
    def __init__(self, name, number, expiry_date):
                self.name = name
                self.number = number
                self.expiry_date = expiry_date
            
    def checker(self):
        if self.number:
              return True
        
pio = visa()

