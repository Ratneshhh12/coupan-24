def calculate_coupan_discount(toatl_amount, is_present_discount_type, is_amount_discount_type, 
                              minimum_cart_value, maximum_discount_amount_limit, discount):

   discount_amount =0


   if(total_amount > minimum_cart_value):
    if(is_present_discount_type == true):
        discount_amount = (amount / 100) * total_amount
        if(discount_amount<maximum_discount_amount_limit):
            return discount_amount
         else:
            return maximum_discount_amount_limit

       elif(is_amount_discount_type == True):
        discount_amount = total_amount - maximum_discount_amount_limit
       if(discount_amount<discount_value)
        return discount_amount
      else
        return maximum_discount_amount_limit
else

        print("Total amount doesnt match with minimum")