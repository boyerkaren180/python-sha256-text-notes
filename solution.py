import hashlib

def solve(value):
    return hashlib.sha256(value.encode('utf-8')).hexdigest()
