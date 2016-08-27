from forms import LoginForm 
from django.http import HttpResponse
from django.views.generic.edit import FormView
from django.contrib.auth.decorators import login_required
from django.urls import reverse

# Create your views here.

@login_required(login_url="login/")
def home(request):
    return HttpResponse("Hello you are loged in"+str(request.user.is_authenticated()))

class LoginView(FormView):

    template_name = "plutus_core/login.html"
    form_class = LoginForm

    def get_form_kwargs(self):
        kwargs = super(LoginView, self).get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs

    def form_valid(self, form):
        return super(LoginView, self).form_valid(form)

    def get_success_url(self):
        return reverse('home')
