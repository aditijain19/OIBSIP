import string
import random
pass_demo = string.ascii_letters + string.digits + string.punctuation
len_of_pass = 10
password = ''.join(random.choices(pass_demo, k=len_of_pass))
print("Your password is:", password)