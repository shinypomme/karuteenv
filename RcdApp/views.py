from django.shortcuts import render, redirect
from . import forms
from django.core.files.storage import FileSystemStorage
import os
from .models import PostRcd
from django.contrib import messages
from django.db.models import Q
from .forms import LoginForm
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.http import FileResponse
import csv

STORE_LIST = (
    '大須サロン',
    'SKドックラン',
    'ローズマリー岡崎店',
    'ローズマリー豊橋店',
    'Floor岡崎店',
    'クヌート土岐店',
    'その他'
)

def index(request):
    login_form = LoginForm(request.POST or None)
    if login_form.is_valid():
        username = login_form.cleaned_data.get('username')
        password = login_form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return redirect('rcdapp:form_page')
            else:
                messages.error(request, 'アカウントが有効になっていません')
        else:
            messages.error(request, 'ユーザー名かパスワードが間違っています')
    return render(request, 'rcdapp/index.html', context={
        'login_form': login_form
    })

@login_required
def form_page(request):
    form = forms.UserInfo(request.POST or None, request.FILES or None)
    if form.is_valid():
        messages.success(request, '保存しました。')
        form.save()
        form = forms.UserInfo()
    return render(request, 'rcdapp/form_page.html', context={
        'form': form
    })

@login_required
def form_list(request):
    if (request.method == 'POST'):
        form = forms.UserFind(request.POST or None)
        find = request.POST['find']
        find = find.split()
        if find:
            queries = []
            for word in find:
                store_name = ["0"]
                for ii, store in enumerate(STORE_LIST):
                    if word in store:
                        store_name.append(str(ii + 1))
                query = (Q(id__contains = word) | Q(name_orner__contains = word) | Q(name_dog__contains = word) | Q(breed_dog__contains = word) | Q(store__in = store_name) | Q(tel__contains = word))
                queries.append(query)
            rcds = PostRcd.objects.filter(*queries)
        else:
            rcds = PostRcd.objects.all()
    else:
        form = forms.UserFind()
        rcds = PostRcd.objects.all()
    return render(
        request, 'rcdapp/form_list.html', context = {
            'rcds' : rcds,
            'form': form,
        }
    )

def is_changed_data(before, after):
    is_changed = False
    if before.name_orner != after.cleaned_data['name_orner']    \
    or before.name_dog != after.cleaned_data['name_dog']        \
    or before.breed_dog != after.cleaned_data['breed_dog']      \
    or before.tel != after.cleaned_data['tel']                  \
    or before.store != after.cleaned_data['store']              \
    or after.cleaned_data['operation']                          \
    or after.cleaned_data['date_examin']                        \
    or after.cleaned_data['picture_1']                          \
    or after.cleaned_data['picture_2']                          \
    or after.cleaned_data['picture_3']                          \
    or after.cleaned_data['picture_4']                          \
    or after.cleaned_data['picture_5']:
        is_changed = True
    for i in range(1, 51):
        if before.__dict__['date_examin_' + str(i)] != after.cleaned_data['date_examin_' + str(i)] \
        or before.__dict__['operation_' + str(i)] != after.cleaned_data['operation_' + str(i)]:
            is_changed = True
    return is_changed

def make_form_initial(rcd):
    initial = {
        'name_orner':rcd.name_orner,
        'name_dog':rcd.name_dog,
        'breed_dog':rcd.breed_dog,
        'store':rcd.store,
        'tel':rcd.tel,
        'picture_1':rcd.picture_1,
        'picture_2':rcd.picture_2,
        'picture_3':rcd.picture_3,
        'picture_4':rcd.picture_4,
        'picture_5':rcd.picture_5
    }
    for i in range(1, 51):
        initial[f'date_examin_{i}'] = rcd.__dict__['date_examin_' + str(i)]
        initial[f'operation_{i}'] = rcd.__dict__['operation_' + str(i)]
    return initial

def update_record(rcd):
    over_record = False
    if rcd.date_examin or rcd.operation:
        if rcd.record_no < 49:
            rcd.record_no += 1
            rcd.__dict__['date_examin_' + str(rcd.record_no + 1)] = rcd.date_examin
            rcd.__dict__['operation_' + str(rcd.record_no + 1)] = rcd.operation
        else:
            over_record = True
    
    return rcd, over_record

@login_required
def form_update(request, id):
    rcd = PostRcd.objects.get(id=id)    
    initial = make_form_initial(rcd)
    update_form = forms.UserInfo(initial)
    if request.method == 'POST':
        update_form = forms.UserInfo(request.POST or None, request.FILES or None)
        if update_form.is_valid():
            changed_data = is_changed_data(rcd, update_form)
            rcd.name_orner = update_form.cleaned_data['name_orner']
            rcd.name_dog = update_form.cleaned_data['name_dog']
            rcd.breed_dog = update_form.cleaned_data['breed_dog']
            rcd.store = update_form.cleaned_data['store']
            rcd.tel = update_form.cleaned_data['tel']
            rcd.date_examin = update_form.cleaned_data['date_examin']
            rcd.operation = update_form.cleaned_data['operation']
            for i in range(1, 50):
                rcd.__dict__['date_examin_' + str(i)] = update_form.cleaned_data[f'date_examin_{i}']
                rcd.__dict__['operation_' + str(i)] = update_form.cleaned_data[f'operation_{i}']
            pictures = [
                update_form.cleaned_data['picture_1'], 
                update_form.cleaned_data['picture_2'], 
                update_form.cleaned_data['picture_3'], 
                update_form.cleaned_data['picture_4'], 
                update_form.cleaned_data['picture_5']
            ]
            for i, picture in enumerate(pictures):
                if picture:
                    rcd.__dict__['picture_' + str(i + 1)] = picture
                    fs = FileSystemStorage()
                    file_name = fs.save(os.path.join('rcd', picture.name), picture)
                    rcd.__dict__['picture_' + str(i + 1)] = file_name
            rcd, over_record = update_record(rcd)
            if over_record:
                messages.error(request, '「過去の受診内容」の更新が上限の50回に到達しているのでカルテを更新できません。新しくカルテを作り直してください。')
            else:
                if changed_data:
                    messages.success(request, '更新しました。')
                    rcd.save()
                else:
                    messages.error(request, 'データが変更されていません。')
        else:
            messages.error(request, 'データが変更されていません。')
    return render(request, 'rcdapp/form_update.html', context = {
            'update_form' : update_form,
            'rcd':rcd,
            'end_loop': int(rcd.record_no + 1)*2,
        })

@login_required
def delete_user(request, id):
    rcd = PostRcd.objects.get(id=id)
    delete_form = forms.UserDelete(
        initial = {
            'id':id
        }
    )
    delete_value = {
        "id" : str(id),
        "name_orner" : str(rcd.name_orner),
        "name_dog" : str(rcd.name_dog),
        "breed_dog" : str(rcd.breed_dog),
        "tel" : str(rcd.tel),
        "store" : STORE_LIST[int(rcd.store)]
    }
    if request.method == 'POST':
        delete_form = forms.UserDelete(request.POST or None)
        if delete_form.is_valid():
            PostRcd.objects.get(id=delete_form.cleaned_data['id']).delete()
            messages.success(request, '削除しました。')
    return render(
        request, 'rcdapp/delete_user.html', context={
            'delete_value': delete_value,
            'delete_form': delete_form
        }
    )

@login_required
def user_logout(request):
    logout(request)
    return redirect('rcdapp:index')

def pandas_csv():
    from django_pandas.io import read_frame

    query = PostRcd.objects.all()
    df = read_frame(query)
    response = HttpResponse(content_type='text/csv; charset=utf8')
    response['Content-Disposition'] = 'attachment; backup.csv'
    df.to_csv(path_or_buf=response, encoding='utf_8_sig', index=None)

    return response

@login_required
def backup(request):
    if request.method == "POST":
        response = pandas_csv()
        return response
    
    return render(request, 'rcdapp/backup.html', context={
    })