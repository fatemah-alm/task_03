from django.shortcuts import render

def welcome(request):
    return render(request, 'index.html', {'msg':'Hello World!'})

def restaurant_list(request):

    context = {'my_list':[{'restaurant_name':'Ashaz', 'food_type':'Persian'},{'restaurant_name':'Hardee\'s', 'food_type':'American'},{'restaurant_name':'Kabab-AlHijja', 'food_type':'Iraqi'}]

    }
    return render(request, 'list.html', context)


def restaurant_detail(request):

    context = { "my_object":{'restaurant_name':'Ubon', 'food_type':'Thai'}

    }
    return render(request, 'detail.html', context)
