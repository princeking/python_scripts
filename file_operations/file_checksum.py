import hashlib
m = hashlib.md5()
with open("large.txt", 'rb') as f:
        for chunk in iter(f.read(1024)):
            m.update(chunk)
print(m.hexdigest())