import random
import string

length = int(input("Enter the length of password: "))

lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits
symbols = string.punctuation

gen = lower+upper+num+symbols

temp = random.sample(gen,length)
password = "".join(temp)
print(password)