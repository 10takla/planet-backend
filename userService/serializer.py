from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.core import validators
from django.db.models import Sum, Count
from django.db.models import F, Max, Q
from userService.models import User
from buyingService.models import Buying
from planetService.models import Plot


class BaseUserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(
        max_length=10,
        min_length=5,
        error_messages={
            'blank': 'Не оставляйте это поле пустым',
            'min_length': 'Логин должен содержать от 5 до 10 символов',
            'max_length': 'Логин должен содержать от 5 до 10 символов',
        },
        validators=[
            validators.RegexValidator(
                regex=r'^[a-zA-Z0-9]+([\._][a-zA-Z0-9]+)*$',
                message='логин должен содержать только буквенно-цифровые символы'
            ),
            UniqueValidator(queryset=User.objects.all(), message='пользователь уже существует')
        ]
    )
    password = serializers.CharField(
        max_length=20,
        min_length=5,
        write_only=True,
        error_messages={
            'blank': 'Не оставляйте это поле пустым',
            'min_length': 'введите пароль от 5 до 20 символов',
            'max_length': 'введите пароль от 5 до 20 символов',
        }
    )
    email = serializers.EmailField(
        max_length=255,
        error_messages={
            'blank': 'Не оставляйте это поле пустым',
            'max_length': 'email не должен превышать 255 символов',
        },
        validators=[
            validators.EmailValidator(message='email введен не правильно'),
            UniqueValidator(queryset=User.objects.all(), message=' эта почта уже зарегистрирована')
        ]
    )


class AuthUserSerializer(BaseUserSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'email']
        extra_kwargs: {
            'username': {'source': 'login'},
            'password': {'source': 'pass'},
            'email': {'source': 'email'}
        }


class UpdateUserSerializer(BaseUserSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'logo', 'color', 'telegramName', 'status']

    def __init__(self, *args, **kwargs):
        context = kwargs.get('context', {})
        fields = set(context.get('fields', ''))
        all_fields = set(self.fields.keys())
        super().__init__(*args, **kwargs)
        if fields is not None:
            for field_name in all_fields - fields:
                self.fields.pop(field_name)


class UserSerializer(serializers.ModelSerializer):
    # plotsCount = serializers.SerializerMethodField()
    # rank = serializers.SerializerMethodField()
    # plotsCapital = serializers.SerializerMethodField()

    # def get_plotsCount(self, user):
    #     return Plot.objects.filter(owner=user).count()
    #
    # def get_rank(self, obj):
    #     users_plots_count = User.objects.annotate(num_plots=Count('plot')).order_by('-num_plots')
    #     rank = list(users_plots_count).index(obj) + 1
    #     return rank
    #
    # def get_plotsCapital(self, user):
    #     total_capital = Plot.objects.filter(owner=user).aggregate(total=Sum('price'))['total']
    #     return total_capital or 0

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'wallet', 'logo', 'color', 'telegramName', 'status',
                  # 'plotsCapital',
                  # 'rank',
                  # 'plotsCount'
                  ]

    def __init__(self, *args, **kwargs):
        fields = set(self.fields.keys())
        all_fields = set(self.fields.keys())
        user_fields = {'email', 'wallet'}

        mode = kwargs.get('context', {}).get('mode', '')
        if mode == 'conf_user':
            pass
        else:

            fields = all_fields.difference(user_fields)

        super().__init__(*args, **kwargs)
        if fields is not None:
            for field_name in all_fields - fields:
                self.fields.pop(field_name)
