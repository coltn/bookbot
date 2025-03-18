import sys
import os
import stats


def main():
    usage = "Usage: python3 main.py <path_to_book>"
    if len(sys.argv) != 2:
        print(usage)
        sys.exit(1)

    filepath = sys.argv[1]

    if not os.path.exists(filepath):
        print(usage)
        sys.exit(1)

    chars, words = \
        stats.parse_file(filepath, stats.count_chars, stats.count_words)
    chars.sort(reverse=True, key=stats.sort_on_count)

    print(
        f"============ BOOKBOT ============\n\
Analyzing book found at {filepath}...\n\
----------- Word Count ----------"
    )
    print(f"Found {words} total words")
    print("---- Character Count ----")
    for char in chars:
        print(f"{char["name"]}: {char["count"]}")

    print("============= END ===============")

    return 0


main()
