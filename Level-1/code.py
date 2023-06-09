'''
////////////////////////////////////////////////////////////
///                                                      ///
///   0. tests.py is passing but the code is vulnerable  /// 
///   1. Review the code. Can you spot the bug?          ///
///   2. Fix the code but ensure that tests.py passes    ///
///   3. Run hack.py and if passing then CONGRATS!       ///
///   4. If stuck then read the hint                     ///
///   5. Compare your solution with solution.py          ///
///                                                      ///
////////////////////////////////////////////////////////////
'''

from collections import namedtuple
from decimal import Decimal

Order = namedtuple('Order', 'id, items')
Item = namedtuple('Item', 'type, description, amount, quantity')

max_amount = 100000 # max cost per item
max_quantity = 10 # max quantity
max_total = 1e10 # max total amount

def validorder(order: Order):
    net = Decimal('0')
    
    for item in order.items:
        if item.type == 'payment':
            # -max_amount < item.amount < max_amount
            if item.amount > -1*max_amount and item.amount < max_amount: 
                net += Decimal(str(item.amount))
        elif item.type == 'product':
            # 0 < quantity <= max_quantity, 0 < amount <= max_amount
            if item.quantity > 0 and item.quantity <= max_quantity and item.amount > 0 and item.amount <= max_amount:
                net -= Decimal(str(item.amount)) * item.quantity

            # max_total < net < -max_total - less than min/more than max amount 
            if net > max_total and net < -1*max_total: 
                return("Total amount exceeded")
        else:
            return("Invalid item type: %s" % item.type)
    
    if net != 0:
        return("Order ID: %s - Payment imbalance: $%0.2f" % (order.id, net))
    else:
        return("Order ID: %s - Full payment received!" % order.id)
