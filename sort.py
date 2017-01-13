"""

Sort a list of integers and strings.

Write a program that takes a list of strings containing integers and
words and returns a sorted version of the list.

All words must be in alphabetical order, all ints sorted numberically.

Keep element types in the same order (i.e. if the nth element is an int,
the final nth element must also be an int.)
"""
import sys
import string


def sort_strings(s):
    """Sort strings into a-z order."""
    return()


def sort_ints(i):
    """Sort ints smallest to largest."""
    return()


def consume_input(f):
    """Given file f, write to array of strings."""
    input_array = []
    return(input_array)


def clean_array(dirty_array):
    """Prepare array for sorting.

    Remove all special ascii characters that are not letters or digits.
    Cast any number strings to int.
    Return cleaned array.
    """
    # TODO: do we need to have an exception for something that's just
    # unallowed chars?

    # Create a set of all ascii letters and digits
    # NOTE TO SELF: union like this doesn't work with Python 2.7 or earlier
    ascii_allowed = set().union(*[string.ascii_letters, string.digits])

    clean_array = []
    for d in dirty_array:
        # Build new string as we go
        placeholder = ''
        # Initialize is_digit to false
        is_digit = False
        # Check each character in this string. If it is not in our allowed list
        # skip it. Otherwise, add to placeholder and check if it is a digit.
        # TODO: will I ever have a string that has a digit in it?????? re-read
        # directions.
        for character in d:
            if character in ascii_allowed:
                placeholder += character
                if character in string.digits:
                    is_digit = True
            else:
                continue
        if is_digit:
            clean_array.append(int(placeholder))
        else:
            clean_array.append(placeholder)

    return(clean_array)


def sort_array(array):
    """Given an array of strings and ints, sort."""
    # Array looks something like:
    # ['hello', 235, 'what', 0, 'idk', -12, 'y', 'x', 'z', 3]
    # for every string in the list, get strings in order
    # ...create list of strings, then sort
    # for every int in list, get ints in order
    # ...create list of ints, then sort
    # TODO: is this better with sets?? Probably, but figure out why...
    string_arr = []
    int_arr = []

    # Build out a string array and an int array for sorting
    # TODO: can probably build this and sort at the same time,
    # figure it out when optimizing code.
    for a in array:
        if type(a) == int:
            int_arr.append(a)
        # No need to do an explicit check since we've already ensured these
        # two types.
        else:
            string_arr.append(a)

    # Sort string list, int list
    # TODO:be sure on this implementation
    string_arr.sort()
    int_arr.sort()

    # Build output array from new array, mantaining type order.
    output_arr = []
    int_tracker = 0
    str_tracker = 0

    for a in array:
        if type(a) == int:
            output_arr.append(int_arr[int_tracker])
            int_tracker += 1
        else:
            output_arr.append(string_arr[str_tracker])
            str_tracker += 1

    return(output_arr)


def clean_and_sort(input_file, output_file):
    """Main function to consume file, sort, and write to output."""
    input_array = consume_input(input_file)
    cleaned_array = clean_array(input_array)
    sorted_array = sort_array(cleaned_array)
    return(sorted_array)


if __name__ == '__main__':
    # Handle missing args gracefully.
    if not len(sys.argv) == 3:
        print("""
            This program requires exactly two arguments:
            1) the path to the input.txt file, and
            2) the path to result.txt

            Please try again!
        """)
    else:
        clean_and_sort(sys.argv[1], sys.argv[2])