def sort_alphabeticly( chars: str ) -> str:
    l: list[ str ] = list( chars )
    l.sort()

    return ''.join( l )

def main() -> None:
    msg: str = input( '=> Message: ' )

    print( f'--> { sort_alphabeticly( msg ) }' )

    return

if __name__ == '__main__':
    main()
