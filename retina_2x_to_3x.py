def replace(m):
    num = float(m.group(1))
    num = num * 2 / 3
    return "%dpx" % (num)