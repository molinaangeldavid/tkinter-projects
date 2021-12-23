import random

class Generatepass():
    
    def __init__(self):
        
        self.alfabeth = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        self.number = ['1','2','3','4','5','6','7','8','9']
        self.character = ['!','#','@','$','%','&','-','+','*','(',')']
    
    def generate_pass(self):    
        password = ''
        count = 0
        for i in range(15):
            count += 1
            if count >= 0 and count < 9:
                letter = random.choice(self.alfabeth)
                password += letter
            elif count > 8 and count < 12:
                number = random.choice(self.number)   
                password += number
            else:
                character = random.choice(self.character)
                password += character
        password = list(password)            
        random.shuffle(password)
        p = "".join(password)
        return p
    
        
        
        
        
        
        
        