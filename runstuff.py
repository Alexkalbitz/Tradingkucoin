from pprint import pprint
import testing


singlemarketcheck='QLC'
markets=testing.list_markets()
coinlist=testing.coin_list()
pricelist=testing.get_all_current_prices(markets)
print (pricelist)

#get_all_current_prices()
testing.get_current_price(singlemarketcheck)

'''get_tradingvolume_mean(symbol,time)'''
s1,m1 = testing.get_tradingvolume_mean(singlemarketcheck,60)
s2,m2 = testing.get_tradingvolume_mean(singlemarketcheck,10)






