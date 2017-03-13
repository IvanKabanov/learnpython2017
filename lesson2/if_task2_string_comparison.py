def string_comparison(string1, string2):
    if string1 == string2:
        print('1')
        return 1
    else:
        if string2 == 'python':
            print('3')
            return 3
        else:        
            len(string1) > len(string2)
            print('2')
            return 2
        
string_comparison('qwerty33','python')
