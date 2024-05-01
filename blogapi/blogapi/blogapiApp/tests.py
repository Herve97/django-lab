from django.test import TestCase
import requests

request = requests.get("http://localhost:8000")

print(request.json())
