import random
import string

length=int(input("enter the length of password \n"))
"""Generate a random password of the given length."""
letters = string.ascii_letters
digits = string.digits
symbols = string.punctuation
password = ''.join(random.choice(letters + digits + symbols)for _ in range(length))
print(password)
