# Skrypt obliczający medianę

def median(l):
    n = len(l)
    sorted_l = sorted(l)
    midpoint = n // 2

    if n % 2 == 1:
        return sorted_l[midpoint]
    else:
        lo = midpoint - 1
        hi = midpoint
        return (sorted_l[lo] + sorted_l[hi]) / 2

if __name__ == "__main__":
    l = [1, 3, 5, 6, 7, 10]
    print(median(l))
