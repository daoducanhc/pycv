def smaller_k_time(image, k):
    hr = height//k
    wr = width//k
    return size_change(image, hr, wr)

def size_change(image, hr, wr):
    height = len(image)
    width = len(image[0])
    result = np.zeros((hr, wr))
    if(height%hr == 0): kr = height//hr
    else: kr = height // hr + 1
    if(width%wr == 0): kc = width//wr
    else: kc = width//wr + 1
    r_dis, index_r = 0,-1

    for r in range(height):
        index_c = 0
        c_dis = 0
        if r % kr != 0 and r_dis < height - hr:
            r_dis += 1
            continue
        else: index_r += 1
        for c in range(width):
            if(c % kc == 0 or c_dis == width - wr):
                result[index_r, index_c] = (image[r, c]/255)
                print(index_c)
                print(c_dis)
                index_c += 1
            else: c_dis += 1

    return result
