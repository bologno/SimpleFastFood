from counter_class import Counter
#import Caja
#import Stock


class Order(Object):
    '''
    This class maps the order from customer, recording products and taotal
    and separated prices for them. balance and peformance can be draw from it.
    '''

    def __init__(self, choice, oldOrd, deliveryAdd, timeOrder = None, ticket):
        self.orderId = oldOrd + 1
        self.choice = choice
        self.deliveryAdd = deliveryAdd
        self.timeOrder = timeOrder
        self.cooking = False
        #self.cobrado = False
        self.delivered = False
        self.ticket = ticket

    def toKitchen(self, order):
        kitchenTxt = open('kitchenDisplay.txt', 'w+')
        kitchenTxt.write(self.choice)
        kitchenTxt.close()

        runningOrder = Counter()
        timerCocina = runningOrder.order(max(self.seleccion))
        timerCocina.start()

    def toDeliver(self):
        if not timerCocina:
            self.cooking = True
        if cooking:
            pedidoActual = Counter()
            timerDelivery = pedidoActual.delivery(self.dirDelivery)#This method caculates delivey time from store
            timerDelivery.empezar()

    def updateStockAndRegister(self):

        stockUpdate = open('stock.txt', 'w+')
        stockUpdate.write(self.choice)
        stockUpdate.close()

        updateRegister = open('todaSales.txt', 'w+')
        updateRegister.write(self.ticket)
        updateRegister.close()
