from django.http import HttpResponse
from django.template import loader
import csv
from web.models import ItemsFile
import os.path

def index(request, store=511):
    query = ItemsFile.objects.filter(store=store)
    query = query.order_by("-upload_date")
    filename = "media/" + str(query[0].specifications)
    if not os.path.isfile(filename):
        return landing(request)

    with open(filename,newline='', encoding='utf-8-sig') as csvfile:
        fieldnames=['id','external', 'desc', 'qoh', 'price']
        reader = csv.DictReader(csvfile, fieldnames=fieldnames)
        item_list = [row for row in reader]
        context = { "item_list" : item_list }
        template = loader.get_template("web/index.html")
        return HttpResponse(template.render(context, request))

def landing(request):
    template = loader.get_template("web/404.html")
    context = { }
    return HttpResponse(template.render(context, request))

