from stats import (
    count_character,
    count_word,
    sort_dict,
)
import sys


def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    c_word = count_word(text)
    char_dict = count_character(text)
    new_dict = sort_dict(char_dict)

    #sort
    

    print ("============ BOOKBOT ============")
    print (f'Analyzing book found at {book_path}')
    print ("----------- Word Count ----------")
    print (f'Found {c_word} total words')
    print ("--------- Character Count -------")
    for item in new_dict:
        if item[0].isalpha():
            print(f'{item[0]}: {item[1]}')
    print ("============= END ===============")

    return None

main()
