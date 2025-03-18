import stats


def main():
    filepath = "books/frankenstein.txt"
    chars, words = \
        stats.parse_file(filepath, stats.count_chars, stats.count_words)
    chars.sort(reverse=True, key=stats.sort_on_count)

    print(
        "============ BOOKBOT ============\n\
Analyzing book found at books/frankenstein.txt...\n\
----------- Word Count ----------"
    )
    print(f"Found {words} total words")
    print("---- Character Count ----")
    for char in chars:
        print(f"{char["name"]}: {char["count"]}")

    print("============= END ===============")

    return 0


main()
