def main() -> None:
    li1: list = list( input( '==> List of chars 1: ' ) )
    li2: list = list( input( '==> List of chars 2: ' ) )

    li3: list = li1 + li2

    print( f'> { li3 }' )

if __name__ == '__main__':
    main()
