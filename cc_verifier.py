print('      CREDIT CARD, VERIFICATION & CORRECTION')


def cc_verify():
    from luhn import verify
    from luhn import append
    print('1.APPEND/CORRECT')
    print('2.VERIFY YOUR CREDIT CARD')
    a = input('Please Choose Your Option: ')
    if a == '1':
        result1 = append(input('Enter Your Card: '))
        print(result1)
        return cc_verify()
    elif a == '2':
        result2 = verify(input('Enter Your Card: '))
        print(result2)
        return cc_verify()
    else:
        print('Unknown Input Please try Again....')
        return cc_verify()

cc_verify()
