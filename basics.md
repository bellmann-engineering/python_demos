# Python 3 Basics

Here we learn the fundamental concepts in Python 3, including variables, data types, basic operations, conditions, and loops.

## Variables

Variables are containers used to store data values. They're created by assigning a value to a name. Variable names must start with a letter or underscore and can contain letters, numbers, and underscores. [Learn more](https://docs.python.org/3/tutorial/introduction.html#variables)

Variable assignment example:
```python
variable_name = 42
```

## Data Types

Python supports various data types to represent different kinds of information.

### Integers (int)

Integers are used to represent whole numbers. [Learn more](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)

Example:
```python
my_integer = 42
```

### Floats (float)

Floats are used to represent numbers with decimal points. [Learn more](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)

Example:
```python
my_float = 3.14
```

### Strings (str)

Strings are used to represent text. [Learn more](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)

Example:
```python
my_string = "Hello, World"
```

### Lists

Lists are ordered collections of items. [Learn more](https://docs.python.org/3/library/stdtypes.html#sequence-types-list-tuple-range)

Example:
```python
my_list = [1, 2, 3]
```
Working with lists:

```python
my_list = [1, 2, 3, 4, 5]

# Check if a value is in the list
if 3 in my_list:
    print("3 is in the list")

# Sort the list
my_list.sort()
print(my_list)
```

### Tuples

Tuples are ordered, immutable collections of items. [Learn more](https://docs.python.org/3/library/stdtypes.html#sequence-types-list-tuple-range)

Example:
```python
my_tuple = (4, 5, 6)
```

### Dictionaries (dict)

Dictionaries store key-value pairs, allowing you to associate values with unique keys. [Learn more](https://docs.python.org/3/library/stdtypes.html#mapping-types-dict)

Example:
```python
my_dict = {"name": "Alice", "age": 30}
```

### Booleans (bool)

Booleans represent logical values, True or False. [Learn more](https://docs.python.org/3/library/stdtypes.html#truth-value-testing)

Example:
```python
my_bool = True
```

## Basic Operations

Python supports various basic operations for performing arithmetic and mathematical calculations.

### Arithmetic Operations

Python provides standard arithmetic operations. [Learn more](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)

Example:
- Addition: `result = 5 + 3`
- Subtraction: `result = 7 - 2`
- Multiplication: `result = 4 * 6`
- Division: `result = 8 / 2`
- Modulus (remainder): `result = 10 % 3`
- Exponentiation: `result = 2 ** 4`

### Using the math Library

The math library in Python provides more advanced mathematical functions. [Learn more](https://docs.python.org/3/library/math.html)

Example:
`import math`
- Square root: `result = math.sqrt(16)`
- Sine function (requires radians): `result = math.sin(math.radians(30))`
- Natural logarithm: `result = math.log(100)`


## Conditions

Conditional statements are used to make decisions based on certain conditions. [Learn more](https://docs.python.org/3/tutorial/controlflow.html#if-statements)

Example:
```python
x = 10
if x > 5:
    print("x is greater than 5")
elif x == 5:
    print("x is equal to 5")
else:
    print("x is less than 5")
```

## Loops

Loops are used for repetitive tasks in Python. [Learn more](https://docs.python.org/3/tutorial/introduction.html#first-steps-towards-programming)

### While Loop

The while loop repeatedly executes a block of code as long as a condition is true. [Learn more](https://docs.python.org/3/reference/compound_stmts.html#the-while-statement)

Example:
```python
count = 0
while count < 5:
    print(count)
    count += 1
```
### For Loop

The for loop is used to iterate over a sequence, such as a list or a range of numbers. [Learn more](https://docs.python.org/3/reference/compound_stmts.html#the-for-statement)

Example:
```python
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
```

Additionally, you can use the range function to create a sequence of numbers and iterate over it. [Learn more](https://docs.python.org/3/library/stdtypes.html#range)

Example:
```python
for i in range(5):
    print(i)
```
### Break and Continue

Python provides two control statements within loops:

- break is used to exit a loop prematurely. [Learn more](https://docs.python.org/3/reference/simple_stmts.html#the-break-statement)
- continue is used to skip the current iteration and continue to the next. [Learn more](https://docs.python.org/3/reference/simple_stmts.html#the-continue-statement)

Example:
```python
for i in range(10):
    if i == 3:
        break  # Exit the loop when i is 3
    if i == 7:
        continue  # Skip iteration when i is 7
    print(i)
```

These are the fundamental concepts of Python 3. As you become more familiar with the language, you can explore more advanced topics and libraries.
