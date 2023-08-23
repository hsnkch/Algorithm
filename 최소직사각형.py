def solution(sizes):
    w = 0
    h = 0

    for size in sizes:
        size.sort()
        w = max(w, size[0])
        h = max(h, size[1])

    return w*h

print(solution([[60, 50], [30, 70], [60, 30], [80, 40]]))