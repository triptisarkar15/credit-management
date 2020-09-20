from django.shortcuts import render
from django.http import HttpResponseRedirect
from cal.models import Users, Transactions
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView

def home(request):
    return render(request, 'home.html')

def userinfo(request):
    data= Users.objects.all().order_by("id")
    return render(request, 'users.html',{"ppl": data})


class UserDetail(DetailView):
    model=Users
    template_name="details.html"
    def get_context_data(self, **kwargs):
        context = DetailView.get_context_data(self, **kwargs)
        context["user"]=Users.objects.get(id=self.kwargs["pk"])
        context["transaction"]=Transactions.objects.filter(WhomUsers=self.kwargs["pk"])
        return context

class Transaction(TemplateView):
    template_name="transactions.html"
    
    def get_context_data(self, **kwargs):        
        context = TemplateView.get_context_data(self, **kwargs)
        context["user"]=Users.objects.get(id=self.kwargs["pk"])
        context["pple"]=Users.objects.exclude(id=self.kwargs["pk"]).order_by("id")        
        return context

    def post(self, request, *args, **kwargs):
        Amount = request.POST["Amount"]
        users = request.POST["users"]
        users=Users.objects.get(Name= users)
        trans=Transactions.objects.create(Amount= Amount, WhomUsers=Users.objects.get(id=self.kwargs["pk"]),WhoUsers=users, Status="Credit")
        trans.save()
        who=Users.objects.get(id= self.kwargs["pk"])
        who.Credit=who.Credit-int(Amount)
        who.save()
        users.Credit=users.Credit+int(Amount)
        users.save()
        return HttpResponseRedirect('/users/details/' + str(self.kwargs['pk']))

