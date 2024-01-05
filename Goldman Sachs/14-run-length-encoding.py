# Traverse through the string, keep track of the current character and its count
# If the next character is different, append the current character and its count to the result

def encode(string):
    # Code here
    char = string[0]
    c = 1
    res = ''
    
    for ch in string[1:]:
        if ch != char:
            res += (char+str(c))
            char = ch
            c = 1
        else:
            c += 1
    res += (char+str(c))    
    return res
