from mpmath import mp
from colorama import Fore, Style

# Set the frame
y = 25

# Line breaker
x = 68

# Set the desired precision (number of decimal places)
precision = y * x

# Set the value of PI with the desired precision
mp.dps = precision
pi_value = str(mp.pi)

def generate_range(base, start, end):
    """
    Generate a range based on starting and ending positions.
    
    Args:
        base (int): Base value for the range.
        start (int): Starting position.
        end (int): Ending position.
        
    Returns:
        range: A range of values from 'base + start' to 'base + end + 1'.
    """
    return range(base + start, base + end + 1)
    
# Define the red and blue ranges
red_ranges = [
        generate_range(x * 0, 0, 3),
        generate_range(x * 2, 11, 55),
        generate_range(x * 3, 8, 55),
        generate_range(x * 4, 6, 55),
        generate_range(x * 5, 4, 55),
        generate_range(x * 6, 3, 6), generate_range(x * 6, 16, 21), generate_range(x * 6, 37, 42),
        generate_range(x * 7, 2, 4), generate_range(x * 7, 16, 21), generate_range(x * 7, 37, 42),
        generate_range(x * 8, 2, 3), generate_range(x * 8, 15, 20), generate_range(x * 8, 36, 41),
        generate_range(x * 9, 2, 2), generate_range(x * 9, 14, 19), generate_range(x * 9, 35, 40),
        generate_range(x * 10, 14, 19), generate_range(x * 10, 35, 40),
        generate_range(x * 11, 14, 19), generate_range(x * 11, 35, 40),
        generate_range(x * 12, 14, 19), generate_range(x * 12, 35, 40),
        generate_range(x * 13, 13, 18), generate_range(x * 13, 35, 40),
        generate_range(x * 14, 13, 18), generate_range(x * 14, 35, 40),
        generate_range(x * 15, 13, 18), generate_range(x * 15, 35, 40),
        generate_range(x * 16, 12, 18), generate_range(x * 16, 35, 40),
        generate_range(x * 17, 11, 17), generate_range(x * 17, 35, 40), generate_range(x * 17, 53, 53),
        generate_range(x * 18, 10, 17), generate_range(x * 18, 35, 41), generate_range(x * 18, 52, 53),
        generate_range(x * 19, 8, 16), generate_range(x * 19, 35, 42), generate_range(x * 19, 50, 53),
        generate_range(x * 20, 6, 16), generate_range(x * 20, 35, 52),
        generate_range(x * 21, 6, 15), generate_range(x * 21, 36, 51),
        generate_range(x * 22, 6, 15), generate_range(x * 22, 38, 49),
        generate_range(x * 23, 8, 13), generate_range(x * 23, 41, 47),
    ]

blue_ranges = [
        generate_range(x * 2, 58, 65),
        generate_range(x * 3, 61, 62),
        generate_range(x * 4, 61, 62),
        generate_range(x * 5, 61, 62),
        generate_range(x * 7, 58, 59), generate_range(x * 7, 64, 65),
        generate_range(x * 8, 58, 59), generate_range(x * 8, 64, 65),
        generate_range(x * 9, 58, 65),
        generate_range(x * 10, 58, 59), generate_range(x * 10, 64, 65),
        generate_range(x * 11, 58, 59), generate_range(x * 11, 64, 65),
        generate_range(x * 13, 60, 63),
        generate_range(x * 14, 58, 59), generate_range(x * 14, 64, 65),
        generate_range(x * 15, 58, 59), generate_range(x * 15, 64, 65),
        generate_range(x * 16, 58, 59), generate_range(x * 16, 64, 65),
        generate_range(x * 17, 60, 63),
        generate_range(x * 19, 58, 60), generate_range(x * 19, 64, 65),
        generate_range(x * 20, 58, 59), generate_range(x * 20, 61, 62), generate_range(x * 20, 64, 65),
        generate_range(x * 21, 58, 59), generate_range(x * 21, 62, 63), generate_range(x * 21, 64, 65),
        generate_range(x * 22, 58, 59), generate_range(x * 22, 63, 64), generate_range(x * 22, 64, 65),
    ]

# Print the PI number with 'x * y' decimals
for i, char in enumerate(pi_value):
    if any(i in rng for rng in red_ranges):
        print(f"{Fore.RED}{char}{Style.RESET_ALL}", end="")
    elif any(i in rng for rng in blue_ranges):
        print(f"{Fore.BLUE}{char}{Style.RESET_ALL}", end="")
    else:
        print(char, end="")

    if (i + 1) % x == 0:
        print(' ')

