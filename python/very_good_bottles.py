#! /usr/bin/python

# This function prints the constructed verse from form_verse(bottles) function.
def write_verse(verse):
    print(verse)

# This function constructs each verse (consisting of two lines) to be printed to screen.
def form_verse(bottles):
# Cast the integer variable bottles, and integer result from bottles - 1, into strings.
# This allows concatenation of these values with other strings, using the "+" operator.
    bwall = str(bottles)
    bleft = str(bottles - 1)

# These two lines form the two lines of a verse. If the bottles on the wall is greater
# than 2 and smaller than 100, theses can be printed to screen as is.
    line1 = bwall + " bottles of beer on the wall, " + bwall + " bottles of beer.\n"
    line2 = "Take one down and pass it around, " + bleft + " bottles of beer on the wall.\n"

# Check for special cases! Notice how the most common and simplest occurrence is checked first.
# The last case (bottles == 0) is the least common and involves the most complex action. It also
# results in the end of this program using the "return" keyword to exit the function.
    if bottles > 2:
        write_verse(line1 + line2)
    elif bottles == 2:
            line2 = line2.replace("bottles", "bottle")
            write_verse(line1 + line2)
    elif bottles == 1:
            line1 = line1.replace("bottles", "bottle")
            line2 = line2.replace("0", "no more")
            write_verse(line1 + line2)
    elif bottles == 0:
# Something tricky with the next two lines. :)
# If I use just the first line and not the second, then the sentence is
# grammatically wrong. Try it.
        line1 = line1.replace("0", "no more")
        line1 = line1.replace("no more", "No more", 1)
        line2 = "Go to the store and buy some more, 99 bottles of beer on the wall."
        write_verse(line1 + line2)
        return

# Demonstrates recursion: a function invoking itself. Notice that the bottles parameter is
# is reduced by 1 each time this function runs, until it reaches 0.
    form_verse(bottles - 1)

# Calls form_verse(bottles) function, which will keep calling itself until bottles = 0.
form_verse(99)