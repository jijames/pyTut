
# Our first Python script

# Print text to your command prompt
print("Hello CTINS!")
print("안녕하세요!")


# Ask the user for input
#print("What is your name?")
# Get whatever the user typed, and save in "name" variable
#name = input()
# Print some text, plus the saved name
#print("Nice to meet you, " + name)

# Use the len function to find the length of the name
#print(len(name))

# Ask the user for their age
#print("What is your age?")
# Wait for the user to input an age, and save it in the "age" variable
#age = input()

# More complicated string creation
# Take the age as a number (int type)
# Add that number plus 1
# Convert that number to a string type
# Combine the first, second and third parts of the string
# Print it all on the screen
#print("You will be " + str(int(age) + 1) + " in a year.")

# Again asking the user for some input
#print("Do you speak Japanese, Korean or English?")
# Save input to the "lang" veriable
#lang = input()

# Next: Make a decision based on a conditional check

# For this part, notice the space at the beginning of the line.
# In Python, that indention is *very important*. Python uses
# indentation to group code together rather than brackets {}

# If the text in lang is *exactly* "Japanese" (note the uppercase J)
#if lang == "Japanese":
    # Then print hello in Japanese
    # Requires correct language packs to view properly
#    print("こんにちは!")
# If the first check fails (text is not Japanese), go to next check
# If the text in lang is *exactly* "Korean" (note the uppercase K)
#elif lang == "Korean":
    # Print hello in Korean
    # Requires correct langauge packs to view properly
#    print("안녕하세요!")
# If the text was not Japanese or Korean, check for English
#elif lang == "English":
    # Here we are using array slicing to display the text reversed
#    print("English? How about now?"[::-1])
# If the text was not Japanese, Korean or English, everything else will
# end up at the last "else" check. This is true for "everything else".
# You do NOT need to have an else, but it is very common.
#else:
#    print("I don't know your language, but you're still great!")

# Make sure there is at least one empty space to denote the end

# Now we can print output and ask for input from the user
# We can save that input in a variable and make decisions about it
# Sometimes we need to repeat tasks over and over again.
# We can repeat tasks with "loops".

# !!!!!! This will run forever !!!!!!!!
# To get out of the loop, type  ctrl+c
#while(1):
#    print("Do you like infinite loop jokes?")
#    input()

# ctrl+c is the "KeyboardInterrupt". Let's do something with it.
# To "catch" exceptions, like errors, we can use a try-catch block
#try:
#    while(1):
#        print("Do you like infinite loop jokes?")
#        input()
#except (KeyboardInterrupt, SystemExit):
#    print("Agh! You got me!")
#except:
#    print("Some other error happended")

# Listening for eceptions is very useful for catching errors,
# restarting processes and making sure your program closes correctly.
# For example, you want want to catch program exits and save config files,
# or clean up temporary files your programming was using.
