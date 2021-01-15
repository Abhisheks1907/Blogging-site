from django.shortcuts import render,redirect , get_object_or_404

from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .forms import userProfileForm 
from .models import post
from django.views.generic import ListView , DetailView ,CreateView


# Create your views here.

class PostListView(ListView):
    model = post
    template_name = 'welcome.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']

class PostDetailView(DetailView):
    model = post
    template_name = 'post_detail.html'

class PostCreateView(CreateView):
    model = post
    fields = ['title','content']
    template_name = 'post/post_form.html'

    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)
        # here we created the instance of the author and set it to the current logged in user   

def profile(request):
    context={
        'user_posts':post.objects.all()
    }

    return render (request,'profile.html',context, )
  
class UserPostListView(ListView):
    model =post
    template_name = 'post/user_post.html'
    context_object_name= 'posts'
    paginate_by = 5

    def get_queryset(self):
        user =  get_object_or_404(User, username = self.kwargs.get("username"))
        return post.objects.filter(author= user).order_by('-date_posted')


def index(request):
    
    return render(request,'index.html',)

@login_required
def profile_change(request):
    if request.method == 'POST':

        u_form = userProfileForm(request.POST , request.FILES , instance=request.user.user_profile)

        if u_form.is_valid :
            u_form.save()

            messages.success(request, f'account updated')
            return redirect('profile')

    else:
        u_form = userProfileForm(instance=request.user.user_profile)
    context={
        'u_form':u_form
    }
    


    return render(request,'edit_profile.html',context)

def homep(request):
    context = {
        'posts':post.objects.all()
    }
    return render (request,'welcome.html',context)



def logout_view(request):
    logout(request)
    return render(request,'index.html')

def login_view(request):
    if request.method=='POST':
        username= request.POST.get('username')
        password = request.POST.get('password')

        user=authenticate(username=username,password=password)

        if user is not None:
            login(request,user)
            context = {
                'posts':post.objects.all()
            }
            return render(request,'welcome.html',context)

        else:
            messages.info(request , 'invalid credentials')
            return render(request,'login.html')
    else:
        return render(request,'welcome.html')
            




        
def register(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'username taken')
                return render(request,'register.html')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'email taken')
                return render(request,'register.html')
            else:
                user = User.objects.create_user(username=username,email=email,password=password1)
                user.save()

        else:
            messages.info(request,'password didint match')
            return render(request,'register.html')
        return render(request,'login.html')



    else:
        
        return render(request,'index.html')

