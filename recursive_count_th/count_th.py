'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    
    # fail with any words less than 2 characters in length (th)
    if len(word) <= 1:
        return 0
    # check if word has 'th' in it anywhere
    if word.find("th") == -1:
        return 0

    else:    
    # if none of the above is true, get index where it is found
        index = word.find("th")
    # set count to 1+ what the function returns   
    # which starts word at index + 2 - to start at the letter after 'h'
        th_count = 1 + count_th(word[index + 2:])
    # return value
        return th_count
