import sys

def longest( chars: list[ str ] ) -> str:
    index: int = 0

    for i in range( 1, len( chars ) ):
        if len( chars[ i ] ) > len( chars[ i - 1 ] ):
            index = i

    return chars[ index ]

def main() -> None:
    while True:
        chars: list[ str ] = input( '==> Enter message: ' ).split( ' ' )

        print( f'\n--> Longest word: { longest( chars ) }' )

        break


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print( '\n-> Exiting...' )
        sys.exit( 1 )
