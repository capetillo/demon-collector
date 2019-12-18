from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
import uuid
import boto3
from .models import Demon, Sin, Photo
from .forms import SoulForm
# Create your views here.

class DemonCreate(LoginRequiredMixin, CreateView):
    model = Demon
    fields = ['name', 'classification', 'description', 'age']

    def form_valid(self, form):
      form.instance.user = self.request.user
      return super().form_valid(form)

class DemonUpdate(LoginRequiredMixin, UpdateView):
    model = Demon
    fields = ['classification', 'description', 'age', 'sins']

class DemonDelete(LoginRequiredMixin, DeleteView):
    model = Demon
    success_url = '/demons/'

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

@login_required
def demons_index(request):
  demons = Demon.objects.filter(user=request.user)
  return render(request, 'demons/index.html', { 'demons': demons })

@login_required
def demons_detail(request, demon_id):
  demon = Demon.objects.get(id=demon_id)
  sins_demon_doesnt_have = Sin.objects.exclude(id__in = demon.sins.all().values_list('id'))
  soul_form = SoulForm()
  return render(request, 'demons/detail.html', { 
      'demon': demon, 
      'soul_form': soul_form,
      'sins': sins_demon_doesnt_have
    })

@login_required
def add_soul(request, demon_id):
  form = SoulForm(request.POST)
  if form.is_valid():
    new_soul = form.save(commit=False)
    new_soul.demon_id = demon_id
    new_soul.save()
  return redirect('detail', demon_id=demon_id)

@login_required
def assoc_sin(request, demon_id, sin_id):
  demon = Demon.objects.get(id=demon_id)
  demon.sins.add(sin_id)
  return redirect(demon)

@login_required
def unassoc_sin(request, demon_id, sin_id):
  Demon.objects.get(id=demon_id).sins.remove(sin_id)
  return redirect('detail', demon_id=demon_id)

class SinList(LoginRequiredMixin, ListView):
  model = Sin

class SinDetail(LoginRequiredMixin, DetailView):
  model = Sin

class SinCreate(LoginRequiredMixin, CreateView):
  model = Sin
  fields = '__all__'

class SinUpdate(LoginRequiredMixin, UpdateView):
  model = Sin
  fields = ['level']

class SinDelete(LoginRequiredMixin, DeleteView):
  model = Sin
  success_url = '/sins/'

@login_required
def add_photo(request, demon_id):
  S3_BASE_URL = 'https://s3-us-west-1.amazonaws.com/'
  BUCKET = 'demoncollector'
  photo_file = request.FILES.get('photo-file', None)
  if photo_file:
    s3 = boto3.client('s3')
    key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):] 
    try:
      s3.upload_fileobj(photo_file, BUCKET, key)
      url = f"{S3_BASE_URL}{BUCKET}/{key}"
      photo = Photo(url=url, demon_id=demon_id)
      photo.save()
    except:
      print('An error occurred uploading file to S3')
  return redirect('detail', demon_id=demon_id)

def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = { 'form': form, 'error_message': error_message }
  return render(request, 'registration/signup.html', context)