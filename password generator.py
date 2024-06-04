#Password Generator
import random
password = int(input("Enter the Length of the Password : "))
generator="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()[]{}><?"
output="".join(random.sample(generator,password))
print("Result :",output)
