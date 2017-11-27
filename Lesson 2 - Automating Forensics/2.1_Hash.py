# A common task in digital investigations is hash matching.
# We can use the hashlib library for the most common hashing algs.
import hashlib

# Use hashlib's md5 method to hash a string
# The method accepts binary data, so we need to cast the string to b
# Save the result in a variable "md5obj"
#md5obj = hashlib.md5(b"Whats up?")
# md5obj is a digest object. We want to print the hex digest
#print(md5obj.hexdigest())

# Next, hash a user input. First get the input.
#userString = input("Enter string to hash: ")
# We need to encode the user string
#md5obj = hashlib.md5(userString.encode())
# Print like before.
#print("MD5: " + md5obj.hexdigest())

# hasblib also supports sha1, sha256 and other common hashes
#sha1obj = hashlib.sha1(userString.encode())
#sha2obj = hashlib.sha256(userString.encode())
#print("SHA1: " + sha1obj.hexdigest())
#print("SHA256: " + sha2obj.hexdigest())

# Now that we can hash strings and user input,
# lets build a program to hash a file or a string.

import os, sys
# First, ask for a file name from the user
#fName = input("Please give the full path to a file: ")
# Check if the input is a real file
#if os.path.isfile(fName):
    # Here we are combining a lot of functions.
    #Try to keep code simple to read.
    # First, we open the file in "read" mode as binary
    # Next, use hashlib to make the hash
    # Use hexdigest to get the hex value of the hash
    # Finally, print the hex value of the hash
#    print(hashlib.md5(open(fName, "rb").read()).hexdigest())

# Let's accept a file as a command argument
# Get the number of arguments
#ARGL = len(sys.argv)
# Check if there is exactly 1 argument
#if ARGL < 2 or ARGL > 2:
    # Error message if more or less than 1 argument
#    print("Please give a file or directory to hash.")
#else:
    # Create variable toHash with the potential file name
#    toHash = sys.argv[1]
    # Check if toHash is a file
#    if os.path.isfile(toHash):
        # If yes, hash the file as before
#        print("We are going to hash a file!")
#        print(hashlib.md5(open(fName, "rb").read()).hexdigest())
    # Check if toHash is a directory
#    elif os.path.isdir(toHash):
#        print("We are going to hash a directory!")
        # If yes, list all the subfolders and files
#        for root, subdirs, files in os.walk(toHash):
#            for file in files:
                # Get each file, and hash
                #print(os.path.join(root, file))
                # Use os.path.join to join a directory and file name
#                FN = os.path.join(root, file)
                # Hash as before
#                print(hashlib.md5(open(FN, "rb").read()).hexdigest())
    # If input is not a file or directory, we can't do anything.
#    else:
#        print("No files found!")

# Lets call an external program and get it's result
# Note: the command will be specific to the operating system
# In this case, we want to create and compare fuzzy hashes with ssdeep
# We need to import the subprocess library
import subprocess
# Ask for the first file to hash
#toHash = input("What will we hash? ")
# Use subprocess to run ssdeep.exe against the file, and get the output
#out = subprocess.check_output(["ssdeep\ssdeep.exe", "-s", toHash])
# Here we can split the result by the newline chracters
#fuzzy = out.split(b"\r\r\n")
# Print only the fuzzy hash value - not header
#print(fuzzy[1].decode("utf-8"))
# Open a file in "append" writing mode
#with open('f1.tmp', 'a') as f:
    # Write the full fuzzy hash (with header) to f1.tmp
#    f.write(out.decode("utf-8"))
    # Close the file handle
#    f.close
# Get the second file to compare to the first
#toHash = input("What will we compare? ")
# Run ssdeep against the file. The -s command suppresses errors
#out = subprocess.check_output(["ssdeep\ssdeep.exe", "-s", toHash])
# Split like before
#fuzzy = out.split(b"\r\r\n")
#print(fuzzy[1].decode("utf-8"))
#with open('f2.tmp', 'a') as f:
#    f.write(out.decode("utf-8"))
#    f.close
# Here we use ssdeep to compare the two hashes saved in f1.tmp and f2.tmp
#print(subprocess.check_output(["ssdeep\ssdeep.exe", "-s", "-k", "f1.tmp", "f2.tmp"]).decode("utf-8"))
# Delete files f1.tmp and f2.tmp
#os.remove('f1.tmp')
#os.remove('f2.tmp')

# Assignment 2: To show the concepts we have been writing decode in order.
# Convert this code to functions. Use arguments on the command line to
# run different functions.
# For example:
#   hash.py md5 file -- should print the md5 sum of the file
#   hash.py fuzzy file1 file2 -- should compare the two files similarity

# ------ Hint ------
# Problem is that big files may not fit in memory!
# We can read the file in pieces, add each chunk and feed to md5
#def md5(fname):
#    hash_md5 = hashlib.md5()
#    with open(fname, "rb") as f:
#        for chunk in iter(lambda: f.read(4096), b""):
#            hash_md5.update(chunk)
#    return hash_md5.hexdigest() # Returns the hash
