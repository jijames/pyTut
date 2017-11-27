# Some pieces of code we need to run very often.
# Instead of typing the same code many times, we
# can create a function. A function is a small
# piece of code that we assign a name to. Everytime
# we call the function's name, the code inside will run.

# Here "def" defines a function
# Next is the function name. The name can be anything,
# but cannot have spaces. It should be memorable.
# Next are (). Inside we can put "arguments". Now, it's empty.
#def myFunction():
#    print("This text is inside the function.")

#print("Let's call our function!")
# Now we can "call" the fuction by using its name.
#myFunction() # Notice the () at the end of the function name

# An important point is that the function is written before
# we used its name. Python will read a script from top to bottom.
# However, when it comes to functions, it will only run them
# when we call them. So in this case, python found "def",
# and then moved on without running it. In then ran our second print
# statement, and then the function call.

# Now we are going to use some extra functionality. We can import
# extraction functions as python libraries. Python libraries arguments
# a very powerful way to make Python do what you want with little coding.

# import a library named sys
import sys
# Use the library by calling methods (like functions)
# sys.argv[] gets arguments given with the script at run time.
#print("The name of this script is " + sys.argv[0])
# We can count the number of arguments.
# Each argument is seperated by a space.
#print("Number of arguments: ", len(sys.argv))

# Let's take a file as an input, and check if it exists.
# We need to import the "os" library to work with files.
import os

# Let's check that there is 1, and only 1, argument.
#ARGL =  len(sys.argv) # Save value in variable
#FN = "" # Defining the variable here is important for scope.
#if ARGL < 2 or ARGL > 2: # Why do you think we said 2 here?
#    print("Please enter one argument.")
#else:
#    FN = sys.argv[1]
#    if os.path.isfile(FN):
#        print(FN + " is a file!")
#    else:
#        print(FN + " is NOT a file!")


# Notice there are two spaces to end the first if statement

# Let's try to get the extension of the file saved in FN
# The extension is usually the last 3 characters.
#print(FN[-3:]) # This way is splitting an array
# If we do it this way, then we have a problem without
# longer or shorter extensions .py || .jpeg.
# Instead we use a library to extract the extension.
#FN2, EXT = os.path.splitext(FN)
#print("The extension is " + EXT)
# Now we want to get rid of the .
# We can split the array from 1 to end [1:]
#print(EXT[1:]) # The array starts at 0. So the . was 0. We started at 1.


# Next, let's start to read the file
# A common task is to get the file header. We will need another
# library to convert binary to hex.
#from base64 import b16encode # Base 16 is our friend

# Here we are opeiong a file. The file name / location is in the FN var.
# rb stands for "read" and "binary". Read mode as a binary file.
# "as f" means load the data from FN into the variable f
# FN is the file name, f is the file handle. We opened the file.
#with open(FN, 'rb') as f:
    # Here we see f.read(4) - from the file (f), read 4 bytes
    # And base 16 encode the resulting data
    # We decode the 4 bytes as utf-8 to get the header value.
    # All of this is saved into the variable file_sig_hex
    #file_sig_hex = b16encode(f.read(4)).decode('utf-8')
    #print(file_sig_hex)


# Python is really good at lists and dictionaries
# Let's make a dictionary to lookup phone numbers.
# The name of the dictionary looks like a normal variable
# You might want to add a marker so you know its a dictionary
#dictPhone = {"Google":"111-1111", "Facebook":"222-2222","Naver":"333-3333","Twitter":"444-4444"}
# Print all of the values in the dictionary
#print(dictPhone)
# Get the value for Google if we know the key
#print("Googles number is: " + dictPhone["Google"])
# Get the value for Twitter if we know the key
#print("Twitters number is: " + dictPhone["Twitter"])
# Get the key for Facebook if we know the values
#for co, phone in dictPhone.items():
#    if phone == "222-2222":
#        print("Number 222-2222 is for " + co)
#    else
#        print("Number not found!")


# Assignment 1: Make a signature verification script.
# Get the file's header and extension, and compare to see if
# they match. Ref: https://www.garykessler.net/library/file_sigs.html
