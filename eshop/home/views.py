from django.shortcuts import render

from django.views import View


class HomeView(View):
    """ Serve home page """
    def get(self, request):
        return render(request, 'home/home.html')
