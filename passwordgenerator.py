import random
import string

def generate():
    part = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(6))
    return part

n = int(input("Level of security: "))

password = '-'.join(generate() for _ in range(n))

print('Your new password is: ' + password)