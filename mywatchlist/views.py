from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import render
from mywatchlist.models import Myfavoritewatchlist


def show_mywatchlist(request):
    favorite_film = Myfavoritewatchlist.objects.all()
    context = {
        'list_favoritefilm': favorite_film,
        'nama': 'Adly Renadi Raksanagara',
        'student_id':'2106752306'
    }
    return render(request, "mywatchlist.html", context)

def show_xml(request):
    data = Myfavoritewatchlist.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
def show_json(request) : 
    data = Myfavoritewatchlist.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
def show_json_by_id(request, id) :
    data = Myfavoritewatchlist.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
def show_xml_by_id(request,id):
    data = Myfavoritewatchlist.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")