# MODULE A: The status of the customers
def get_customer_status(years_active):
    if years_active >= 10:
        return 'platinum'
    else:  
        return 'standard'


# MODULE B: Given the status get the discounts of the clients 
def calculate_discount(status):
    if status == 'platinum':
        return 10
    if status == 'standard':
        return 0
    
    return 0