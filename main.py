def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    text_word_count = count_number_of_words(text)
    
    print(text)
    print("")
    print(f"This text contains {text_word_count} words!")


def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents


def count_number_of_words(string):
    words = string.split()
    word_count = len(words)
    return word_count


main()