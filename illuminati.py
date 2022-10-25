for i in range(1,10) :

        if i == 5:
                print((10-i)*' ','1'*int((i/2)-1), '1 0', '1 '*int(i/2))
        elif i == 6:
                print((10-i)*' ', '1'*int((i/2)-2), '1 000', '1 '*int((i/2)-1))
        elif i == 7:
                print((10-i)*' ', '1'*int((i/2)-2), '1 1 0', '1 '*int(i/2))
        else :
                print((10-i)*' ', '1 '*i)
