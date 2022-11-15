import os

msgs = [ "One time pad is really a completely unbreakable cryptosystem",
         "Encrypt and decrypt functions are each just an XOR operation",
         "Key needs to be random bitstring with same length as message",
         "A many time pad is very insecure and can be broken with ease",
         "If you can decipher this you can see just how insecure it is" ]

# msgs = [" of spades ur squares", "ninety nin forget itt", "kanye west i am robot", "banananty  pantaloo i", "his forear four score"]

def encrypt(pad, msg):
    return bytes([x ^ ord(y) for (x, y) in zip(pad, msg)]).hex()

pad = os.urandom(60)
print(type(pad))
ctxts = [encrypt(pad, m) for m in msgs]
print('\n'.join(ctxts))
