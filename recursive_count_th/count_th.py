'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    count = 0
    
    # Base Case
    if "th" not in(word):
        return count
    
    else:
        count += 1
        end = word.find("th") + 2
        new_word = word[end:]
        count += count_th(new_word)
        
    return count
