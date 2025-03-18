def sort_on_count(d):
    return d["count"]


def count_words(string):
    return len(string.split())


def parse_file(file_path, *funcs):
    contents = ""
    outputs = []
    with open(file_path) as file:
        contents = file.read()
    for func in funcs:
        outputs.append(func(contents))
    return tuple(outputs)


def count_chars(text):
    counts = {}
    for char in text:
        if char.isalpha():
            key = char.lower()
            if key not in counts:
                counts[key] = 1
                continue
            counts[key] += 1
    lst = []
    for key in counts:
        lst.append(dict(name=key, count=counts[key]))
    return lst
