from unicodedata import category
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render,redirect
from .models import *
import random

# Create your views here.
def home(request):
    return HttpResponse("Hello from Django")

def get_category(request):
    try:
        category_objs = list(Category.objects.all())
        data = []
        random.shuffle(category_objs)
        for category_obj in category_objs:
            data.append({
                "category" : category_obj.category_name,
            })
            payload ={'status': True, 'data' : data}

        return JsonResponse(payload)
    except Exception as e:
        print(e)
    return HttpResponse("Something went wrong!!!!")

def get_question(request):
    try:
        question_objs = list(Question.objects.all())
        data = []
        random.shuffle(question_objs)
        print(question_objs)
        for question_obj in question_objs:
            print(question_obj.get_answers())
            data.append({
                "question" : question_obj.question,
            })
        payload ={'status': True, 'data' : data}
        return JsonResponse(payload)

    except Exception as e:
        print(e)
    return HttpResponse("Something went wrong!!!!")

def get_answer(request):
    try:
        question_objs = list(Question.objects.all())
        data = []
        random.shuffle(question_objs)
        print(question_objs)
        for question_obj in question_objs:
            print(question_obj.get_answers())
            data.append({
                "answers" : question_obj.get_answers(),
            })
        payload ={'status': True, 'data' : data}

        return JsonResponse(payload)

    except Exception as e:
        print(e)
    return HttpResponse("Something went wrong!!!!")
'''
def home(request):
    context = { 'categories' : Category.objects.all()}
    if request.GET.get('category'):
        return redirect(f"/quiz/?category={request.GET.get('category')}")
    return render(request,'', context)'''

def quiz(request):
    return render(request,'')

def get_quiz(request):
    try:
        question_objs = Question.objects.all()

        if request.GET.get('category'):
            question_objs=question_objs.filter(category__category_name__icontains=request.GET.get('category'))
        question_objs = list(question_objs)

        data = []
        print(question_objs)
        for question_obj in question_objs:
            print(question_obj.get_answers())
            data.append({
                "category" : question_obj.category.category_name,
                "questionType" : question_obj.questionType.questionType,
                "question" : question_obj.question,
                "marks" : question_obj.marks,
                "answers" : question_obj.get_answers(),
            })
        payload ={'status': True, 'data' : data}

        return JsonResponse(payload)

    except Exception as e:
        print(e)
    return HttpResponse("Something went wrong!!!!")