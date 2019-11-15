alpha1 = "abcdefghijklmnopqrstuvwxyz"
alpha2 = "cdefghijklmnopqrstuvwxyzab"
trantab = str.maketrans(alpha1, alpha2)

message = """http://www.pythonchallenge.com/pc/def/map.html"""
print (message.translate(trantab))
