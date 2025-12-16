import sys, os

def sum( numbers: list ) -> float:
    somme: float = 0

    for i in range( len( numbers ) ):
        somme += float( numbers[ i ] )

    return somme

def delete_spaces( l: list[ str ] ) -> list:
    lst: list = l[ : ]
    indexes: list[ int ] = []

    for i in range( len( l ) ):
        if l[ i ] == ' ' or l[ i ] == '':
            indexes.append( i )
        else:
            continue
    
    indexes.reverse()

    for i in range( len( indexes ) ):
        lst.pop( indexes[ i ] )    

    return lst

def is_number( nums: list[ str ] ) -> bool:
    all_numbers: bool = False
    for i in range( len( nums ) ):
        nums[ i ].replace( '-' if '-' in nums[ i ] else '+' if '+' in nums[ i ] else '', '' )
        
        try:
            float( nums[ i ] )
            all_numbers = True
        except ValueError:
            all_numbers = False

    if all_numbers:
        return True
    else:
        return False

def main() -> None:
    os.system( 'cls' if os.name == 'nt' else 'clear' )
    print( 'Enter the numbers that u want to add toghether. a number is spaced by the other by spaces.' )
    print( '[ Ctrl + C ] to exit' )
    while True:
        numbers_input: str = input( '=>> ' )
        numbers: list[ str ] = numbers_input.split( ' ' )
        numbers = delete_spaces( numbers )
        
        if is_number( numbers ):
            print( f'>> { sum( numbers ) }' )
            continue
        else:
            print( '>> You did not enter numbers. Please enter numbers.' ) 
            continue

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print( '\n=> Exiting...' )
        sys.exit( 1 )
