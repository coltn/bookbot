
def get_numbers(file_path):
    return count_words(get_book_text(file_path))


def count_words(string):
    return len(string.split())


def get_book_text(file_path):
    contents = ""
    with open(file_path) as file:
        contents = file.read()
    return contents


def count_chars(text):
    count = {}
    for char in text:
        key = char.lower()
        if key not in count:
            count[key] = 1
            continue
        count[key] += 1
    return count
