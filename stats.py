
def get_numbers(file_path):
    return count_words(get_book_text(file_path))

def count_words(string):
    return len(string.split())


def get_book_text(file_path):
    contents = ""
    with open(file_path) as file:
        contents = file.read()
    return contents

