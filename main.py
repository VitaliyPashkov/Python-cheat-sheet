     ###Naming conventions###

# Variable lower_snake
first_name = 'Mike'

# Class and module CamelCase
class InvoiceDetail:

# Constant
MAX_USER = 100 # All uppercase

# Indentation : 4 spaces
if num > 9:
    print('Small number')
    
      ###Data type###    
      
name = 'Mike' # string
age = 42 # int
price = 199.99 # float
is_active = True # boolean
colors = ['red', 'green', 'blue'] # list
products = { 'name': 'iPad Pro', 'price': 199.99 } # dict
MAX_USER = 100 # Constant     

    ###Type conversion###
  
# Python is a strong type language
number = 50 + "50" # TypeError

# Convert to string
number = 50 + int("50") # 100

# Convert to string
my_text = str(199.99)   # "199.99"

# Convert to number
my_number = int('21.99') # 21
my_number = float('21.99') # 21.99

# Get type
type(my_text) # <class 'str'>
type(my_number) # <class 'float'>

# Check if number 0 to 9
isdigit('8') # True

# Check type
isinstance(my_number, int) # True

    ###Strings###

name = 'Mike'
# or
name = "Mike"
# or
message = """This is multiline
string that is easier to
read and assign"""

# escape characters \n will do a line break
message = "Hello \nWorld"

# raw string (ignore escape characters)
message = r"https:\\example.com\index.html"

# Convert to lower case
name.lower() # mike

# Convert to upper case
name.upper() # MIKE

# Convert first char to Capital letter
name.capitalize() # Mike

# Convert first char of all words to Capital letter
name = 'mike taylor'
name.title() # Mike Taylor

# Chain methods
name = 'MIKE'
name.lower().capitalize() # Mike

name = 'Mike'

# Start with ?
name.startswith('M') # true

# End with ?
name.endswith('ke') # true

# String length
len(name) # 4

# String concatenation
full_name = first_name + ' ' + last_name

# String format
full_name = f"{first_name} {last_name}"

# Remove leading and trailing characters (like space or \n)
text = ' this is a text with white space '
text.strip() # 'this is a test with white space'

name = 'Mike'
# Get string first character
name[0] # M

# Get string last character
name[-1] # e

# Get partial string
name[1:3] # ik

# Replace
name.replace('M', 'P') # Pike

# Find (return pos or -1 if not found)
name.find('k') # 2

# List to string
colors = ['red', 'green', 'blue']
', '.join(colors) # 'red, green, blue'  

    ###Commons functions###

# Print to console
print('Hello World')

# Print multiple string
print('Hello', 'World') # Hello World

# Multiple print
print(10 * '-') # ----------

# Variable pretty printer (for debug)
from pprint import pprint
pprint(products) # will output var with formatting

# Get keyboard input
name = input('What is your name? ')

# Random (between 0 and 1)
from random import random 
print(random()) # 0.26230234411558273

# Random beween x and y
from random import randint
print(randint(3, 9)) # 5

# Rounding
number = 4.5
print(round(number)) # 5

number = 4.5163
print(round(number, 2)) # 4.52

# Path
import os
current_file_path = __file__
folder_name = os.path.dirname(current_file_path)
new_path = os.path.join(folder_name, 'new folder')

# Round number
solution = round(12.9582, 2) # 12.96

    ###Conditionals###

if x == 4:
    print('x is 4')
elif x != 5 and x < 11:
   print('x is between 6 and 10')
else:
   print('x is 5 or greater than 10')

#In or not in
colors = ['red', 'green', 'blue', 'yellow']
if 'blue' in colors:
if 'white' not in colors:

# Ternary
print('y = 10') if y == 10 else print('y != 10') 

# ShortHand Ternary
is_valid = 'Valid'
msg = is_valid or "Not valid" # 'Valid'

# Falsy
False, None, 0, empty string "", empty list [], (), {}

# Truthy
True, not zero and not empty value 
