import hashlib

def md5(text, salt = ''):
    md5coder = hashlib.md5()
    md5coder.update((text + salt).encode('utf-8'))
    return md5coder.hexdigest()