from ast import Try
from django.shortcuts import render
from rango.models import Category
from django.shortcuts import render
from django.http import HttpResponse
from rango.models import Page


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
 
 



 
