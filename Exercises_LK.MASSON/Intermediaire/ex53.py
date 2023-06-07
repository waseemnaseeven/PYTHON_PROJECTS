def presenceVoyelle(phrase):
    bool = False
    for i in phrase:
        if i == 'A' or i == 'a':
            bool = True
            return (bool)
        elif i == 'E' or i == 'e':
            bool = True
            return (bool)
        elif i == 'I' or i == 'i':
            bool = True
            return (bool)
        elif i == 'O' or i == 'o':
            bool = True
            return (bool)
        elif i == 'U' or i == 'u':
            bool = True
            return (bool)
        elif i == 'Y' or i == 'y':
            bool = True
            return (bool)
    return (bool)

print(presenceVoyelle("rbhapm"))