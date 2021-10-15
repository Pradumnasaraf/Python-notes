has_high_income = True
has_good_credit = True
has_criminal_record = False

if has_good_credit and has_high_income:
    print("You are elegible for the loan")

elif has_good_credit or has_high_income:
    print("You are only eligible for a short term laon")

else:
    print("Sorry, you not eligible")


if has_good_credit and not has_criminal_record:
    print("Eligible")