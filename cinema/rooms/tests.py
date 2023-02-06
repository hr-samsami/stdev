from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from .models import Room
from .serializer import RoomSerializer


class RoomTests(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.room_data = {'name': 'Room 1', 'rows': 10, 'seats_per_row': 10}
        self.response = self.client.post(
            reverse('room-list'),
            self.room_data,
            format='json'
        )

    def test_create_valid_room(self):
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Room.objects.count(), 1)
        self.assertEqual(Room.objects.get().name, 'Room 1')

    def test_get_rooms(self):
        response = self.client.get(reverse('room-list'))
        rooms = Room.objects.all()
        serializer = RoomSerializer(rooms, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_valid_single_room(self):
        room = Room.objects.create(**self.room_data)
        response = self.client.get(
            reverse('room-detail', kwargs={'pk': room.pk})
        )
        serializer = RoomSerializer(room)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_single_room(self):
        response = self.client.get(reverse('room-detail', kwargs={'pk': 30}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_update_valid_room(self):
        room = Room.objects.create(**self.room_data)
        response = self.client.put(
            reverse('room-detail', kwargs={'pk': room.pk}),
            {'name': 'Room 2'}
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_invalid_room(self):
        response = self.client.put(
            reverse('room-detail', kwargs={'pk': 30}),
            {'name': 'Room 2'}
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_delete_valid_room(self):
        room = Room.objects.create(**self.room_data)
        response = self.client.delete(
            reverse('room-detail', kwargs={'pk': room.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        with self.assertRaises(Room.DoesNotExist):
            Room.objects.get(pk=room.pk)

