"""LING 131A ASSIGNMENT 1

Solve the four problems below. Do this by editing the skeleton code given. Do
not change the names of the functions in the skeleton code. You are free to add
more functions as you see fit. You may use Python libraries if you are aware of
them, but all you need to do this assignment has been presented in class.

The problems are more or less listed in order of increasing difficulty. The
first two are the easiest, three is a bit harder and 4 is the trickiest.

Edit this file and then submit it on LATTE.

This is due Thursday September 27th, late submissions accepted till September
28th 12:30, possibly with a penalty of a deduction up to 20%.


PROBLEM 1.

Write a function called is_determiner() that takes a word as input and decides
wheter it is a determiner.

>>> is_determiner('the')
True
>>> is_determiner('thesis')
False

Then create another function remove_determiners() that uses is_determiner() and
that eliminates all determiners in a piece of a text.

>>> remove_determiners('The dog is asleep in a basket.')
'dog is asleep in basket.'

Do not worry about punctuation. But do worry about capitalization, so you want
to remove words like 'The'.


PROBLEM 2.

Write a function called remove_middle1() that removes some interior part of a
list. The function takes three arguments: the list to remove elements from, the
index of the first element to remove, and the index of the last element to
remove.

>>> lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> remove_middle1(lst, 3, 7)
>>> lst
[1, 2, 3, 9]

This is easier than you might think. But do consider what happens when you want
to use the function to remove the third through seventh element of a list that
has only two elements.

Part two of this problem is to write a function remove_middle2() that does the
same, except that it does not change the list that you hand in, instead, it
returns a new list that has the elements removed.

>>> lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> new_lst = remove_middle2(lst, 3, 7)
>>> new_lst
[1, 2, 3, 9]
>>> lst
[1, 2, 3, 4, 5, 6, 7, 8, 9]


PROBLEM 3

Write a Python function count_strings() to count the number of strings where the
string length is 3 or more and the first and last character are from a given
sequence of characters. The function takes two arguments, the input list and the
characters to check for.

>>> count_strings(['the', 'cat', 'is', 'asleep'], 'etc')
>>> 2

This returns 2 because only "the" and "cat" match the requirements. The others
are too short ("is") or do not start and end with the specified characters
("is" and "asleep").


PROBLEM 4.

Write a function has_most_consonants() that takes a string as input and returns
the words that have the largest number of consonants in them. For this exercise,
consonants are just letters like t and k (in fact, all letters except a, e, i, o
and u). You may use split() to get the tokens and you do not need to worry about
splitting off punctuations.

>>> has_most_consonants('The door is closed. And many dogs barked.')
['closed.', 'barked.']
>>> has_most_consonants('')
[]

"""


# PROBLEM 1 - determiners

def is_determiner(word):
    # replace this
    s = set(['the', 'a','an', 'some','my', 'your', 'his', 'her', 'its', 'our', 'their'
    , 'whose','this','that','those','these',
    'few','little','much','many','lot','most','any','enougn',
    'all', 'both', 'half','either','neither','each','every','other','another'])
    return True if word.lower() in s else False

def remove_determiners(text):
    # replace this
    l = text.split()
    l_new = []
    l_new = [a for a in l if not is_determiner(a)]
    # for word in l:
    #     if not is_determiner(word):
    #         l_new.append(word)
            
    return ' '.join(l_new)


# PROBLEM 2 - remove interior of list

# Not the use of "pass". This is a usefull little placeholder for code that you
# have not written yet, it does not do anything, but it makes the syntax legal

def remove_middle1(lst, first, last):
    # replace this, 
    lst[first:last+1] = []
    ##lst[first:last] = ''
    pass

def remove_middle2(lst, first, last):
    # replace this
    return lst[:first] + lst[last+1:]


# PROBLEM 3 - counting strings

def count_strings(lst, chars):
    s = set(chars)
    count = 0
    for l in lst:
        if l[0] in s and l[-1] in s and len(l)>=3:
            count += 1

    return count


# PROBLEM 4 - consonants

def has_most_consonants(text):
    # replace the body of this function, it is just some stupid code that gets
    # it right for th eexamples mentioned above
    if text == '':
        return []
    else:
        s = text.split()
        result = []
        letters = set([chr(i) for i in range(97,123)])
        contsonants = letters - set('aeoui')
        max_count = 0
        for word in s:
            count = 0
            for i in word:
                if i.lower() in contsonants:
                    count += 1
            if count > max_count:
                max_count = count
                result = [word]
            elif count == max_count:
                result.append(word)
            

        return result




if __name__ == '__main__':

    # here you can put code where you test what you are doing, for example

    result = is_determiner("Door")
    print(result)
    text = 'The dog is asleep in a basket.'
    result = remove_determiners(text)
    print(result)
    lst = [1,2,3,4,5,6,7,8,9]
    first = 2
    last = 5
    ###negative index
    remove_middle1(lst,first,last)
    print(lst)
    result = remove_middle2(lst,first,last)
    lst = ['the', 'cat', 'is', 'asleep','happy', 'pity']
    result = count_strings(lst, 'apty')
    print(result)
    result = has_most_consonants(text)
    print(result)



