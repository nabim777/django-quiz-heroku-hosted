from django.db import models
import uuid
import random
# Create your models here.
class BaseModel(models.Model):
    uid = models.UUIDField(primary_key = True, default = uuid.uuid4,editable = False)
    created_at = models.DateField(auto_now_add = True)
    updated_at = models.DateField(auto_now = True)
    class Meta:
        abstract = True
    

class Category(BaseModel):
    category_name = models.CharField(max_length=100)
    def __str__(self):
        return self.category_name

class Questiontype(models.Model):
    questionType = models.CharField(max_length=100, unique=True)
    id_parent = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return self.questionType

class Question(BaseModel):
    category = models.ForeignKey(Category, related_name= 'category',on_delete=models.CASCADE)
    questionType = models.ForeignKey(Questiontype,related_name= 'subcategory', on_delete=models.SET_NULL, null=True)
    question = models.CharField(max_length=100)
    marks = models.IntegerField(default=1)

    def __str__(self):
        return self.question

    def get_answers(self):
        answer_objs = list(Answer.objects.filter(question = self))
        random.shuffle(answer_objs)
        data = []
        for answer_obj in answer_objs:
            data.append({
                'answer' : answer_obj.answer,
                'is_correct': answer_obj.is_correct                
            })
        return data

class Answer(BaseModel):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.CharField(max_length = 100)
    is_correct = models.BooleanField(default = False)
    def __str__(self):
        return self.answer