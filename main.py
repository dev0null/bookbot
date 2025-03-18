import sys
from stats import *

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def main():
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    chars_sorted_list = IGETTER_dict_to_sorted_list(chars_dict)
    print_report(book_path, words, chars_sorted_list)


def get_book_text(file_path):
    # A with block can be used to open a file
    # The with block automatically close the file when the block is exited
    with open(file_path) as f:
        return f.read()

def print_report(book_path, words, chars_sorted_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path.replace("./", '')}")
    print("----------- Word Count ----------")
    print(f"Found {words} total words")
    print("----------- Character Count ----------")

    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"{item['char']}: {item['num']}")

    print("============= END ===============")

if __name__ == '__main__':
    main()