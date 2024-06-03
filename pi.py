import numpy as np
from decimal import Decimal, getcontext

def calculate_pi_to_n_decimals(n):
    # Set the precision for decimal calculations
    getcontext().prec = n + 2  # precision needs to be n+2 for correct rounding
    
    # Using Chudnovsky algorithm for Pi: an efficient algorithm for large precision
    C = 426880 * Decimal(10005).sqrt()
    M = 1
    L = 13591409
    X = 1
    K = 6
    S = L

    for i in range(1, n):
        M = (K**3 - 16*K) * M // i**3
        L += 545140134
        X *= -262537412640768000
        S += Decimal(M * L) / X
        K += 12

    pi = C / S
    
    # Return Pi to the specified number of decimal places
    return +pi  # unary plus applies the precision

def print_pi_to_n_decimals(n):
    pi = calculate_pi_to_n_decimals(n)
    print(f"Pi to {n+1} decimas: {pi}")

# Read the numeric value n from the user
while True:
    try:
        n = int(input("Enter the number of decimal places for Pi (min 1 decimal): "))
        if int(n) >= 1:
            break
    except:
        pass

# Call the function to print Pi to n decimal places
print_pi_to_n_decimals(n-1)
print("pi is in np.pi:  ", np.pi)
