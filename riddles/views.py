from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, render

from .models import Riddle, Option, Answers


def toFixed(numObj, digits=0):
    return f"{numObj:.{digits}f}"


def right_answers(id):
    tmp = Option.objects.all().filter(riddle=id, correct='1')
    array_of_right_answers = []
    for i in tmp:
        array_of_right_answers.append(str(i.id))
    return array_of_right_answers

def results(request):
    #dic = {}
    lis = []
    for i in Riddle.objects.all():
        ra = right_answers(i)
        answers = Answers.objects.all().filter(riddle_id = i)
        bad_anwers = 0
        for j in answers:
            if not(str(j.answers) == str(ra)):
                bad_anwers += 1
        if bad_anwers > 0:
            percent_wrong_answers = toFixed(100*(bad_anwers/answers.count()),1)
            #dic[i.riddle_text] = percent_wrong_answers
        #else:
            #dic[i.riddle_text] = 0

        if (float(percent_wrong_answers) > 50):
            lis.append([i.riddle_text, percent_wrong_answers, 1])
        else:
            lis.append([i.riddle_text, percent_wrong_answers, 0])
        #print(lis)
        #print('Вопрос - ' + i.riddle_text + '  Всего ответов -  ' + str(answers.count()) + '  неправильных ответов  -'+ str(bad_anwers))
    return render(request, "results.html", {"results" : lis})


def index(request):
    return render(request, "index.html", {"latest_riddles": Riddle.objects.order_by('-pub_date')[:5]})


def detail(request, riddle_id):
    return render(request, "answer.html", {"riddle": get_object_or_404(Riddle, pk=riddle_id)})


def answer(request, riddle_id):
    riddle = get_object_or_404(Riddle, pk=riddle_id)
    answ = Answers(riddle = riddle, answers = request.POST.getlist ('option'), ip = request.META.get('REMOTE_ADDR'))
    answ.save()
    try:
        option = riddle.option_set.get(pk=request.POST['option'])
    except (KeyError, Option.DoesNotExist):
        return render(request, 'answer.html', {'riddle': riddle, 'error_message': 'Option does not exist'})
    else:
        try:
            rid = Riddle.objects.get(pk=str(int(riddle_id) + 1))
        except Riddle.DoesNotExist:

            return render(request, 'end.html', {'riddle': riddle, 'error_message': 'Опрос окончен'})
        return render(request, 'answer.html', {'riddle': rid, 'error_message': ''})
