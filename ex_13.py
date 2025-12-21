def divisible_by_3_5( numbers: list[ int ] ) -> list[ int ]:
    l: list[ int ] = []

    for i in range( len( numbers ) ):
        if ( numbers[ i ] % 3 ) == 0 or ( numbers[ i ] % 5 ) == 0:
            l.append( numbers[ i ] )

    return l

def main() -> None:
    while True:
        try:
            nums: list = input( '=> Numbers: ' ).split( ' ' )

            for i in range( len( nums ) ):
                nums[ i ] = int( nums[ i ] )

            print( f'--> Les nombres divisibles par 3 et 5 sont: { divisible_by_3_5( nums ) }' )
            break
        except ValueError:
            print( '==> Entrer des nombres et/ou un seul espace...' )
            continue


if __name__ == '__main__':
    main()
