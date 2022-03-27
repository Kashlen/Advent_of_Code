import hashlib, datetime

# 1st part
start = datetime.datetime.now()

s_key = "bgvyzdsv"

def hash_number(key):
    key_in_MD5 = hashlib.md5(key.encode())
    hexadecimal_hash = key_in_MD5.hexdigest()
    return hexadecimal_hash

def find_5_zeros(key):
    for x in range(10000000):
        secret_key = key + str(x)
        if '00000'in hash_number(secret_key)[0:5]:
            print(x)
            break


find_5_zeros(s_key)

print("Runtime: {0}".format(datetime.datetime.now()-start))