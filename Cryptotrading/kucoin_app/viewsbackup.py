from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
import testing
from kucoin.client import Client
from pprint import pprint

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


    return render(request, 'prices.html', context)



# Create your views here.
