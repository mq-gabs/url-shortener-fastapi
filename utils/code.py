import random

chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

def gen_code(L = 6):
    code = ""
    for _ in range(L):
        code += chars[random.randint(0,len(chars)-1)]
    return code