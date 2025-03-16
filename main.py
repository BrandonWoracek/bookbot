from stats import get_book_words
from stats import get_book_characters
from stats import sorted_book_characters
import sys

#Function to acess the book file
def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents



#Main function
def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    filepath = sys.argv[1]
    book_text = get_book_text(filepath)
    word_count = get_book_words(book_text)
    sorted_book = sorted_book_characters(book_text)  # This will print the sorted characters
    
    # Print the word count with the desired format
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")


main()