# fibonnacci sequence

# print the last k 
def fib( n, k ):
    seeds = [ 0, 1 ]

    if k > 2:
        while len( seeds ) < k:
            seeds.append( seeds[-2] + seeds[-1] )

    if n == 0:
        return seeds[0]
    if n == 1:
        return seeds[-k:2]
    else:
        current_count = k-1
        while current_count < n:
            seeds.append( seeds[-2] + seeds[-1] )
            seeds = seeds[1:]
            current_count += 1

        return seeds
                          


               
if __name__ == '__main__':
    for i in ( 0, 1, 2, 3, 4, 5, 10, 20 ):
        print i, fib(i,5)
