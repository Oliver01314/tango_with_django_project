from ast import Try
from django.shortcuts import render
from rango.models import Category
from django.shortcuts import render
from django.http import HttpResponse
from rango.models import Page
from rango.forms import CategoryForm
from django.shortcuts import redirect
from rango.forms import PageForm
from django.urls import reverse

def index(request):

 # Construct a dictionary to pass to the template engine as its context.
 #  Note the key boldmessage matches to {{ boldmessage }} in the template!
#  order the categories by the number of likes in descending order
# retrieve the top 5 only
#  query the database for a list of all categories currently stored
    category_list = Category.objects.order_by('-likes')[:5]
#  add page list
    page_list = Page.objects.order_by('-views')[:5]
    context_dict = {}
 
#  not sure if  i need to add these two 
    context_dict = {'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!'}
    context_dict['categories'] = category_list
    context_dict['pages'] = page_list
    return render(request, 'rango/index.html', context=context_dict)

# add more parameters 
def show_category(request, category_name_slug):
    context_dict = {}

    try:
        category = Category.objects.get(slug=category_name_slug)
        pages = Page.objects.filter(category=category)
        context_dict['pages'] = pages
        context_dict['category'] = category
    except Category.DoesNotExist:
        context_dict['category'] = None
        context_dict['pages']= None
    return render(request, 'rango/category.html', context=context_dict)



def about(request):
    context_dict = {'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!'}

    return render(request, 'rango/about.html', context=context_dict)
 
 

def add_category(request):

    form = CategoryForm()
    
    # A HTTP POST?
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        # Have we been provided with a valid form?
        if form.is_valid():
            # Save the new category to the database. 
            form.save(commit=True)
            # Now that the category is saved, we could confirm this. 
            # For now, just redirect the user back to the index view. 
            return redirect('/rango/')
        else:
            # The supplied form contained errors -
            print(form.errors)

    return render(request, 'rango/add_category.html', {'form': form})

 
def add_page(request, category_name_slug):
    try:
        category = Category.objects.get(slug=category_name_slug) 
    except Category.DoesNotExist:
        category = None

     # You cannot add a page to a Category that does not exist...
    if category is None:
        return redirect('/rango/')

    
    form = PageForm()

    if request.method == 'POST':
        form = PageForm(request.POST)

        if form.is_valid(): 
            if category:
                page = form.save(commit=False)
                page.category = category
                page.views = 0
                page.save()

                return redirect(reverse('rango:show_category',
                                        kwargs={'category_name_slug': 
                                                category_name_slug}))

        else: 
            print(form.errors)
    

    context_dict = {'form': form, 'category': category}
    return render(request, 'rango/add_page.html', context=context_dict)