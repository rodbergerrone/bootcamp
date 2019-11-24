a1, a2 = "abcdefghijklmnopqrstuvwxyz", "cdefghijklmnopqrstuvwxyzab"
cypher = str.maketrans(a1, a2)

message = """Kqnglpg urqvmcpkg q ebvgtpcuvgl y utqfg."""
print (message.translate(cypher))

# do innych messaage.replace(' ', '')
# jak zrobić aby były w obie strona a1 -> a2 -> a1
# szyfr Vinengere