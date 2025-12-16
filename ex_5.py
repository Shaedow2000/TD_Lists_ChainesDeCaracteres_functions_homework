from math import floor

def palindrome( li: list ) -> bool:
    lenght: int = len( li )
    middle: int = floor( lenght / 2 )

    print( middle )

    for i in range( lenght ):
        if i <= ( middle - 1 ):
            j: int = -i-1
            if li[ i ] == li[ j ]:
                pass
    
    return True

def main() -> None:
    list_chars: list[ str ] = list( input( '==> ' ) )

    palindrome(list_chars)

if __name__ == '__main__':
    main()
