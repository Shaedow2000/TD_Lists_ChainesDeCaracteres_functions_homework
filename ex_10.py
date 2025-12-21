import sys

def msg_voyelles( msg: str ) -> str:
    voyelles: list[ str ] = [ 'a', 'e', 'i', 'o', 'u', 'y' ]
    
    voyelles_trouver: list[ str ] = []

    for i in range( len( msg ) ):
        if msg[ i ] in voyelles:
            voyelles_trouver.append( msg[ i ] )

    return ' '.join( voyelles_trouver )


def main() -> None:
    msg: str = input( '=> Message: ' )

    print( f'--> Les voyelles trouver sont: { msg_voyelles( msg ) }' )

    return

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print( '\n--> Exiting...' )
        sys.exit( 1 )
