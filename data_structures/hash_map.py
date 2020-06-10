# Hash maps or Hash tables are data structures that maps keys to its value pairs
# In general, hash tables store key-value pairs and the key is generated using a hash function.
# Hash tables are implemented in python using in-built data type dictionaries
# Creating dictionaries
# 1. Using Curly braces ({})
# 2. Using dict() function
#


def create_dict():
    my_dict = {'Dave': '001', 'Ava': '002', 'Joe': '003'}
    print(my_dict)
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


if __name__ == '__main__':
    create_dict()
