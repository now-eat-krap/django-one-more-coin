from django.db import models
from django.contrib.auth.models import User

class TradeJournal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    #매매일지
    transaction_text = models.JSONField('매매일지',encoder=None, default=dict)

    #결과
    result_text = models.JSONField('결과',encoder=None, default=dict)

    #거래소
    currency = models.CharField('거래소',max_length=20, default='')

    #심볼 
    symbol = models.CharField('심볼',max_length=20, default='')

    #작성일은 제목과 동일
    created_at = models.DateTimeField('작성일', auto_now_add=True)
    updated_at = models.DateTimeField('갱신일', auto_now=True)
