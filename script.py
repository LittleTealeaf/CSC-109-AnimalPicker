#!/bin/env python3

val = ''
validOptions = ['cat','dog','fish']
while val not in validOptions:
    print('Which animal would you like to see?')
    print(', '.join(validOptions))
    val = input().lower()
    if val== 'cat':
        print(' _._     _,-\'\"\"`-._\n(,-.`._,\'(       |\\`-/|\n    `-.-\' \\ )-`( , o o)\n          `-    \\`_`\"\'-')
    elif val == 'dog':
        print('  __      _\no\'\')}____//\n `_/      )\n (_(_/-(_/"')
    elif val == 'fish':
        print('o           //        +\n o        //////    ++\n  .    @))))))))))+++\n   .}:<<)))))))))))++\n       <<\\\\)))))) +++\n          \\\\   \\\\   ++\n                      +')
    else:
        print('Invalid Response')