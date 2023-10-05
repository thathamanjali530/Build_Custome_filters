from django.shortcuts import render
import datetime
# Create your views here.
def built_in_filters(request):
    data='hAi HEllo hoW aRe YOU'
    dt=datetime.datetime.now()
    d={'data':data,'dt':dt}
    return render(request,'built_in_filters.html',d)


def customfilters(request):
    d={'data':'Hai pYthon How aRe YOU' }
    return render(request,'customfilters.html',d)