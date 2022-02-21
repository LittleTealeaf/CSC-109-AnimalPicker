
val = ''
validOptions = ['cat','dog']
while val not in validOptions:
    print('Which animal would you like to see?')
    print(','.join(validOptions))
    val = input().lower()
    if val== 'cat':
        print('CAT ASCII ART HERE')
    elif val == 'dog':
        print('DOG ASCII ART HERE')
    else:
        print('Invalid Response')