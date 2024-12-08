def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    text_word_count = count_number_of_words(text)
    unique_character_counts = get_unique_character_counts(text)
    
    print(text)
    print("")
    print(f"This text contains {text_word_count} words!")
    print("")
    print(f"The unique character counts of this text are:\n{unique_character_counts}")


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


main()