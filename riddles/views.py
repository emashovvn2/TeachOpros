from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, render

from .models import Riddle, Option, Answers


def index(request):
    return render(request, "index.html", {"latest_riddles": Riddle.objects.order_by('-pub_date')[:5]})


def detail(request, riddle_id):
    return render(request, "answer.html", {"riddle": get_object_or_404(Riddle, pk=riddle_id)})


def answer(request, riddle_id):
    riddle = get_object_or_404(Riddle, pk=riddle_id)
    print(request.META.get('REMOTE_ADDR'))
    for q in request.POST.getlist ('option'):
        print(q)
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
