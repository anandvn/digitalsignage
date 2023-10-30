from django.http import HttpResponse
from django.template import loader
import csv
from web.models import ItemsFile
import os.path
from decouple import config
import io

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

