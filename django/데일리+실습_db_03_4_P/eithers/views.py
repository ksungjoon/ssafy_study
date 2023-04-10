from django.shortcuts import render, redirect, get_object_or_404

from .models import Question,Comment
from .forms import QuestionForm, CommentForm

def index(request):
    questions = Question.objects.order_by('-pk')
    context = {
        'questions': questions,
    }
    return render(request, 'eithers/index.html', context)


def create(request):
    if request.method == 'POST':
        question_form = QuestionForm(request.POST)
        if question_form.is_valid():
            question = question_form.save()
            return redirect('eithers:index')
    else:
        question_form = QuestionForm()
    context = {
        'question_form': question_form,
    }
    return render(request, 'eithers/create.html', context)


def detail(request, question_pk):
    question = get_object_or_404(Question, pk=question_pk)

    comment_form = CommentForm()
    context = {
        'question': question,
        'comment_form': comment_form,
    }
    return render(request, 'eithers/detail.html', context)


def random(request):
    import random

    pk_list = []
    for value in Question.objects.values('pk'):
        pk_list.append(value['pk'])
    random_pk=random.choice(pk_list)
    
    return redirect('eithers:detail', random_pk)


def comment_create(request, question_pk):
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.question_id = question_pk
            comment.save()
    return redirect('eithers:detail', question_pk)

def update(request, question_pk):
    quesiton = Question.objects.get(pk=question_pk)

    if request.method =='POST':
        form = QuestionForm(request.POST, request.FILES, instance=quesiton)
        if form.is_valid():
            form.save()
            return redirect('eithers:detail',question_pk)
    else:
        form = QuestionForm(instance=quesiton)
        
        context = {'form':form, 'question':quesiton}
        return render(request, 'eithers/update.html',context)
    

def delete(request, question_pk):
    question = Question.objects.get(pk=question_pk)
    question.delete()
    return redirect('eithers:index')

def comment_delete(request, question_pk,comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    comment.delete()
    return redirect('eithers:detail',question_pk)