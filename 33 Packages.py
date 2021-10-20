#Here  we imported shipping class but calling is differnt
#here we have to call method like ecommerce.shipping.method()
import ecommerce.shipping

# here cal_Shipping() method is imported
# we can simply call by calc_Shipping()
from ecommerce.shipping import calc_Shipping

# here shipping is now object and all methods are imported
# here we access method simply by shipping.method()
from ecommerce import shipping

#1
ecommerce.shipping.calc_Shipping()
#2
calc_Shipping()
#3
shipping.calc_Shipping()