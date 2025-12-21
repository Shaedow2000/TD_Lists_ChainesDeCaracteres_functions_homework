import sys

def moyenne( numbers: list[ int ] ) -> float: 
    total: int = 0
    lenght: int = len( numbers )

    for i in range( lenght ):
        total += numbers[ i ]

    return total / lenght

def main() -> None:
    while True:
        print( '-> Enter numbers with spaces in between each number.' )
        try:
            nums: list = input( '=> Enter numbers: ' ).split( ' ' )

            for i in range( nums.__len__() ):
                nums[ i ] = int( nums[ i ] )

            print( f'>=> La moyenne est: { moyenne( nums ) }' )

            break
        except ValueError:
            print( '--> Enter numbers not letters or characters...' )
            continue


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print( '\n--> Exiting...' )
        sys.exit( 1 )
