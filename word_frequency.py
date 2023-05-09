# import string

STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with'
]

PUNCTUATION = ['?', '!', '.', '"', ',']


# def remove_punctuation(words):
#     stripped_file = words.translate(str.maketrans('', '', string.punctuation))
#     return words

# ALTERNATE WAY TO DO REMOVE_FUNCTION
def remove_punctuation(s):
    for punc in PUNCTUATION:
        s = s.replace(punc, "")
    return s


def remove_stop_words(word_list):
    cleaned_list = []
    for word in word_list:
        if word not in STOP_WORDS:
            cleaned_list.append(word)
    return cleaned_list


def open_file(file):
    # uses `open` to read a text file
    with open(file) as opened_file:
        # file remains open for the indented lines under here
        read_file = opened_file.read()
    stripped_file = remove_punctuation(read_file).lower()
    word_list = stripped_file.split()
    cleaned_list = remove_stop_words(word_list)
    # print(cleaned_list)
    return cleaned_list


def sort_dictionary(dictionary):
    sorted_by_frequency = sorted(
        dictionary.items(), key=lambda x: x[1], reverse=True)
    return sorted_by_frequency


def print_word_freq(file):
    """Read in `file` and print out the frequency of words in that file."""
    # 1. use `open` to read a text file
    words_to_count = open_file(file)
    word_count = {
        # 'new': words_to_count.count('new')
    }
    for word in words_to_count:
        if word in word_count.keys():
            word_count[word] += 1
        else:
            word_count[word] = 1
    sorted_word_count = sort_dictionary(word_count)
    print(sorted_word_count)
    return sorted_word_count
    # loop through the list of words, and update the dictionary to indicate how many of each we have

    # need to print:
    # no. of spaces === len(longest key) - len(current key)
    # layout: spaces, current key, vertical line, freq, stars === freq


# EXAMPLE FROM MICHAEL // SORTED_LIST WAS SORTED_DICTIONARY
    # for thing, count in sorted_list:
    #     asterisks = '*' * count
    #     print(f'{thing} | {count} {asterisks}')


# def add_stars(tuples):
#     word_freq = open_file(file)
#     for tuple in tuples:
#         stars = tuple[1] + ' ' + '*'*tuple[1]
#     print(stars)
#     return stars


if __name__ == "__main__":
    import argparse
    from pathlib import Path

    parser = argparse.ArgumentParser(
        description='Get the word frequency in a text file.')
    parser.add_argument('file', help='file to read')
    args = parser.parse_args()

    file = Path(args.file)
    if file.is_file():
        print_word_freq(file)
    else:
        print(f"{file} does not exist!")
        exit(1)
