from stats import get_book_text, count_chars  # word_count


def main():
    # word_count = get_numbers("books/frankenstein.txt")
    char_count = count_chars(get_book_text("books/frankenstein.txt"))
    print(f"{char_count} words found in the document")
    return 0


main()
