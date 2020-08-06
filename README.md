# Credit Calculator
Credit Calculator is the program which takes several parameters such as credit principal and credit interest and then calculate the needed values (for example, monthly payment or over payment), and output them.
## Terms
### Installments
The best credits are probably those with a 0% interest; such credits are called installments.
### Differentiated Payment
This is a kind of payment where the part for reducing the credit principal is constant. Another part of the payment is for interest repayment and it reduces during the credit term. It means that the payment is different every month.
### Annuity
This is a kind of payment where you pay the whole interest of the payment at the time of principal payment.
### Principal
A principal is the original amount of money you get on credit. 
### Interest
An interest is the charge you pay for borrowing money, usually calculated as a percentage of the loan sum.
### Periods
number of months and/or years needed to repay the credit.
### Overpayment
Difference between all the payments made and principal.
## Formulae
1. payment = months / principal<br/>
2. lastpayment = principal − (periods−1) ∗ payment<br/>
3. ordinary_annuity(A) = P ∗ (1+i) ^ n / i ∗ (1+i) ^ n - 1<br/>
*P and n can be derived from above formula*<br/>

4. Montly_Interest(i) = 1/12 * Interest in percentage
5. Differentiated_Payment(D) = P / n + i * (P - (P * (m - 1)) / n)

 
