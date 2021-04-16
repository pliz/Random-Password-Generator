# deleting while True may result in an error
while True: 
    import random 
    passlen = int(input("enter desired password length  "))
    s="abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
    p = "".join(random.sample(s,passlen ))
    print(p)
# deleting True will result in execution failiure
True 

