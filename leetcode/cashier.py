class Cashier:
    """
    3, 50%
    [1,  2,  3,  4,   5,  6,  7]
map{1:1, 2:2,3:3,4:4,5:5,6:6,7:7}
    [100,200,300,400,300,200,100]
    [1,2] [1,2] counter = 1
    1*100,+  200*2 = 500
    [3,7],[10,10] counter = 2
    10*300 + 10*100 = 4000 
    [1,2,3,4],[1,1,1,1,1,1,1]] counter = 3 %3 == 0
    100+200+300+400= 1000 -> 500
    first try
    init: o(n)
        counter, n, discount, products, prices,map
    getBill:o(products in bill)
        increase counter+=1
        amount = 0
        for price, prod in zip(prices, products):
            index = map[prod]
            amount += price*self.prices[index]

        if counter%n:
            apply discount to amount
        return amount
    """
    def __init__(self, n: int, discount: int, products: List[int], prices: List[int]):
        self.counter = 0
        self.n = n
        self.discount = discount
        self.products = products
        self.prices = prices
        self.map = {prod:i for i,prod in enumerate(products)}

    def getBill(self, product: List[int], amount: List[int]) -> float:
        self.counter +=1
        qty = 0
        for am, prod in zip(amount, product):
            index = self.map[prod]
            qty += am * self.prices[index]
        
        if self.counter%self.n == 0:
            #apply disc
            qty = qty*((100-self.discount)/100)
        return qty
        


# Your Cashier object will be instantiated and called as such:
# obj = Cashier(n, discount, products, prices)
# param_1 = obj.getBill(product,amount)