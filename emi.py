#PF-Assgn-20

def calculate_loan(account_number,salary,account_balance,loan_type,loan_amount_expected,customer_emi_expected):
    eligible_loan_amount=0
    bank_emi_expected=0
    eligible_loan_amount=0
    count=0
    temp=account_number
    while(account_number!=0):
       rem=account_number%10
       account_number=account_number//10
       count=count+1
    if(count==4 and rem==1):
        if(account_balance>=100000):
            if(salary>25000 and salary<=50000):
                eligible_loan_amount=500000
                bank_emi_expected=36
                if(loan_amount_expected<=eligible_loan_amount and customer_emi_expected<=bank_emi_expected):
                  
                    print("Account number:",temp)
                    print("The customer can avail the amount of Rs.", eligible_loan_amount)
                    print("Eligible EMIs :", bank_emi_expected)
                    print("Requested loan amount:", loan_amount_expected)
                    print("Requested EMI's:",customer_emi_expected)
                else:
                    print("The customer is not eligible for the loan")
                
                
            elif(salary>50000 and salary<=75000):
                eligible_loan_amount=6000000
                bank_emi_expected=60
                if(loan_amount_expected<=eligible_loan_amount and customer_emi_expected<=bank_emi_expected):
                    print("Account number:", temp)
                    print("The customer can avail the amount of Rs.", eligible_loan_amount)
                    print("Eligible EMIs :", bank_emi_expected)     
                    print("Requested loan amount:", loan_amount_expected)
                    print("Requested EMI's:",customer_emi_expected)
                else:
                    print("The customer is not eligible for the loan")    
                
            elif(salary>75000):
                eligible_loan_amount=7500000
                bank_emi_expected=84
                if(loan_amount_expected<=eligible_loan_amount and customer_emi_expected<=bank_emi_expected):
                    print("Account number:", temp)
                    print("The customer can avail the amount of Rs.", eligible_loan_amount)
                    print("Eligible EMIs :", bank_emi_expected)
                    print("Requested loan amount:", loan_amount_expected)
                    print("Requested EMI's:",customer_emi_expected)
                else:
                    print("The customer is not eligible for the loan")    
            else:
                print("Invalid loan type or salary")
        else:
             print("Insufficient account balance")
    else:
        print("Invalid account number")
                
   
calculate_loan(1001,40000,250000,"Car",300000,30)
