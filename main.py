# This lab was pair programmed by Ryan and Day on 3/7/23

def encoder(password):
    encoded = ""
    for char in password:
        encoded += str(int(char) + 3)
    return encoded

def decoder(password):
    decoded = ""
    for char in password:
        decoded += str(int(char) - 3)
    return decoded

