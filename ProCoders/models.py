from django.contrib.auth.models import User 
from django.db import models

class Languages(models.Model):
    language = models.CharField(max_length=64, unique=True)
    image = models.ImageField(upload_to='static/Supports/Language/', null=True, blank=True)
    iframe_url = models.TextField(null=True)

    def __str__(self):
        return self.language

class Information(models.Model):
    language = models.ForeignKey(Languages, on_delete=models.CASCADE, related_name='information')
    heading = models.CharField(max_length=128)
    image = models.ImageField(upload_to='static/Supports/Information/', null=True, blank=True)
    about = models.TextField()

    def __str__(self):
        return f"{self.heading} ({self.language})"

class Quiz(models.Model):
    language = models.ForeignKey(Languages, on_delete=models.CASCADE, related_name='quizzes')
    question = models.CharField(max_length=512)
    option1 = models.CharField(max_length=256)
    option2 = models.CharField(max_length=256)
    option3 = models.CharField(max_length=256)
    option4 = models.CharField(max_length=256)
    answer = models.CharField(max_length=1)
    explanation = models.CharField(max_length=512)

    def __str__(self):
        return f"Quiz in {self.language}: {self.question}"

class Room(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="created_rooms")
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name

class Message(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name="messages")
    value = models.CharField(max_length=2048)
    date = models.DateTimeField(auto_now=True)
    user = models.CharField(max_length=128)


'''class QuizRecord:
    pass
'''