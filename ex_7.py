import sys

def is_pair( n: int ) -> bool:
    if ( n % 2 ) == 0:
        return True
    
    return False

def pair_numbers( numbers: list[ int ] ) -> list[ int ]:
    pairs: list[ int ] = []

    for i in range( len( numbers ) ):
        if is_pair( numbers[ i ] ):
            pairs.append( numbers[ i ] )
    
    return pairs

def main() -> None:
    print( '--> Enter only one space between each number.' )
    while True:
        try:
            nums: list = input( '=> Numbers: ' ).split( ' ' )
            
            for i in range( len( nums ) ):
                nums[ i ] = int( nums[ i ] )

            print( f'>=> Pair Numbers: { pair_numbers( nums ) }' )
            break
        except ValueError:
            print( '-> Enter numbers please...' )
            continue

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print( '--> Exiting...' )
        sys.exit( 1 )
