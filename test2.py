def plusMinus(arr):
    # Write your code here
    pos_elem = 0
    neg_elem = 0
    null_elem = 0
    for num in arr:
        if num < 0:
            neg_elem += 1
        elif num > 0:
            pos_elem += 1
        else:
            null_elem += 1
    
    print("{:.6f}".format(pos_elem / len(arr)))
    print("{:.6f}".format(neg_elem / len(arr)))
    print("{:.6f}".format(null_elem / len(arr)))

plusMinus([1,0,-1,-3,-2,1,2,10,200,0,0])