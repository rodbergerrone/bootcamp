def kwadrat(x):
    return x ** 2

print(kwadrat(5))

print()

# z zastosowaniem lambdy
# kwadrat = lambda x: x ** 2
print((lambda x: x ** 2)(5))
print(sorted(["pies", "kot", "żółw", "papuga"], key=lambda x: x[-1]))