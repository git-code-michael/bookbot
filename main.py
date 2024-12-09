def main():
    book_path = "books/frankenstein.txt"
    print_book_report(book_path)


def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents


def count_number_of_words(string):
    words = string.split()
    word_count = len(words)
    return word_count


def get_unique_character_counts(string):
    character_count_dictionary = {}

    for character in string.lower():
        if character not in character_count_dictionary:
            character_count_dictionary[character] = 1
        else:
            character_count_dictionary[character] += 1
            
    return character_count_dictionary


def print_book_report(path_to_book):
    book_text = get_book_text(path_to_book)
    book_word_count = count_number_of_words(book_text)
    unique_character_counts = get_unique_character_counts(book_text)
    sorted_unique_character_counts = dict(sorted(unique_character_counts.items(), key=lambda item: item[1], reverse=True))
    
    print(f"--- Begin report of {path_to_book} ---")
    print(f"The book contains {book_word_count} words.")
    print()
    print(f"Unique alpha-character counts of book's text (in descending order):")

    for character in sorted_unique_character_counts:
        if character.isalpha():
            count = sorted_unique_character_counts[character]
            print(f"The '{character}' character was found {count} times.")

    print("--- End report ---")


main()