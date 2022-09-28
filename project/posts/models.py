from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    tank = 'TK'
    heal = 'HL'
    DD = 'DD'
    GM = 'GM'
    QG = 'QG'
    blacksmith = 'BS'
    leather_worker = 'LW'
    potion_master = 'PM'
    spell_master = 'SM'
    dealer = 'DL'

    CAT = [
        (tank, 'Танки'),
        (heal, 'Хилы'),
        (DD, 'ДД'),
        (GM, 'Гилдмастеры'),
        (QG, 'Квестгиверы'),
        (blacksmith, 'Кузнецы'),
        (leather_worker, 'Кожевники'),
        (potion_master, 'Зельевары'),
        (spell_master, 'Мастера заклинаний'),
        (dealer, 'Торговцы'),

    ]
    type = models.CharField(max_length=2, choices=CAT, default=tank)
    time_add = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=255)
    text = models.TextField()

    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def preview(self):
        return f'{self.text[0:124]}'

    def __str__(self):
        return f'{self.name}'


class Response(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.TextField()
    who = models.ForeignKey(User, on_delete=models.CASCADE)
    whom_id = models.IntegerField(default=0)
    boolean = models.BooleanField(default=False)


