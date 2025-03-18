def get_num_words(text):
    words = text.split()
    return len(words)


def get_chars_dict(text):
    chars = {}
    text = text.lower()

    for c in text:
        if c in chars:
            chars[c] += 1
        else:
            chars[c] = 1
    return chars

'''
Purpose: Extracts the "num" value from a dictionary entry to use as the sort key.
Input:   A dictionary d with a key "num".
Output:  Returns the value of d["num"].
'''
def sort_on(d):
    return d["num"]


'''
Purpose: Converts a dictionary of {char: count} pairs into a sorted list of {"char": char, "num": count} dictionaries.
Steps:
    - Initialize an empty list: sorted_list.
    - Convert dictionary entries: Loop through each key (char) in num_chars_dict, and append a new dictionary {"char": ch, "num": num_chars_dict[ch]} to sorted_list.
    - Sort the list: Use sorted_list.sort(reverse=True, key=sort_on) to sort the list in descending order by the "num" value.
    - Return the sorted list.
'''
def dict_to_sorted_list(chars_dict):
    sorted_list = []
    
    for ch in chars_dict:
        sorted_list.append({"char": ch, "num": chars_dict[ch]})
        
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list


'''
READABILITY OPTIMIZED VER.
Uses list comprehension + negative lambda key to avoid reverse=True
'''
def LAMBDA_dict_to_sorted_list(num_chars_dict):
    return sorted(
        [{"char": k, "num": v} for k, v in num_chars_dict.items()],
        key=lambda x: -x["num"]
    )


'''
PERFORMANCE OPTIMIZED VER.

Eliminated Redundant Function:
 - Removed sort_on(d) helper function
 - Replaced with operator.itemgetter("num") (a faster, built-in alternative to lambda)

Dictionary Iteration:
 - Used num_chars_dict.items() instead of key iteration + value lookup
 - Avoids O(1) dictionary lookups in loops, which add up for large datasets

List Comprehension → Generator:
 - Used a generator expression (...) instead of building an intermediate list
 - Reduces memory usage for large datasets (processed in streaming fashion)

Single-Step Sorted List:
 - Combined list creation and sorting using sorted()
 - Avoids separate list initialization and explicit sorting

C-Level Optimization:
 - operator.itemgetter is implemented in C (vs Python lambda/helper functions)
 - Provides faster sorting execution
'''
from operator import itemgetter

def IGETTER_dict_to_sorted_list(num_chars_dict):
    return sorted(
        ({"char": ch, "num": num} for ch, num in num_chars_dict.items()),
        key=itemgetter("num"),
        reverse=True
    )