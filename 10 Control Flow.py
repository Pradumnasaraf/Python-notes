print()
is_hot_day = False
is_cold = True

if is_hot_day:
    print("It's A Hot Day")
elif is_cold:
    print("It's A Cold Day")
else:
    print("It's A Normal Day")

price = 1000000
has_good_credit = True

if has_good_credit:
    downpayment =0.1*price
else:
    downpayment=  0.2* price

print(f"Down Payment $ {downpayment}")
