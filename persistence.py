def per(x):
    num = []
    int_num = []
    product = 1
    if len(str(x)) == 1:
        print("Done")
        return x
    for i in str(x):
        num.append(i)
    for y in num:
        f = int(y)
        int_num.append(f)
    for j in int_num:
        product *= j
    print(product)
    per(product)
    return product


per(int(input('Insert a number: ')))
