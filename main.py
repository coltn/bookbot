def main():
    word_count = count_words(get_book_text("books/frankenstein.txt"))
    print(f"{word_count} words found in the document")
    return 0

def count_words(string):
    return len(string.split())


def get_book_text(file_path):
    contents = ""
    with open(file_path) as file:
        contents = file.read()
    return contents




main()
