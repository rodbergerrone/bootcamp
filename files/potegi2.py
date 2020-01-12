with open('potegi2.txt', 'w') as f:
    for i in range(100):
        f.write(f"{2 ** i}\n")