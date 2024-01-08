import random
import string
def generatePass(leng):
    chars=string.ascii_letters+string.digits
    password="".join(random.choice(chars) for km in range(leng))
    return password


pass_len=int(input("Enter the length of the password you need to create: "))
rand_pass=generatePass(pass_len)
print()
print("The generated random password is :")
print()
print(rand_pass)