def safe_sqrt(num):
    if num < 0:
        print("square root of a negatiive numbers is not a real number .")
        return None
    else:
        sqrt_val = num**0.5
        return sqrt_val
print("square root of 30:", safe_sqrt(30))
print("square root of -9:", safe_sqrt(-9))