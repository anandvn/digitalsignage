from django.http import HttpResponse
from django.template import loader
import csv
from web.models import ItemsFile
from web.models import HotItem
import os.path
import io
import urllib.request

def index(request, store=0):
    query = ItemsFile.objects.filter(store=store)
    query = query.order_by("-upload_date")

    if query.count() == 0:
        return landing(request)
    try:
        with query[0].specifications.open(mode="r") as csvfile:
            lines = csvfile.read()
            fieldnames=['id','external', 'desc', 'qoh', 'price']
            reader = csv.DictReader(io.StringIO(lines), fieldnames=fieldnames)
            item_list = [row for row in reader]
            context = { "item_list" : item_list }
            template = loader.get_template("web/index.html")
            return HttpResponse(template.render(context, request))
    except:
        return landing(request)

def landing(request):
    template = loader.get_template("web/404.html")
    context = { }
    return HttpResponse(template.render(context, request))

def dadjoke(request):
    url = "https://icanhazdadjoke.com/"
    hdr = { 'User-Agent' : 'mywoodcraft.com (https://github.com/anandvn/digitalsignage)' , 'Accept' : 'text/plain' }
    req = urllib.request.Request(url, headers=hdr)
    resp = urllib.request.urlopen(req)
    context = { 'dad_joke' : resp.read().decode() }
    template = loader.get_template("web/dadjoke.html")
    return HttpResponse(template.render(context, request))
    
def hotbuy(request, store=0):
    query = HotItem.objects.filter(store=store)
    if query.count() == 0:
        return landing(request)
    print(str(query[0]))
    context = { 'hot_buy' : query[0] }
    template = loader.get_template("web/hotbuy.html")
    return HttpResponse(template.render(context, request))
        
