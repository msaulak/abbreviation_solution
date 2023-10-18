import re
def get_abbreviations(word):
    ret = []
    for i in range(len(word)+1):
        for j in range(len(word)-i):
            if j+i <= len(word):
                following = get_abbreviations(word[j+i+1:])
            else:
                following = get_abbreviations("")
            for f in following:
                s = word[0:j] + str(i+1) + f
                digits = re.findall(r'\d', s)
                digitCount = len(digits)
                if digitCount > 1:
                    continue
                ret.append(s)
    ret.sort(key=lambda x: len(x))
    ret.append(word)
    return ret
