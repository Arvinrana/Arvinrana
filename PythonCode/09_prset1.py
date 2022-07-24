from socketserver import DatagramRequestHandler


f = open('peoms.txt')
t = f.read()
if 'twinkle' in t:
    print("Twinkle is present in peoms")
else:
    print("Twinkle is not present")    
f.close()
