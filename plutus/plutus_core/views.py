from forms import LoginForm 
from django.http import HttpResponse
from django.views.generic.edit import FormView
from django.views.generic import TemplateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.urls import reverse

# Create your views here.
class HomeView(TemplateView):

    template_name = "plutus_core/home.html"

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(HomeView, self).dispatch(*args, **kwargs)


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
