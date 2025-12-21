import sys

def somme_cumulative( numbers: list[ int ] ) -> list[ int ]:
    list_sommes: list[ int ] = [ numbers[ 0 ] ]

    for i in range( 1, len( numbers ) ):
        list_sommes.append( list_sommes[ i - 1 ] + numbers[ i ] )

    return list_sommes

def main() -> None:
    print( '--> Enter des nombres avec un espace entre eux.' )
    while True:
        try:
            nums: list = input( '=> Numbers: ' ).split( ' ' )

            for i in range( len( nums ) ):
                nums[ i ] = int( nums[ i ] )

            print( f'-> Nouvelle list: { somme_cumulative( nums ) }' )
            break
        except ValueError:
            print( '=> Enter numbers please...' )
            continue

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print( '\n--> Exiting...' )
        sys.exit( 1 )
