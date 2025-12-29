def solution(sizes):
    for i in range(len(sizes)):
        w, h = sizes[i]
        if w < h:
            sizes[i] = h, w
    
    max_w = max(size[0] for size in sizes)
    max_h = max(size[1] for size in sizes)

    return max_w * max_h