def reverse_half_loop(string):
    result = list(string)
    length = len(result)
    for c in range(length // 2):
        decal = length - 1 - c
        result[c], result[decal] = result[decal], result[c]
    return ''.join(result)


def recursive_reverse(string):
    return string[-1] + recursive_reverse(string[:-1]) if string else ''


if __name__ == '__main__':
    print(recursive_reverse('Hi my name is Yongjin Jo'))
    print(reverse_half_loop('Hi my name is Yongjin Jo'))
