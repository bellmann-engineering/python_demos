# Working with Lists and Indexing
my_list = [1, 2, 3, 4, 5]

# Accessing elements by index using a for loop
for element in my_list:
    print(element)

# Strings and Immutability
my_string = "Hello, World!"

# Iterating over characters in a string using a for loop
for char in my_string:
    print(char)

# Countdown using a while loop
count = 10
while count > 0:
    print(count)
    count -= 1

# String Slicing and Manipulation
my_string = "Python is versatile and fun!"

# Slicing to get every other character
substring = my_string[::2]

# Printing the sliced string
for char in substring:
    print(char)

# Min, Max, and Mean
numbers = [5, 8, 3, 12, 9]

min(numbers)
max(numbers)

import statistics  # Import the statistics module
# Calculating the mean using statistics.mean
mean = statistics.mean(numbers)

# Function for avg
def avg(numbers : list) -> float:
    return sum(numbers) / len(numbers)

avg(numbers)

# Functions and Type Hints
def add(a: int, b: int) -> int:
    """Add two integers and return the result."""
    return a + b

# call the function
result = add(3, 4)  # 7

# Sorting Lists
my_list = [4, 1, 3, 2, 5]

# Using sort() to sort the list in-place
my_list.sort()  # my_list is now [1, 2, 3, 4, 5]

# Using sorted() to create a new sorted list
sorted_list = sorted(my_list)  # sorted_list is [1, 2, 3, 4, 5]

# Sorting in reverse order
my_list.sort(reverse=True)  # my_list is now [5, 4, 3, 2, 1]

def search(n: int, numbers: list):
    if n in numbers:
        return numbers.index(n)
    else:
        print("not found")

# Tuples are immutable ordered collections in Python that can hold a sequence of elements of different data types.
# Stock information as a tuple
stock = ("AAPL", "Apple Inc.", 150.0)

# Access and print stock information
stock_symbol, company_name, stock_price = stock
print(stock_price)

# List of stock information as tuples
stocks = [
    ("AAPL", "Apple Inc.", 150.0),
    ("GOOGL", "Alphabet Inc.", 2700.0),
    ("MSFT", "Microsoft Corporation", 300.0),
    ("AMZN", "Amazon.com Inc.", 3400.0)
]

# Access and print the list of stock information
for symbol, name, price in stocks:
    print(f"Stock Symbol: {symbol}, Company Name: {name}, Current Price: ${price:.2f}")

# Dictionary with WKN as keys for stock information
stocks = {
    "AAPL": ("Apple Inc.", 150.0),
    "GOOGL": ("Alphabet Inc.", 2700.0),
    "MSFT": ("Microsoft Corporation", 300.0),
    "AMZN": ("Amazon.com Inc.", 3400.0)
}

# Access and print stock information using WKN as the key
wkn = "AAPL"
if wkn in stocks:
    name, price = stocks[wkn]
    print(f"Stock with WKN {wkn}: Company Name: {name}, Current Price: ${price:.2f}")
else:
    print(f"Stock with WKN {wkn} not found.")

