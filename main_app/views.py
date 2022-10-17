from django.shortcuts import render, redirect
from django.views import View
from django.views.generic.base import TemplateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.urls import reverse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
from .models import Book, Favorite
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
# Create your views here.


class Home(TemplateView):
    template_name = "home.html"

       
class Booklist(TemplateView): 
    template_name = "booklist.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        title = self.request.GET.get("title")

        if title != None:
            context["books"] = Book.objects.filter() # 
            context["header"] = f"Searching for {title}"
        else:
            context["books"] = Book.objects.all()
            context["header"] = f"Search"
            
        return context

class Bookdetails(DetailView):
    model = Book
    template_name = "bookdetails.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['favorites'] = Favorite.objects.all()
        return context

@method_decorator(login_required, name='dispatch') 


class FavoritesListAssoc(View):

    def get(self, request, pk, book_pk):
        assoc = request.GET.get("assoc")

        if assoc == "remove":
            Favorite.objects.get(pk=pk).books.remove(book_pk)
        
        if assoc == "add":
            Favorite.objects.get(pk=pk).books.add(book_pk)
        
        return redirect('booklist')

class BookCreate(CreateView):
    model = Book
    fields = ['img', 'title', 'author', 'description']
    template_name = "book_create.html"
    success_url = "/books/"

    def get_success_url(self):
        return reverse('bookdetails', kwargs={'pk': self.object.pk})

class BookUpdate(UpdateView):
    model = Book
    fields = ['img', 'title', 'author', 'description']
    template_name = "book_update.html"
    success_url = "/books/"

    def get_success_url(self):
        return reverse('bookdetails', kwargs={'pk': self.object.pk})

class BookDelete(DeleteView):
    model = Book
    template_name = "book_delete.html"
    success_url = "/books/"



class Signup(TemplateView):
    # show a form to fill out
    def get(self, request):
        form = UserCreationForm()
        context = {"form": form}
        return render(request, "registration/signup.html", context)
    # on form submit, validate the form and login the user.
    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("favorites")
        else:
            context = {"form": form}
            return render(request, "registration/signup.html", context)
