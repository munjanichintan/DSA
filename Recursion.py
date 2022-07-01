def removeX(string):
    if len(string) == 0:
        print(string)
        return string

    print(string)
    smallerOutput = removeX(string[1:])

    if string[0] == 'x':
        return smallerOutput
    else:
        return string[0] + smallerOutput

string = 'bxbx'
print(removeX(string))