def convert_currency(amount_needed_inr,current_currency_name):
    current_currency_amount=0
    if(current_currency_name=='Euro'):
        return amount_needed_inr*0.01417
    elif(current_currency_name=='british pound'):
        return amount_needed_inr*0.0100
    elif(current_currency_name=='Australian dollar'):
        return amount_needed_inr*0.02140
    elif(current_currency_name=='canadian dollar'):
        return amount_needed_inr*0.02027
    else:
        return -1
    return current_currency_amount
currency_needed=convert_currency(2000,"Australian dollar")
if(currency_needed!= -1):
    print(currency_needed )
else:
    print("Invalid currency name")
