def hash(s):
    st, m = 31, 10 ** 9 + 13
    h = 0
    for i in s:
        h = (h * st % m + ord(i)) % m
    return str(h)


if __name__ == '__main__':
    print(hash('kdjgksd'))
