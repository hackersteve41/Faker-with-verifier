from faker import Faker
from faker_e164.providers import E164Provider
import sys


def main():

    get_inpu = input('Do You Want To Generate Fake Data Y/N: ').lower()
    if get_inpu == 'y':
        def gendata():

            generate_data = Faker()
            generate_data.add_provider(E164Provider)
            name = generate_data.name()
            a= ('Name: ' + name + '\n')
            phone = generate_data.safe_e164(region_code="US")
            b = ('Phone Number (US): ' + phone + '\n')
            email = generate_data.email()
            c = ('Email: ' + email + '\n')
            address = generate_data.address()
            d = ('Address: ' + address + '\n')
            ssn = generate_data.ssn()
            e = ('SSN: ' + ssn + '\n')
            cc = generate_data.credit_card_full(card_type=None)
            f = ('Credit Card Details: ' + cc + '\n')

            print('Fake Data....')
            final = (a + '\n' + b + '\n' + c + '\n' + d + '\n' + e + '\n' + f + '\n' )
            print(final)

            fa = open('fake.txt', 'a')

            fa.write(a + '\n' + b + '\n' + c + '\n' + d + '\n' + e + '\n' + f + '\n')
            fa.close()


            ask = input('Do You Want To Generate Again: ').lower()
            if ask == 'y':
                gendata()
            elif ask == 'n':
                print('Exiting...')
                sys.exit()

            else:
                return main()

        gendata()

    elif get_inpu == 'n':
        exit()

if __name__ == '__main__':
    main()
