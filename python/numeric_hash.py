


import hashlib
value = 'something to hash'
t_value = value.encode('utf8')
h = hashlib.sha256(t_value)
h.hexdigest()
n = int(h.hexdigest(),base=16)
print(n)