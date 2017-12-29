import codecademylib
import pandas as pd

visits = pd.read_csv('visits.csv',
                     parse_dates=[1])
cart = pd.read_csv('cart.csv',
                   parse_dates=[1])
checkout = pd.read_csv('checkout.csv',
                       parse_dates=[1])
purchase = pd.read_csv('purchase.csv',
                       parse_dates=[1])

visits_cart = pd.merge(visits, cart)

visits_cart[visits_cart.cart_time.isnull()]

float(len(visits_cart))/float(len(visits))

cart_checkout = pd.merge(cart, checkout, how = "left")

cart_checkout[cart_checkout.checkout_time.isnull()]

float(len(cart))-float(len(checkout))/float(len(cart_checkout))

all_data = visits.merge(cart, how='left')\
.merge(checkout, how="left")\
.merge(purchase, how="left")

all_data[all_data.purchase_time.isnull()]

(float(len(checkout))-float(len(purchase)))/float(len(all_data))

all_data['time_to_purchase'] = \
    all_data.purchase_time - \
    all_data.visit_time
    
print all_data.time_to_purchase

print all_data.time_to_purchase.mean()





