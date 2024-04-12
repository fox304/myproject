from django import forms

from seminarsapp.models import AuthorModel, ArticleModel

"""
---------------Перечислим некоторые из наиболее популярных классов Field в Django:--------------

● CharField — используется для создания текстовых полей, таких как имя,
фамилия, электронная почта и т.д.
● EmailField — используется для создания поля электронной почты.
● IntegerField — используется для создания поля для ввода целых чисел.
● FloatField — используется для создания поля для ввода чисел с плавающей
точкой.
● BooleanField — используется для создания поля флажка.
● DateField — используется для создания поля даты.
● DateTimeField — используется для создания поля даты и времени.
● FileField — используется для создания поля для загрузки файла.
● ImageField — используется для создания поля для загрузки изображения.
● ChoiceField — используется для создания выпадающего списка с выбором
одного из нескольких вариантов.

--------------Вот некоторые из наиболее популярных классов виджетов в Django:----------------

● TextInput — используется для создания текстового поля ввода.
● EmailInput — используется для создания поля ввода электронной почты.
● PasswordInput — используется для создания поля ввода пароля.
● NumberInput — используется для создания поля ввода чисел.
● CheckboxInput — используется для создания флажка.
● DateInput — используется для создания поля ввода даты.
● DateTimeInput — используется для создания поля ввода даты и времени.
● FileInput — используется для создания поля загрузки файла.
● Select — используется для создания выпадающего списка с выбором одного
  из нескольких вариантов.
● RadioSelect — используется для создания списка радиокнопок.
● Textarea — используется для создания многострочного текстового поля ввода.



"""


class SelectRandom(forms.Form):
    game = forms.ChoiceField(choices=[('coin', 'монетка'), ('dice', 'кость'), ('number', 'число')])


class NewAuthor(forms.Form):
    name = forms.CharField(max_length=20)
    surname = forms.CharField(max_length=20)
    email = forms.EmailField()
    bio = forms.CharField()
    dob = forms.DateField()
    # fullname = forms.CharField(max_length=40)


class NewAuthor2(forms.ModelForm):
    class Meta:
        model = AuthorModel
        fields = ['name', 'surname', 'email', 'bio']

class NewArticle2(forms.ModelForm):
    class Meta:
        model = ArticleModel
        fields = ['title', 'text', 'category']
