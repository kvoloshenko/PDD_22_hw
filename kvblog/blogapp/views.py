from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from blogapp.models import Hh_Response, Hh_Request
from blogapp.forms import Hh_Search_Form
from django.urls import reverse
import hhru.all_data as ad
import pprint

# Create your views here.
def main_view(request):
    requests = Hh_Request.objects.all()
    return render(request, 'blogapp/index.html', context={'requests': requests})

def history(request):
    # обратная сортировка
    requests = Hh_Request.objects.order_by('id').reverse()
    responses = Hh_Response.objects.all()
    return render(request, 'blogapp/history.html', context={'requests': requests, 'responses': responses})


def create_result(request, id):
    # hh_request = Hh_Request.objects.last()
    hh_request = get_object_or_404(Hh_Request, id=id)
    responses = Hh_Response.objects.filter(request = hh_request)
    return render(request, 'blogapp/result.html', context={'hh_request': hh_request, 'responses': responses})

def create_form(request):
    form = Hh_Search_Form(request.POST)
    if form.is_valid():
        # Получить данные из форы
        hh_query = form.cleaned_data['hh_query']
        # обработка полученных данных
        print(type(hh_query),f' hh_query = {hh_query}')
        ad.set_keywords(hh_query)
        result = ad.get_data(hh_query)
        # print(type(result))
        # print(type(result[0]['requirements']))
        # pprint.pprint(result)
        keywords = result[0]['keywords']
        # print(f'keywords={keywords}')
        Hh_Request.objects.create(keywords = keywords)
        last_request = Hh_Request.objects.last()
        # print(f'last_request.id = {last_request.id}')

        requirements_l = result[0]['requirements']
        # print(type(requirements_l), f'requirements_l={requirements_l}')
        for item in requirements_l:
            # print(f'item={item}')
            # print(f'{item["name"]} {item["count"]} {round(int(item["persent"]))}')
            Hh_Response.objects.create(request=last_request,
                                       skill_name=item["name"],
                                       skill_count=item["count"],
                                       skill_persent=round(int(item["persent"])))
        #  подготовка для отображения на странице result.html
        hh_request = get_object_or_404(Hh_Request, id=last_request.id)
        responses = Hh_Response.objects.filter(request=hh_request)
        return render(request, 'blogapp/result.html', context={'hh_request': hh_request, 'responses': responses})
    else:
        return render(request, 'blogapp/form.html', context={'form': form})

    return render(request, 'blogapp/form.html', context={'form':form})


def create_contacts(request):
    dev_name = 'Konstantin Voloshenko'
    creation_date = 'Июнь 2022'
    return render(request, 'blogapp/contacts.html', context={'dev_name': dev_name, 'creation_date': creation_date})

