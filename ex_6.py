import sys

def is_prime( num: int ) -> bool:
    for i in range( 2, num ):
        if ( num % i ) == 0:
            return False
    return True

def prime_numbers( numbers: list[ int ] ) -> list[ int ]:
    prime_list: list[ int ] = []

    for i in range( len( numbers ) ):
        if is_prime( numbers[ i ] ):
            prime_list.append( numbers[ i ] )

    return prime_list

def main() -> None:
    print( '--> Enter only one space between each number.' )
    while True:
        try:
            nums: list = input( '=> Numbers: ' ).split( ' ' )
            
            for i in range( len( nums ) ):
                nums[ i ] = int( nums[ i ] )

            print( f'>=> Prime Numbers: { prime_numbers( nums ) }' )
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
