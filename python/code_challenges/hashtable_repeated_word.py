from python.code_challenges.data_structures.hashtable import Hashtable
import string


def first_repeated_word(str):
    new_table = Hashtable()
    remove_specials = str.translate(str.maketrans('', '', string.punctuation))
    key_list = remove_specials.split()
    for key in key_list:
        new_key = key.lower()
        if new_table.contains(new_key) is True:
            return new_key
        else:
            new_table.set(new_key, key)

    return None


if __name__ == '__main__':
    new_string = ' A B C D a'
    print(first_repeated_word(new_string))
