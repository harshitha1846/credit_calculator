from math import log, ceil, floor
import argparse
parser = argparse.ArgumentParser(argument_default = '')
parser.add_argument('--principal')
parser.add_argument('--interest')
parser.add_argument('--payment')
parser.add_argument('--periods')
parser.add_argument('--type')
args = parser.parse_args()
if args.type == 'diff':
    if args.periods and args.interest and args.principal and args.payment == '':
        P = int(args.principal)
        n = int(args.periods)
        interest = float(args.interest)
        if P > 0 and n > 0 and interest > 0:
            total_pays = 0
            i = (1/12) * (interest/100)
            for m in range(1, n + 1, 1):
                D = ceil((P/n) + (i * (P - (P * ((m -1) /n)))))
                total_pays += D
                print('Month {}: paid out {}'.format(m, D))
            print('\nOverpayment = {}'.format(total_pays - P))
        else:
            print("Incorrect parameters")
    else:
        print("Incorrect parameters")
elif args.type == 'annuity':
    if args.principal and args.payment and args.interest and args.periods == '':
        P = int(args.principal)
        A = float(args.payment)
        interest = float(args.interest)
        if P > 0 and A > 0 and interest > 0:
            i = (1/12) * (interest/100)
            n = ceil(log(A /(A - (i * P)), 1 + i))
            years = n // 12
            months = n % 12
            if years == 0:
                print('You need {} months to repay this credit!'.format(months))
            elif months == 0:
                if years == 1:
                    print('You need {} year to repay this credit!'.format(months))
                else:
                    print('You need {} years to repay this credit!'.format(years))
            else:
                print('You need {} years and {} months to repay this credit!'.format(years, months))
            print('Overpayment = {}'.format((n * A) - P))
        else:
            print("Incorrect parameters")
    elif args.principal and args.interest and args.periods and args.payment == '':
        P = int(args.principal)
        n = int(args.periods)
        interest = float(args.interest)
        if P > 0 and n > 0 and interest > 0:
            i = (1/12) * (interest/100)
            A = ceil(P * ((i * ((1 + i) ** n)) / (((1 + i) ** n) - 1)))
            print('Your annuity payment = {}!'.format(A))
            print('Overpayment = {}'.format((n * A) - P))
        else:
            print("Incorrect parameters")
    elif args.payment and args.interest and args.periods and args.principal == '':
        n = int(args.periods)
        A = float(args.payment)
        interest = float(args.interest)
        if A > 0 and n > 0 and interest > 0:
            i = (1/12) * (interest/100)
            P = floor(A / ((i * ((1 + i) ** n)) / (((1 + i) ** n) - 1)))
            print('Your credit principal = {}!'.format(P))
            print('Overpayment = {}'.format((n * A) - P))
        else:
            print("Incorrect parameters")
    else:
        print("Incorrect parameters")
else:
    print("Incorrect parameters")
