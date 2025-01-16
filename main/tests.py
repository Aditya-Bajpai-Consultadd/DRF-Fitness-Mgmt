from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from main.models import Member
from main.serializers import MemberSerializer
from django.contrib.auth.models import User


class ViewOrAddMembersTestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='password') 
        Member.objects.create(name='Aditya Bajpai',email='aditya@gmail.com', phone="1234566788", address="Rukmani Nagar")
        Member.objects.create(name='Payal Bajpai',email='payal@gmail.com', phone= "123456", address="Anjani Nagar")

    def test_get_member(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.get('/members/')  
        members = Member.objects.all()
        serializer = MemberSerializer(members, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_post_member(self):
        self.client.force_authenticate(user=self.user)
        data = {'name': 'Sanjay Bajpai', 'email': 'sanjay@gmail.com', 'phone': '1234567890', 'address': 'Rukmani Nagar'}
        response = self.client.post('/members/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Member.objects.count(), 3)

    def test_post_member_failure(self):
        self.client.force_authenticate(user=self.user)
        data = {'name': 'Aditya Bajpai', 'email': 'aditya@gmail.com', 'phone': '1234567890', 'address': 'Rukmani Nagar'}        
        response = self.client.post('/members/', data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_invalid_authentication(self):
        response = self.client.get('/members/',)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    
        

    
        

