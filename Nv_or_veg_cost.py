def calculate_bill_amount(food_type,quantity_ordered,distance_in_kms):
    bill_amount=0
    cost=0
    extra_price=0
    if(quantity_ordered>=1 and distance_in_kms>0):
        if(food_type=='N'):
            cost=150
        
            if(distance_in_kms<=3):
               extra_price=0
            elif(distance_in_kms>3 and distance_in_kms<=6):
              extra_price=((distance_in_kms-3)*3)
            elif(distance_in_kms>6):
              extra_price=9+((distance_in_kms-6)*6)
            bill_amount=(cost*quantity_ordered)+extra_price
        elif(food_type=='V'):
            cost=120
            if(distance_in_kms<=3):
               extra_price=0
            elif(distance_in_kms>3 and distance_in_kms<=6):
              extra_price=((distance_in_kms-3)*3)
            elif(distance_in_kms>6):
              extra_price=9+((distance_in_kms-6)*6)
            bill_amount=(cost*quantity_ordered)+extra_price
        else:
            return(-1)
    else:
        return(-1)   
    return bill_amount
bill_amount=calculate_bill_amount("N",2,10)
print(bill_amount)
