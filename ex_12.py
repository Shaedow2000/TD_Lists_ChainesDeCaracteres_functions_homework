def sort_alphabeticly( chars: str ) -> str:
    l: list[ str ] = list( chars )
    l.sort()

    return ''.join( l )

def main() -> None:
    while True:
        msg: str = input( '=> Message: ' )

        print( f'--> { sort_alphabeticly( msg ) }' )

        break

if __name__ == '__main__':
    main()
