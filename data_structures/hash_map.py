# Hash maps or Hash tables are data structures that maps keys to its value pairs
# In general, hash tables store key-value pairs and the key is generated using a hash function.
# Hash tables are implemented in python using in-built data type dictionaries
# Creating dictionaries
# 1. Using Curly braces ({})
# 2. Using dict() function
#
import re

def create_dict():
    my_dict = {'Dave': '001', 'Ava': '002', 'Joe': '003'}
    my_dict["Victor"] = '004'
    print(my_dict)
    del my_dict['Dave']
    print(type(my_dict))


# Writing data files
def write_to_file():
    # open the file
    text_file = open("myfile.txt", 'w')
    for i in range(1, 11):
        text_file.write("%s\n" % i)
    text_file.close()


# Read data from a file
def read_from_file():
    text_file = open("readfile.txt", 'r')
    data = text_file.read()
    print(data)


# A prime number is only divisible by 1 and itself
def is_prime(n):
    return min([n % e for e in range(2, n)]) != 0

def implement_hash_table():
    stock_prices = {}
    with open("file.csv", 'r') as f:
        for entry in f:
            tokens = entry.split(',')
            date = tokens[0]
            price = float(token[1])
            stock_prices[date]=price


def format_sentence(sentence_input):
    # Create a list of words from the sentence
    words = sentence_input.split(" ")
    required_words = []
    if len(words) > 1:
        return words[0]
    pattern = re.compile(['a-zA-Z'])
    for word in words:
        # Check that the word does not contain a digit
        if re.match(pattern, word):
            required_words.append(word)
    return " ".join(i for i in required_words)




if __name__ == '__main__':
    create_dict()
