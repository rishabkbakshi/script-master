import os

my_string = "WelCOmE tO PyThoN ScripTinG"
# your_string = input("Enter your string here: ")

lowercase_string = my_string.lower()
print(lowercase_string)

uppercase_string = my_string.upper()
print(uppercase_string)

swapcase_string = my_string.swapcase()
print(swapcase_string)

titlecase_string = my_string.title()
print(titlecase_string)


# Case folding can be used to match caseless strings (strings from other languages), whereas lower() just converts to lowercase
casefolded_string = my_string.casefold()
print(casefolded_string)

# Display Options for Strings in Terminal

#First get terminal size
terminal_dimensions = os.get_terminal_size() # Platform independent module to get terminal dimensions. Has rows and columns

print(my_string.center(terminal_dimensions.columns).title())
print(my_string.ljust(terminal_dimensions.columns))
print(my_string.rjust(terminal_dimensions.columns))

# Once the above strings are printed, they are fixed in place and do not dynamically change their positions on window re-size