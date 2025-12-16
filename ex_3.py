import sys

def main() -> None:
    msg: list = list( input( '=> message: ' ) )
    msg.reverse()
    print( ''.join( msg ) )

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit( 1 )
