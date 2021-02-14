from django.shortcuts import render
from .models import Board

def discussions(request):
    boards = Board.objects.all()

    return render(request, 'community.html', {'boards': boards})