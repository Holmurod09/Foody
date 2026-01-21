from django.shortcuts import render
from .models import Comments, Parties, Chefs, Bar_menu, Salad_menu, Additionaldishes_menu, Burger_menu, Pizza_menu, Bread_menu, Sup_menu, Fish_menu, BBQ_menu, National_dishes_menu, Kebab_menu, Sweets_menu
from django.http import Http404

def home(request):
    bars_menu = Bar_menu.objects.all()
    salads_menu = Salad_menu.objects.all()
    additionaldishes_menu = Additionaldishes_menu.objects.all()
    burgers_menu = Burger_menu.objects.all()
    pizza_menu = Pizza_menu.objects.all()
    bread_menu = Bread_menu.objects.all()
    sup_menu = Sup_menu.objects.all()
    fish_menu = Fish_menu.objects.all()
    bbq_menu = BBQ_menu.objects.all()
    national_menu = National_dishes_menu.objects.all()
    kebab_menu = Kebab_menu.objects.all()
    sweets_menu = Sweets_menu.objects.all()
    comments = Comments.objects.all()
    parties = Parties.objects.all()
    chefs = Chefs.objects.all()

    context = {
        "bars_menu":bars_menu,
        "salads_menu":salads_menu,
        "additionaldishes_menu":additionaldishes_menu,
        "burgers_menu":burgers_menu,
        "pizza_menu":pizza_menu,
        "bread_menu":bread_menu,
        "sup_menu":sup_menu,
        "fish_menu":fish_menu,
        "bbq_menu":bbq_menu,
        "national_menu":national_menu,
        "kebab_menu":kebab_menu,
        "sweets_menu":sweets_menu,
        "comments":comments,
        "parties":parties,
        "chefs":chefs,
    }
    return render(request, 'index.html', context=context)


def custom_404(request, exception):
    return render(request, "404.html", status=404)