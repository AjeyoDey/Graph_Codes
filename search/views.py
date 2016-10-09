from django.shortcuts import *
from .forms import InternForm
from find import *
from api import  *
# Create your views here.

def index(request):
    form = InternForm(request.POST or None)
    f = {'form':form}
    if request.method != 'POST':
        form = InternForm()
        return render(request,'search/index.html',{'form':form})
    try:
        form = InternForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            college = data['college']
            area = data['area']
            tmp= correctexp(area)
            proff_data= get_data("http://ee.iitd.ernet.in/people/faculty.html",tmp)
            return render(request,'search/index.html',{'proff_data':proff_data,'form':form,'c':True})
    except Exception as E:
        return render(request,'search/index.html',{'error':True,'error_value':E})
    return render(request,'search/index.html',f)