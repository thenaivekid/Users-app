from ctypes import sizeof


def is_valid_password(password):
    if len(password) >= 8:
        return password
    
    else:
        return None