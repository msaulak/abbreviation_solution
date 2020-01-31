def _generate_abbreviations(word):
    """
    backtracking, pivoting letter
    :type word: str
    :rtype: List[str]
    """
    if not word:
        return [""]

    ret = []
    for i in range(len(word) + 1):
        left_num = str(i) if i else ""
        for right in _generate_abbreviations(word[i + 1:]):
            cur = left_num + word[i:i + 1] + right
            if cur == word or cur == str(len(word)):
                continue
            ret.append(cur)

    return ret


def generate_abbreviations(word):
    ret = _generate_abbreviations(word)
    ret_filtered = []

    if not word:
        return ret_filtered

    for s in ret:
        digit_count = sum(c.isdigit() for c in s)
        if digit_count < 2:
            ret_filtered.append(s)

    ret_filtered = sorted(ret_filtered, key=len)

    ret_filtered.insert(0, str(len(word)))
    ret_filtered.append(word)

    return ret_filtered

# print (generate_abbreviations("officially"))
# print (generate_abbreviations("is"))
