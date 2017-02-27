for i in range(1,1000):
    digit_list=str(i)
    digit_list=list(map(int, digit_list))
    prod=1
    sum1 = sum(digit_list)
    for j in digit_list:
        prod = prod * j
    k=(i % sum1)
    if k==0:
        print (i,"Is Harshad number")
    if prod!= 0:
        y=(i % prod)
        if y==0:
            print (i,"Is divisible by the product of it's digits")
