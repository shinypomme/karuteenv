from json import JSONDecodeError
from django.db import models
import os
from django.contrib.auth.models import User

STORE_CHOISE = (
    ("1", '大須サロン'),
    ("2", 'SKドックラン'),
    ("3", 'ローズマリー岡崎店'),
    ("4", 'ローズマリー豊橋店'),
    ("5", 'Floor岡崎店'),
    ("6", 'クヌート土岐店'),
    ("7", 'その他')
)

# Create your models here.
class PostRcd(models.Model):
    name_orner = models.CharField(max_length=50)
    name_dog = models.CharField(max_length=255)
    mail = models.EmailField(max_length=255, null=True)
    tel = models.CharField(max_length=20, null=True)
    store = models.CharField(max_length=255, choices=STORE_CHOISE, null=True)
    picture_1 = models.FileField(upload_to='picture/%Y/%m/%d', null=True)
    picture_2 = models.FileField(upload_to='picture/%Y/%m/%d', null=True)
    picture_3 = models.FileField(upload_to='picture/%Y/%m/%d', null=True)
    picture_4 = models.FileField(upload_to='picture/%Y/%m/%d', null=True)
    picture_5 = models.FileField(upload_to='picture/%Y/%m/%d', null=True)

    record_no = models.IntegerField(default=0)

    date_examin = models.DateField(max_length=255, null=True)
    operation = models.CharField(max_length=65535, null=True)

    date_examin_1 = models.DateField(max_length=255, null=True)
    operation_1 = models.CharField(max_length=65535, null=True)

    date_examin_2 = models.DateField(max_length=255, null=True)
    operation_2 = models.CharField(max_length=65535, null=True)

    date_examin_3 = models.DateField(max_length=255, null=True)
    operation_3 = models.CharField(max_length=65535, null=True)

    date_examin_4 = models.DateField(max_length=255, null=True)
    operation_4 = models.CharField(max_length=65535, null=True)

    date_examin_5 = models.DateField(max_length=255, null=True)
    operation_5 = models.CharField(max_length=65535, null=True)

    date_examin_6 = models.DateField(max_length=255, null=True)
    operation_6 = models.CharField(max_length=65535, null=True)

    date_examin_7 = models.DateField(max_length=255, null=True)
    operation_7 = models.CharField(max_length=65535, null=True)

    date_examin_8 = models.DateField(max_length=255, null=True)
    operation_8 = models.CharField(max_length=65535, null=True)

    date_examin_9 = models.DateField(max_length=255, null=True)
    operation_9 = models.CharField(max_length=65535, null=True)

    date_examin_10 = models.DateField(max_length=255, null=True)
    operation_10 = models.CharField(max_length=65535, null=True)

    date_examin_11 = models.DateField(max_length=255, null=True)
    operation_11 = models.CharField(max_length=65535, null=True)

    date_examin_12 = models.DateField(max_length=255, null=True)
    operation_12 = models.CharField(max_length=65535, null=True)

    date_examin_13 = models.DateField(max_length=255, null=True)
    operation_13 = models.CharField(max_length=65535, null=True)

    date_examin_14 = models.DateField(max_length=255, null=True)
    operation_14 = models.CharField(max_length=65535, null=True)

    date_examin_15 = models.DateField(max_length=255, null=True)
    operation_15 = models.CharField(max_length=65535, null=True)

    date_examin_16 = models.DateField(max_length=255, null=True)
    operation_16 = models.CharField(max_length=65535, null=True)

    date_examin_17 = models.DateField(max_length=255, null=True)
    operation_17 = models.CharField(max_length=65535, null=True)

    date_examin_18 = models.DateField(max_length=255, null=True)
    operation_18 = models.CharField(max_length=65535, null=True)

    date_examin_19 = models.DateField(max_length=255, null=True)
    operation_19 = models.CharField(max_length=65535, null=True)

    date_examin_20 = models.DateField(max_length=255, null=True)
    operation_20 = models.CharField(max_length=65535, null=True)

    date_examin_21 = models.DateField(max_length=255, null=True)
    operation_21 = models.CharField(max_length=65535, null=True)

    date_examin_22 = models.DateField(max_length=255, null=True)
    operation_22 = models.CharField(max_length=65535, null=True)

    date_examin_23 = models.DateField(max_length=255, null=True)
    operation_23 = models.CharField(max_length=65535, null=True)

    date_examin_24 = models.DateField(max_length=255, null=True)
    operation_24 = models.CharField(max_length=65535, null=True)

    date_examin_25 = models.DateField(max_length=255, null=True)
    operation_25 = models.CharField(max_length=65535, null=True)

    date_examin_26 = models.DateField(max_length=255, null=True)
    operation_26 = models.CharField(max_length=65535, null=True)

    date_examin_27 = models.DateField(max_length=255, null=True)
    operation_27 = models.CharField(max_length=65535, null=True)

    date_examin_28 = models.DateField(max_length=255, null=True)
    operation_28 = models.CharField(max_length=65535, null=True)

    date_examin_29 = models.DateField(max_length=255, null=True)
    operation_29 = models.CharField(max_length=65535, null=True)

    date_examin_30 = models.DateField(max_length=255, null=True)
    operation_30 = models.CharField(max_length=65535, null=True)

    date_examin_31 = models.DateField(max_length=255, null=True)
    operation_31 = models.CharField(max_length=65535, null=True)

    date_examin_32 = models.DateField(max_length=255, null=True)
    operation_32 = models.CharField(max_length=65535, null=True)

    date_examin_33 = models.DateField(max_length=255, null=True)
    operation_33 = models.CharField(max_length=65535, null=True)

    date_examin_34 = models.DateField(max_length=255, null=True)
    operation_34 = models.CharField(max_length=65535, null=True)

    date_examin_35 = models.DateField(max_length=255, null=True)
    operation_35 = models.CharField(max_length=65535, null=True)

    date_examin_36 = models.DateField(max_length=255, null=True)
    operation_36 = models.CharField(max_length=65535, null=True)

    date_examin_37 = models.DateField(max_length=255, null=True)
    operation_37 = models.CharField(max_length=65535, null=True)

    date_examin_38 = models.DateField(max_length=255, null=True)
    operation_38 = models.CharField(max_length=65535, null=True)

    date_examin_39 = models.DateField(max_length=255, null=True)
    operation_39 = models.CharField(max_length=65535, null=True)

    date_examin_40 = models.DateField(max_length=255, null=True)
    operation_40 = models.CharField(max_length=65535, null=True)

    date_examin_41 = models.DateField(max_length=255, null=True)
    operation_41 = models.CharField(max_length=65535, null=True)

    date_examin_42 = models.DateField(max_length=255, null=True)
    operation_42 = models.CharField(max_length=65535, null=True)

    date_examin_43 = models.DateField(max_length=255, null=True)
    operation_43 = models.CharField(max_length=65535, null=True)

    date_examin_44 = models.DateField(max_length=255, null=True)
    operation_44 = models.CharField(max_length=65535, null=True)

    date_examin_45 = models.DateField(max_length=255, null=True)
    operation_45 = models.CharField(max_length=65535, null=True)

    date_examin_46 = models.DateField(max_length=255, null=True)
    operation_46 = models.CharField(max_length=65535, null=True)

    date_examin_47 = models.DateField(max_length=255, null=True)
    operation_47 = models.CharField(max_length=65535, null=True)

    date_examin_48 = models.DateField(max_length=255, null=True)
    operation_48 = models.CharField(max_length=65535, null=True)

    date_examin_49 = models.DateField(max_length=255, null=True)
    operation_49 = models.CharField(max_length=65535, null=True)

    date_examin_50 = models.DateField(max_length=255, null=True)
    operation_50 = models.CharField(max_length=65535, null=True)

    class Meta:
        db_table = 'postrcd'
        ordering = ['id']

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username