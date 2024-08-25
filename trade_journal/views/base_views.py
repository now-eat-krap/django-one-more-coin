from django.shortcuts import render
from ..models import TradeJournal

# Create your views here.
def index(request):
    # 로그인 되어있으면
    if request.user.is_authenticated:
        journal_list = TradeJournal.objects.order_by('-created_at')
        context = {'journal_list': journal_list}
        return render(request, 'trade_journal/index.html', context)
    else:
        #매매일지 소개페이지 작성
        pass

    return render(request, 'trade_journal/index.html')
