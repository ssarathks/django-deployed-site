from django.shortcuts import render
from second_app.models import UserProfileInfo,School,Student
from second_app.forms import UserForm,UserProfileInfoForm


from django.http import HttpResponseRedirect,HttpResponse
from django.core.urlresolvers import reverse,reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.views.generic import View,TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView
# Create your views here.

def index(request):
    return render(request,'second_app/index.html')

def registration_view(request):
        registered = False
        if request.method == 'POST':
                user_form = UserForm(data=request.POST)
                user_profile_info_form = UserProfileInfoForm(data=request.POST)
                if user_form.is_valid() and user_profile_info_form.is_valid():
                        user = user_form.save()
                        user.set_password(user.password)
                        user.save()

                        profile = user_profile_info_form.save(commit=False)
                        profile.user = user
                        if 'profile_pic' in request.FILES:
                                profile.profile_pic = request.FILES['profile_pic']
                        profile.save()
                        registered =True
                        return index(request)
        else:
                user_form = UserForm()
                user_profile_info_form = UserProfileInfoForm()
        return render(request,'second_app/registration.html',{'user_form':user_form,
                                                                'user_profile_info_form':user_profile_info_form,
                                                                'registered':registered})

def user_login(request):
        if request.method == 'POST':
                email = request.POST.get('email')
                password = request.POST.get('password')

                user = authenticate(username=email, password=password)
                if user:
                        if user.is_active:
                                login(request,user)
                                return HttpResponseRedirect(reverse('index'))
                        else:
                                return HttpResponse('Account not active')
                else:
                        return HttpResponse('invalid credentials')
        else:
                return render(request,'second_app/login.html')
        return render(request,'second_app/login.html')

@login_required
def user_logout(request):
        logout(request)
        return HttpResponseRedirect(reverse('index'))


        return render(request,'second_app/login.html')


class CBView(View):
        def get(self,request):
                return HttpResponse("This is the class based view page")

class TemplatePageView(TemplateView):
        template_name = 'second_app/template_view_test.html'
        
        def get_context_data(self,**kwargs):
                context = super().get_context_data(**kwargs)
                context['inject_me'] = "Injected Content for Template view page"
                return context

class SchoolListView(ListView):
        model = School
        template_name = 'second_app/school_list_page.html'

class SchoolDetailView(DetailView):
        model = School
        template_name = 'second_app/school_detail.html'
        context_object_name = 'school_detail'

class SchoolCreateView(CreateView):
        model =School
        fields = ('name','principal','location')

class StudentCreateView(CreateView):
        model =Student
        fields = ('name','age','school')
class SchoolUpdateView(UpdateView):
        model = School
        fields = ('name','principal')

class SchoolDeleteView(DeleteView):
        model = School
        success_url = reverse_lazy('second_app:school_list_view')