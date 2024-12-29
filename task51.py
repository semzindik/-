def password_strength(password):
    score = 0
   
    if len(password) >= 8:
        score += 1
    
    if any(char.isupper() for char in password):
        score += 1
   
    if any(char.islower() for char in password):
        score += 1
    
    if any(char.isdigit() for char in password):
        score += 1
    
    
    special_characters = "!@#$%^&*()-_=+[]{}|;:'\",.<>?/"
    if any(char in special_characters for char in password):
        score += 1
    
    return score
print(password_strength("Password123!"))  
print(password_strength("pass"))          
print(password_strength("Password"))      
print(password_strength("12345678"))       
print(password_strength("P@ssw0rd"))       