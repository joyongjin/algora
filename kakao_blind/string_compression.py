def check(s, k):
    new_s = ''
    i = 0
    count = 1
    last = None
    while i <= len(s):
        current = s[i:i + k] if i < len(s) else None
        if last is not None:
            if last == current:
                count += 1
            else:
                new_s += "{}{}".format(count if count > 1 else '', last)
                count = 1

        last = current
        i += k

    if i > len(s) - 1:
        new_s += s[i - k:]
    return new_s


def solution(s):
    return min([len(check(s, k)) for k in [*range(1, (len(s) // 2) + 1), [len(s)]]])
