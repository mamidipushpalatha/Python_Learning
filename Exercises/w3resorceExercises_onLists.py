#  Write a Python program to count the number of strings from a given list of strings.
# The string length is 2 or more and the first and last characters are the same.
def match_words(words):
    ctr = 0

    for word in words:
        if len(word) > 1 and word[0] == word[-1]:
            ctr += 1
    return ctr


print(match_words(['abca', 'xyz', 'aba', '1221']))
# Write a Python program to get a list, sorted in increasing order by the
# last element in each tuple from a given list of non-empty tuples.
# Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
# Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]

list1 = [(5, 5), (1, 2), (4, 4), (2, 3), (3, 1)]
# [(3, 1), (1, 2), (2, 3), (4, 4), (5, 5)]
list1.sort(key=lambda list1: list1[1])
# list1.sort(key=lambda list1: list1[1], reverse=True)  #[(5, 5), (4, 4), (2, 3), (1, 2), (3, 1)]
# print(sorted(list1, reverse=True))- o/p: [(5, 5), (4, 4), (3, 1), (2, 3), (1, 2)]

print("sorted in increasing order by the last element in each tuple: " + str(list1))

# Write a Python program to check if a list is empty or not


def check(lis):
    if lis == []:
        return True
    else:
        return False


print("checking lis is empty or not: " + str(check([])))

l = []
if not l:
    print("list is empty")


def func(f1, f2):
    if f1 == f2:
        return True
    else:

        return False


print("funtion is:" + str(func([2, 3, 4], [2, 7, 4])))


def common_data(list1, list2):
    result = False
    for x in list1:
        for y in list2:
            if x == y:
                result = True
                return result


print("common data is " + str(common_data([1, 2, 3], [1, 29, 3])))
# Write a Python program to find the list of words that are longer than n from a given list of words.


def long_words(n, str):
    word_len = []
    txt = str.split(" ")
    for x in txt:
        if len(x) > n:
            word_len.append(x)
    return word_len


print(long_words(3, "The quick brown fox jumps over the lazy dog"))
