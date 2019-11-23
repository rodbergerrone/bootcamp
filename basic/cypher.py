a1, a2 = "abcdefghijklmnopqrstuvwxyz", "cdefghijklmnopqrstuvwxyzab"
cypher = str.maketrans(a1, a2)

message = """g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."""
print (message.translate(cypher))

# do innych messaage.replace(' ', '')