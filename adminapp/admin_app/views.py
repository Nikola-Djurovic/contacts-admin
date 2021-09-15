from django.shortcuts import render
from .models import Contact, Token, Login
from .filters import OrderFilter
from django.views.generic import ListView
# Create your views here.
def homepage(request):
    contacts = Contact.objects.all()
    tokens = Token.objects.all()
    logins = Login.objects.all()
    myFilter = OrderFilter(request.GET, queryset = contacts)
    return render(request, 'homepage.html',{'total_contacts':contacts.count(),
                                            'total_tokens':tokens.count(),
                                            'total_logins':logins.count(),
                                            'users_to_contacts':contacts.count()*1.0/logins.count(),
                                            'user_sesions_to_number_of_users_ratio':logins.count()*0.1/contacts.count(),
                                            'my_filter':myFilter})

