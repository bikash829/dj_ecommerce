from django.shortcuts import render
from django.urls import reverse

# Create your views here.
def index(request):
    context = {
        'home_page_status'   : 'active',
        'title'         : 'Admin Dashboard',
        'page'          : 'Dashboard',
        # 'page_url'      : reverse('app_name:view_name'),
    }
    return render(request, 'admin/pages/index.html', context)


# page widgets
def widgets(request):
    context = {
        'widgets_page_status'   : 'active',
        'title'         : 'Widgets',
        'page'          : 'Widgets',
        
    }
    return render(request, 'admin/pages/widgets.html', context)

# page calendar 
def calendar(request):
    context = {
        'calendar_page_status'      : 'active',
        'title'                     : 'Calendar',
        'page'                      : 'Calendar',
        
    }
    return render(request, 'admin/pages/calendar.html', context)

# =============UI Elements================
# page general 
def general(request):
    context = {
        'general_page_status'       : 'active',
        'title'                     : 'General UI',
        'page'                      : 'Inline Charts',
        'ul_menu'                   : 'menu-open',
        
    }
    return render(request, 'admin/pages/ui/general.html', context)