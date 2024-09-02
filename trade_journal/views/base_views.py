from django.shortcuts import render
from ..models import TradeJournal

def index(request):
    sort_list = 'newest' if request.GET.get('sort') == None else request.GET.get('sort')
    currency_value = 'all' if request.GET.get('currency') == None else request.GET.get('currency')
    symbol_value = 'all' if request.GET.get('symbol') == None else request.GET.get('symbol')

    # 코인종류 선택시 filter
    currency_list = TradeJournal.objects.values('currency').distinct('currency') if symbol_value == 'all' else TradeJournal.objects.values('currency').distinct('currency').filter(symbol=symbol_value)

    # 거래소선택시 filter
    symbol_list = TradeJournal.objects.values('symbol').distinct('symbol') if currency_value == 'all' else TradeJournal.objects.values('symbol').distinct('symbol').filter(currency=currency_value)

    # 로그인 되어있으면
    if request.user.is_authenticated:
        # 날짜순 정렬
        journal_list = TradeJournal.objects.order_by('-created_at') if sort_list == 'newest' else TradeJournal.objects.order_by('created_at')
        # 거래소별 정렬
        journal_list = journal_list if currency_value == 'all' else journal_list.filter(currency=currency_value)
        # 코인별 정렬
        journal_list = journal_list if symbol_value == 'all' else journal_list.filter(symbol=symbol_value)

        context = {'journal_list': journal_list,
                   'sort_list': sort_list,
                   'currency_list': currency_list,
                   'currency_value': currency_value,
                   'symbol_list': symbol_list,
                   'symbol_value': symbol_value,

                  }

        return render(request, 'trade_journal/index.html', context)
    else:
        #매매일지 소개페이지 작성
        pass

    return render(request, 'trade_journal/index.html')
