from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
import testing
from kucoin.client import Client
from pprint import pprint
import klines
from .models import Kline
import dbtest


'''
def home(request):

    symbol = request.GET.get('sym')
    if symbol is None:
        symbol='RPX'
    price=testing.get_current_price(symbol)


    ticks=testing.client.get_tick()
    btclist=[]
    for tick in ticks:
        tick['moreinfo']='so gibts extra infos{}db'.format(tick['coinTypePair'])
        if tick['coinTypePair']=='BTC':
            btclist.append(tick)





    print

    context = {
        "price": "%0.9f" % price,
        "symbol": symbol,
        "ticks":btclist,

#       "mods": mods,
    }


    return render(request, 'home.html', context)

'''

# Create your views here.
'''
def means_to_ticks(ticks):
    means=klines.get_market_mean_summary(klines.load_klines())
    for tick in ticks:
        x=tick['symbol']
        for mean in means:
            y=mean['market']

            if y == x:
                tick['mean_1'] = mean['mean_1']
                tick['mean_2'] = mean['mean_2']
                tick['mean_3'] = mean['mean_3']
                tick['mean_4'] = mean['mean_4']

    return ticks
'''
def prices(request):
    ticks=testing.client.get_tick()
    #ticks_with_mean=means_to_ticks(ticks)
    btclist=[]
    for tick in ticks:
        tick['moreinfo']='so gibts extra infos{}db'.format(tick['coinTypePair'])
        tick['means']= dbtest.get_means_from_db(tick['symbol'])
        if tick['coinTypePair']=='BTC':
            btclist.append(tick)
    print(btclist)
    #historical=dbtest.get_means_from_db(dbtest.list_markets())
    context = {
        "ticks":btclist,
        #"historical":historical,
#        "mods": mods,
    }
    return render(request, 'prices.html', context)

test_klines_data = {'KCS-BTC': [(1515976200, 0.00104405, 0.0011, 0.00104404, 0.0011, 11382.0343),(1515978000, 0.0011, 0.0011499, 0.00107798, 0.00107799, 26444.4279),(1515979800, 0.00107901, 0.00113, 0.00107901, 0.0010815, 8911.831),(1515981600, 0.00108102, 0.0011029, 0.00108, 0.00108607, 4231.17)]}


print

def dummy(request):
    k=Kline()

    k.timestamp=test_klines_data['KCS-BTC'][0][0]
    k.close=test_klines_data['KCS-BTC'][0][4]
    k.high=test_klines_data['KCS-BTC'][0][2]
    k.low=test_klines_data['KCS-BTC'][0][3]
    k.market=list(test_klines_data.keys())[0]
    k.open=test_klines_data['KCS-BTC'][0][1]
    k.volume=test_klines_data['KCS-BTC'][0][5]


    print
    context = {
#        "ticks":btclist,
#        "historical":historical,
#        "mods": mods,
    }
    return render(request, 'prices.html', context)


