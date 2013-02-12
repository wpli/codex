import sys

if __name__ == '__main__':
    x = sys.argv[1]
    rev_array = [ None ] * len( x )

    for idx, i in enumerate( x ):
        rev_array[-1-idx] = i

    print "".join( rev_array )


        
