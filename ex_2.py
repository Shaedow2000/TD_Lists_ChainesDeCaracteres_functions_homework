import sys

def double( msg: str ) -> str:
    list_msg: list[ str ] = list( msg )
    new_msg_list: list[ str ] = []

    for i in range( len( list_msg ) ):
        new_msg_list.append( list_msg[ i ] )
        new_msg_list.append( list_msg[ i ] )

    new_msg: str = ''.join( new_msg_list )

    return new_msg

def main() -> None:
    msg: str = input( '-> Entrer un message: ' )

    print( double( msg ) )

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print( '\n--> Exit...' )
        sys.exit( 1 )
