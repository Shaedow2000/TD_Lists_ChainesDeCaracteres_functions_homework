from math import floor

def palindrome( li: list ) -> bool:
    lenght: int = len( li )
    middle: int = floor( lenght / 2 )

    pal: bool = False

    for i in range( lenght ):
        if i <= ( middle - 1 ):
            j: int = -i-1
            if li[ i ] == li[ j ]:
                pal = True 
    
    return True if pal else False

def main() -> None:
    list_chars: list[ str ] = list( input( '==> ' ) )

    if palindrome(list_chars):
        print( '-> This is a palindrome.' )
    else:
        print( '-> This is not a palindrome.' )

if __name__ == '__main__':
    main()
