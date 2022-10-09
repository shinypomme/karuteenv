from django import forms
from .models import PostRcd
from django.core import validators
from bootstrap_datepicker_plus.widgets import DatePickerInput
from django.contrib.auth.models import User
from .models import Profile

MAX_RECORD_NO = 3

STORE_CHOISE = (
    ("1", '大須サロン'),
    ("2", 'SKドックラン'),
    ("3", 'ローズマリー岡崎店'),
    ("4", 'ローズマリー豊橋店'),
    ("5", 'Floor岡崎店'),
    ("6", 'クヌート土岐店'),
    ("7", 'その他')
)

class UserInfo(forms.ModelForm):
    name_orner = forms.CharField(label='飼い主の名前', widget=forms.TextInput(attrs={'class': 'cls_form'}))
    name_dog = forms.CharField(label='ワンちゃんの名前', widget=forms.TextInput(attrs={'class': 'cls_form'}))
    store = forms.ChoiceField(label='店', choices=STORE_CHOISE, widget=forms.RadioSelect(attrs={'class': 'cls_choice'}))
    mail = forms.EmailField(label='メール', required=False, widget=forms.TextInput(attrs={'class': 'cls_form'}))
    tel = forms.CharField(label='電話番号', required=False, widget=forms.TextInput(attrs={'class': 'cls_form'}))

    record_no = forms.IntegerField(required=False)

    date_examin = forms.DateField(label='受診日', required=False, widget=DatePickerInput(format='%Y-%m-%d'))
    operation = forms.CharField(label='受診内容', required=False, widget=forms.Textarea(attrs={'class': 'cls_form_past'}))

    date_examin_1 = forms.DateField(label='受診日', required=False, widget=DatePickerInput(format='%Y-%m-%d'))
    operation_1 = forms.CharField(label='受診内容', required=False, widget=forms.Textarea(attrs={'class': 'cls_form_past'}))

    date_examin_2 = forms.DateField(label='受診日', required=False, widget=DatePickerInput(format='%Y-%m-%d'))
    operation_2 = forms.CharField(label='受診内容', required=False, widget=forms.Textarea(attrs={'class': 'cls_form_past'}))

    date_examin_3 = forms.DateField(label='受診日', required=False, widget=DatePickerInput(format='%Y-%m-%d'))
    operation_3 = forms.CharField(label='受診内容', required=False, widget=forms.Textarea(attrs={'class': 'cls_form_past'}))

    date_examin_4 = forms.DateField(label='受診日', required=False, widget=DatePickerInput(format='%Y-%m-%d'))
    operation_4 = forms.CharField(label='受診内容', required=False, widget=forms.Textarea(attrs={'class': 'cls_form_past'}))

    date_examin_5 = forms.DateField(label='受診日', required=False, widget=DatePickerInput(format='%Y-%m-%d'))
    operation_5 = forms.CharField(label='受診内容', required=False, widget=forms.Textarea(attrs={'class': 'cls_form_past'}))

    date_examin_6 = forms.DateField(label='受診日', required=False, widget=DatePickerInput(format='%Y-%m-%d'))
    operation_6 = forms.CharField(label='受診内容', required=False, widget=forms.Textarea(attrs={'class': 'cls_form_past'}))

    date_examin_7 = forms.DateField(label='受診日', required=False, widget=DatePickerInput(format='%Y-%m-%d'))
    operation_7 = forms.CharField(label='受診内容', required=False, widget=forms.Textarea(attrs={'class': 'cls_form_past'}))

    date_examin_8 = forms.DateField(label='受診日', required=False, widget=DatePickerInput(format='%Y-%m-%d'))
    operation_8 = forms.CharField(label='受診内容', required=False, widget=forms.Textarea(attrs={'class': 'cls_form_past'}))

    date_examin_9 = forms.DateField(label='受診日', required=False, widget=DatePickerInput(format='%Y-%m-%d'))
    operation_9 = forms.CharField(label='受診内容', required=False, widget=forms.Textarea(attrs={'class': 'cls_form_past'}))

    date_examin_10 = forms.DateField(label='受診日', required=False, widget=DatePickerInput(format='%Y-%m-%d'))
    operation_10 = forms.CharField(label='受診内容', required=False, widget=forms.Textarea(attrs={'class': 'cls_form_past'}))

    date_examin_11 = forms.DateField(label='受診日', required=False, widget=DatePickerInput(format='%Y-%m-%d'))
    operation_11 = forms.CharField(label='受診内容', required=False, widget=forms.Textarea(attrs={'class': 'cls_form_past'}))

    date_examin_12 = forms.DateField(label='受診日', required=False, widget=DatePickerInput(format='%Y-%m-%d'))
    operation_12 = forms.CharField(label='受診内容', required=False, widget=forms.Textarea(attrs={'class': 'cls_form_past'}))

    date_examin_13 = forms.DateField(label='受診日', required=False, widget=DatePickerInput(format='%Y-%m-%d'))
    operation_13 = forms.CharField(label='受診内容', required=False, widget=forms.Textarea(attrs={'class': 'cls_form_past'}))

    date_examin_14 = forms.DateField(label='受診日', required=False, widget=DatePickerInput(format='%Y-%m-%d'))
    operation_14 = forms.CharField(label='受診内容', required=False, widget=forms.Textarea(attrs={'class': 'cls_form_past'}))

    date_examin_15 = forms.DateField(label='受診日', required=False, widget=DatePickerInput(format='%Y-%m-%d'))
    operation_15 = forms.CharField(label='受診内容', required=False, widget=forms.Textarea(attrs={'class': 'cls_form_past'}))

    date_examin_16 = forms.DateField(label='受診日', required=False, widget=DatePickerInput(format='%Y-%m-%d'))
    operation_16 = forms.CharField(label='受診内容', required=False, widget=forms.Textarea(attrs={'class': 'cls_form_past'}))

    date_examin_17 = forms.DateField(label='受診日', required=False, widget=DatePickerInput(format='%Y-%m-%d'))
    operation_17 = forms.CharField(label='受診内容', required=False, widget=forms.Textarea(attrs={'class': 'cls_form_past'}))

    date_examin_18 = forms.DateField(label='受診日', required=False, widget=DatePickerInput(format='%Y-%m-%d'))
    operation_18 = forms.CharField(label='受診内容', required=False, widget=forms.Textarea(attrs={'class': 'cls_form_past'}))

    date_examin_19 = forms.DateField(label='受診日', required=False, widget=DatePickerInput(format='%Y-%m-%d'))
    operation_19 = forms.CharField(label='受診内容', required=False, widget=forms.Textarea(attrs={'class': 'cls_form_past'}))

    date_examin_20 = forms.DateField(label='受診日', required=False, widget=DatePickerInput(format='%Y-%m-%d'))
    operation_20 = forms.CharField(label='受診内容', required=False, widget=forms.Textarea(attrs={'class': 'cls_form_past'}))

    date_examin_21 = forms.DateField(label='受診日', required=False, widget=DatePickerInput(format='%Y-%m-%d'))
    operation_21 = forms.CharField(label='受診内容', required=False, widget=forms.Textarea(attrs={'class': 'cls_form_past'}))

    date_examin_22 = forms.DateField(label='受診日', required=False, widget=DatePickerInput(format='%Y-%m-%d'))
    operation_22 = forms.CharField(label='受診内容', required=False, widget=forms.Textarea(attrs={'class': 'cls_form_past'}))

    date_examin_23 = forms.DateField(label='受診日', required=False, widget=DatePickerInput(format='%Y-%m-%d'))
    operation_23 = forms.CharField(label='受診内容', required=False, widget=forms.Textarea(attrs={'class': 'cls_form_past'}))

    date_examin_24 = forms.DateField(label='受診日', required=False, widget=DatePickerInput(format='%Y-%m-%d'))
    operation_24 = forms.CharField(label='受診内容', required=False, widget=forms.Textarea(attrs={'class': 'cls_form_past'}))

    date_examin_25 = forms.DateField(label='受診日', required=False, widget=DatePickerInput(format='%Y-%m-%d'))
    operation_25 = forms.CharField(label='受診内容', required=False, widget=forms.Textarea(attrs={'class': 'cls_form_past'}))

    date_examin_26 = forms.DateField(label='受診日', required=False, widget=DatePickerInput(format='%Y-%m-%d'))
    operation_26 = forms.CharField(label='受診内容', required=False, widget=forms.Textarea(attrs={'class': 'cls_form_past'}))

    date_examin_27 = forms.DateField(label='受診日', required=False, widget=DatePickerInput(format='%Y-%m-%d'))
    operation_27 = forms.CharField(label='受診内容', required=False, widget=forms.Textarea(attrs={'class': 'cls_form_past'}))

    date_examin_28 = forms.DateField(label='受診日', required=False, widget=DatePickerInput(format='%Y-%m-%d'))
    operation_28 = forms.CharField(label='受診内容', required=False, widget=forms.Textarea(attrs={'class': 'cls_form_past'}))

    date_examin_29 = forms.DateField(label='受診日', required=False, widget=DatePickerInput(format='%Y-%m-%d'))
    operation_29 = forms.CharField(label='受診内容', required=False, widget=forms.Textarea(attrs={'class': 'cls_form_past'}))

    date_examin_30 = forms.DateField(label='受診日', required=False, widget=DatePickerInput(format='%Y-%m-%d'))
    operation_30 = forms.CharField(label='受診内容', required=False, widget=forms.Textarea(attrs={'class': 'cls_form_past'}))

    date_examin_31 = forms.DateField(label='受診日', required=False, widget=DatePickerInput(format='%Y-%m-%d'))
    operation_31 = forms.CharField(label='受診内容', required=False, widget=forms.Textarea(attrs={'class': 'cls_form_past'}))

    date_examin_32 = forms.DateField(label='受診日', required=False, widget=DatePickerInput(format='%Y-%m-%d'))
    operation_32 = forms.CharField(label='受診内容', required=False, widget=forms.Textarea(attrs={'class': 'cls_form_past'}))

    date_examin_33 = forms.DateField(label='受診日', required=False, widget=DatePickerInput(format='%Y-%m-%d'))
    operation_33 = forms.CharField(label='受診内容', required=False, widget=forms.Textarea(attrs={'class': 'cls_form_past'}))

    date_examin_34 = forms.DateField(label='受診日', required=False, widget=DatePickerInput(format='%Y-%m-%d'))
    operation_34 = forms.CharField(label='受診内容', required=False, widget=forms.Textarea(attrs={'class': 'cls_form_past'}))

    date_examin_35 = forms.DateField(label='受診日', required=False, widget=DatePickerInput(format='%Y-%m-%d'))
    operation_35 = forms.CharField(label='受診内容', required=False, widget=forms.Textarea(attrs={'class': 'cls_form_past'}))

    date_examin_36 = forms.DateField(label='受診日', required=False, widget=DatePickerInput(format='%Y-%m-%d'))
    operation_36 = forms.CharField(label='受診内容', required=False, widget=forms.Textarea(attrs={'class': 'cls_form_past'}))

    date_examin_37 = forms.DateField(label='受診日', required=False, widget=DatePickerInput(format='%Y-%m-%d'))
    operation_37 = forms.CharField(label='受診内容', required=False, widget=forms.Textarea(attrs={'class': 'cls_form_past'}))

    date_examin_38 = forms.DateField(label='受診日', required=False, widget=DatePickerInput(format='%Y-%m-%d'))
    operation_38 = forms.CharField(label='受診内容', required=False, widget=forms.Textarea(attrs={'class': 'cls_form_past'}))

    date_examin_39 = forms.DateField(label='受診日', required=False, widget=DatePickerInput(format='%Y-%m-%d'))
    operation_39 = forms.CharField(label='受診内容', required=False, widget=forms.Textarea(attrs={'class': 'cls_form_past'}))

    date_examin_40 = forms.DateField(label='受診日', required=False, widget=DatePickerInput(format='%Y-%m-%d'))
    operation_40 = forms.CharField(label='受診内容', required=False, widget=forms.Textarea(attrs={'class': 'cls_form_past'}))

    date_examin_41 = forms.DateField(label='受診日', required=False, widget=DatePickerInput(format='%Y-%m-%d'))
    operation_41 = forms.CharField(label='受診内容', required=False, widget=forms.Textarea(attrs={'class': 'cls_form_past'}))

    date_examin_42 = forms.DateField(label='受診日', required=False, widget=DatePickerInput(format='%Y-%m-%d'))
    operation_42 = forms.CharField(label='受診内容', required=False, widget=forms.Textarea(attrs={'class': 'cls_form_past'}))

    date_examin_43 = forms.DateField(label='受診日', required=False, widget=DatePickerInput(format='%Y-%m-%d'))
    operation_43 = forms.CharField(label='受診内容', required=False, widget=forms.Textarea(attrs={'class': 'cls_form_past'}))

    date_examin_44 = forms.DateField(label='受診日', required=False, widget=DatePickerInput(format='%Y-%m-%d'))
    operation_44 = forms.CharField(label='受診内容', required=False, widget=forms.Textarea(attrs={'class': 'cls_form_past'}))

    date_examin_45 = forms.DateField(label='受診日', required=False, widget=DatePickerInput(format='%Y-%m-%d'))
    operation_45 = forms.CharField(label='受診内容', required=False, widget=forms.Textarea(attrs={'class': 'cls_form_past'}))

    date_examin_46 = forms.DateField(label='受診日', required=False, widget=DatePickerInput(format='%Y-%m-%d'))
    operation_46 = forms.CharField(label='受診内容', required=False, widget=forms.Textarea(attrs={'class': 'cls_form_past'}))

    date_examin_47 = forms.DateField(label='受診日', required=False, widget=DatePickerInput(format='%Y-%m-%d'))
    operation_47 = forms.CharField(label='受診内容', required=False, widget=forms.Textarea(attrs={'class': 'cls_form_past'}))

    date_examin_48 = forms.DateField(label='受診日', required=False, widget=DatePickerInput(format='%Y-%m-%d'))
    operation_48 = forms.CharField(label='受診内容', required=False, widget=forms.Textarea(attrs={'class': 'cls_form_past'}))

    date_examin_49 = forms.DateField(label='受診日', required=False, widget=DatePickerInput(format='%Y-%m-%d'))
    operation_49 = forms.CharField(label='受診内容', required=False, widget=forms.Textarea(attrs={'class': 'cls_form_past'}))

    date_examin_50 = forms.DateField(label='受診日', required=False, widget=DatePickerInput(format='%Y-%m-%d'))
    operation_50 = forms.CharField(label='受診内容', required=False, widget=forms.Textarea(attrs={'class': 'cls_form_past'}))

    picture_1 = forms.FileField(label='画像1', required=False, widget=forms.FileInput(attrs={'accept':'image/*'}))
    picture_2 = forms.FileField(label='画像2', required=False, widget=forms.FileInput(attrs={'accept':'image/*'}))
    picture_3 = forms.FileField(label='画像3', required=False, widget=forms.FileInput(attrs={'accept':'image/*'}))
    picture_4 = forms.FileField(label='画像4', required=False, widget=forms.FileInput(attrs={'accept':'image/*'}))
    picture_5 = forms.FileField(label='画像5', required=False, widget=forms.FileInput(attrs={'accept':'image/*'}))

    class Meta:
        model = PostRcd
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(UserInfo, self).__init__(*args, **kwargs)
        self.fields['store'].widget.attrs['id'] = 'id_store'

    def save(self, *args, **kwargs):
        obj = super(UserInfo, self).save(commit=False, *args, **kwargs)
        # save前に変換したいデータがあればここに記入

        obj.save()
        return obj

    # def clean(self):
    #     cleaned_data = super().clean()

    #     name_orner = cleaned_data.get('name_orner')
    #     is_exists_name_orner = PostRcd.objects.filter(name_orner=name_orner).first()

    #     name_dog = cleaned_data.get('name_dog')
    #     is_exists_name_dog = PostRcd.objects.filter(name_dog=name_dog).first()

    #     tel = cleaned_data.get('tel')
    #     is_exists_tel = PostRcd.objects.filter(tel=tel).first()
        
    #     if is_exists_name_orner and is_exists_name_dog and is_exists_tel :
    #         raise validators.ValidationError('ERROR!! ：その飼い主のデータはすでに登録されています')

class UserDelete(forms.Form):
    id = forms.IntegerField(widget=forms.HiddenInput)

class UserFind(forms.Form):
    find = forms.CharField(label='カルテを検索', required=False, widget=forms.TextInput(attrs={'class': 'cls_form'}))

class LoginForm(forms.Form):
    username = forms.CharField(label='ユーザー名', max_length=150, widget=forms.TextInput(attrs={'class': 'cls_form'}))
    password = forms.CharField(label='パスワード', widget=forms.PasswordInput(attrs={'class': 'cls_form'}))