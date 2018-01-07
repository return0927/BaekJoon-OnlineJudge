def prime(num):
    skip = [1]

    for n in range(1, int( num**1/2 )+1):
        if n in skip: continue
        #print(n)
        if num % n:
            continue
            max_multiply = num // n
            skip += range(n, n*max_multiply, n)
            skip = list(set(skip))

            me = skip.index(n)
            skip = skip[me:]
        else:
            break

    if n == int(int( num**1/2 )): print("Prime")
    else: print("No Prime", n)

import cProfile
cProfile.run('prime({})'.format(input(": ")))
