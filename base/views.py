from django.shortcuts import render
from django.views import View

from base.models import Room, Chat

class DashboardView(View):
    def get(self, request):
        return render(request, 'main/index.html')

class RoomsView(View):
    def get(self, request):
        rooms = Room.objects.all()
        context = {
            'rooms':rooms
        }
        return render(request, 'main/rooms.html', context)

class RoomDetailView(View):
    def get(self, request, slug):
        room = Room.objects.get(slug=slug)
        chat_messages = Chat.objects.filter(room=room)[0:25]
        context = {
            'room':room,
            'chat_messages':chat_messages
        }
        return render(request, 'main/room.html', context)
