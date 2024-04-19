from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView,DeleteView, FormView
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .models import JobApplication
from .api import get_random_fact,get_weather,get_currency_conversion

    
def random_fact_view(request):
    fact = get_random_fact()
    city = request.GET.get('city','Dublin')  # Default city
    weather_data = get_weather(city)
    conversion_data = None
    if request.method == 'POST':
        source_currency = request.POST.get('source_currency', '')
        amount = request.POST.get('amount', '')
        target_currency = request.POST.get('target_currency', '')
        conversion_data = get_currency_conversion(source_currency, amount, target_currency)

    return render(request, 'random_fact.html', {'fact': fact, 'weather_data': weather_data, 'conversion_data': conversion_data})

class CustomLoginView(LoginView):
    template_name='jobapplication/login.html'
    fields='__all__'
    redirect_authenticated_user=True
    
    def get_success_url(self):
        return reverse_lazy('applications' )
        
class RegisterPage(FormView):
    template_name='jobapplication/register.html'
    form_class= UserCreationForm
    redirect_authenticated_user=True
    success_url=reverse_lazy('applications')
    
    def form_valid(self, form):
        user=form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)
        
    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('applications')
        return super(RegisterPage, self).get(*args, **kwargs)

class ApplicationList(LoginRequiredMixin, ListView):
    model = JobApplication
    context_object_name='jobapplications'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['jobapplications'] = context['jobapplications'].filter(user=self.request.user)
        
        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context['jobapplications'] = context['jobapplications'].filter(job_title__icontains=search_input)
            
        context['search-input'] = search_input
        return context
    
    
class ApplicationDetail(LoginRequiredMixin, DetailView):
    model=JobApplication
    context_object_name='jobapplication'
    
class ApplicationCreate(LoginRequiredMixin, CreateView):
    model=JobApplication
    fields = {'job_title','company', 'application_date','status','referral','people'}
    success_url=reverse_lazy('applications')
    
    def form_invalid(self, form):
        form.instance.user = self.request.user
        return super(ApplicationCreate, self).form_valid(form)
    
class ApplicationUpdate(LoginRequiredMixin, UpdateView):
    model=JobApplication
    fields = {'job_title','company', 'application_date','status','referral','people'}
    success_url=reverse_lazy('applications')
    
class ApplicationDelete(LoginRequiredMixin, DeleteView):
    model=JobApplication
    fields = '__all__'
    success_url=reverse_lazy('applications')
    
