# Strings In Python 

# Single Line Strings
s1 = "hello"
print(s1)

s2 = 'hello'
print(s2)

s3 = '''hello'''
print(s3)

s4 = """hello"""
print(s4)

# Multi Line Strings
# define_python = "Python is a high-level, general-purpose programming language. 
#         Its design philosophy emphasizes code readability with the 
#         use of significant indentation."
# print(define_python)

define_python = '''Python is a high-level, general-purpose programming language. 
        Its design philosophy emphasizes code readability with the 
        use of significant indentation.'''
print(define_python)

define_python = """Python is a high-level, general-purpose programming language. 
        Its design philosophy emphasizes code readability with the 
        use of significant indentation."""
print(define_python)

# Need single quote in a string
question = "how are you ?"
answer = 'im fine'
# answer = 'i'm fine' # SyntaxError
answer = "i'm fine"
print(answer)

# Need double quote in a string
question = "how are you ?"
# answer = "i"m fine" # SyntaxError
answer = 'i"m fine'
print(answer)

# Need single & double quote in a string
question = "how are you ?"
# answer = 'i"m fine i'm fine' # SyntaxError
answer = '''i"m fine i'm fine'''
answer = """i"m fine i'm fine"""
print(answer)

# Accessing Strings 
text = "python"
print(text)

# Accessing Characters Using Index 
# Positive Indexing
print(text[0])
print(text[1])

# Negative Indexing
print(text[-1])
print(text[-2])

# Beyond Index Range
# print(text[10]) # IndexError: string index out of range

print("============")

text = "python"
# Access All Characters
print(text[0])
print(text[1])
print(text[2])
print(text[3])
print(text[4])
print(text[5])

print("============")
# Access All Characters -> Assume we have 1000+ characters
# print(text[500])
# print(text[999])
text = "python is language"
for character in text:
    print(character)
print(type(text))

print("============")
    
# text = 12345 
# for character in text: # TypeError: 'int' object is not iterable
#     print(character)

text = "12345" 
for character in text: 
    print(character)

print("============")
    
prices_products = [1000,1500,2000,2500,10000]
for product_price in prices_products: 
    print(product_price)
print(type(prices_products))

print("============")


data = "python"
print(dir(data)) # yes __iter__ 

prices_products = [1000,1500,2000,2500,10000]
print(dir(prices_products)) # yes __iter__ 

text = 12345 
print(type(text))
print(dir(text)) # no __iter__ 

text = "python"
print("Length Of String: ",len(text))

prices_products = [1000,1500,2000]
print("Number Of Products: ",len(prices_products))

# Slicing -> string[start:end:step]
text = "python"
print(text[::])
print(text[0:3:1]) # pyt
print(text[0:3]) # pyt
print(text[1:3]) # yt
print(text[0:5:2]) # pto

text = "python"
        #     0 1 2 3 4    5
        #     p y t h o    n 
        #    -6 -5 -4 -3 -2 -1
print(text[-4:-1:1]) # tho
print(text[-4:-1:-1]) # noh -> empty
print(text[-4:-6:-1]) # ty

# String Concatenation 
s1 = "good"
s2 = "morning"
print(s1+s2)

# Formatted String Literals (f-strings)
age = 30
# print("My age is "+age) # TypeError: can only concatenate str (not "int") to str
print("My age is {age}")
print(f"My age is {age}")

# String Repetition
laugh = "Haha"
print(laugh)

hard_laugh = laugh * 10 
print(hard_laugh)

# String Immutability 
greet = "hello"
print(greet)
print(greet[0])
# Requirement is Hello
# greet[0] = "H" # TypeError: 'str' object does not support item assignment
print(greet)

# Example of mutable data type
greet = ['h','i']
print(greet)
print(greet[0])
greet[0] = "H"
print(greet)

