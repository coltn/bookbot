from stats import get_numbers

def main():
    word_count = get_numbers("books/frankenstein.txt")
    print(f"{word_count} words found in the document")
    return 0


main()
