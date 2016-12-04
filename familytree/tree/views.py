from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.views.generic.edit import FormView
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from forms import JunkForm, UploadFileForm
from familytree.mongo import get_mongo
from .utils import save_individual
from simplepyged.gedcom import Gedcom
from bson.objectid import ObjectId
import jsonpickle

import json

class JunkView(FormView):
    template_name = 'junk.html'
    form_class = JunkForm
    success_url = '/tree/yay/'

    def form_valid(self, form):
        db = get_mongo('junk')
        db.items.insert_one({"item":form.cleaned_data['junk']})
        return super(JunkView, self).form_valid(form)

def yay(request):
    db = get_mongo('junk')
    items = db.items.find()
    return render(request, 'yay.html', {"items":items})

@login_required
def upload_gedcom(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            z = []
            for x in request.FILES['file'].chunks():
                z.extend([y for y in x.splitlines()])
            gc = Gedcom(z, chunks=True)
            indiv = [save_individual(x, request.user, True) for x in gc.individual_list()]
            return HttpResponseRedirect(reverse("list_people"))
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})

def show_gedcom(request):
    return HttpResponse("ok")

@login_required
def list_people(request):
    db = get_mongo("tree")
    return render(request, 'list_people.html', {"people":db.person.find()})

@login_required
def person_show(request, id):
    db = get_mongo("tree")
    from pprint import PrettyPrinter
    person = db.person.find_one({"_id":ObjectId(id)})
    pp=PrettyPrinter(indent=3)
    pdict = pp.pformat(person)
    return render(request, 'person_show.html', {"person":person, "pdict":pdict})
