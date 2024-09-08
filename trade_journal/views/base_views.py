from django.shortcuts import render
from ..models import TradeJournal
from datetime import datetime, date, timedelta

def index(request):
    #처음과 끝 시간 
    start_end_date_list =[TradeJournal.objects.values('created_at').earliest('created_at'),TradeJournal.objects.values('created_at').latest('created_at')]

    sort_value = 'newest' if request.GET.get('sort') == None else request.GET.get('sort')
    currency_value = 'all' if request.GET.get('currency') == None else request.GET.get('currency')
    symbol_value = 'all' if request.GET.get('symbol') == None else request.GET.get('symbol')

    date_range_value = '날짜 선택' if request.GET.get('date_range') == None else request.GET.get('date_range')
    # date_range_value값 date로 변경
    date_range = None
    if date_range_value != '날짜 선택':
        date_range = date_range_value.split(' - ')
        date_range[0] = datetime.strptime(date_range[0], '%Y/%m/%d').date()
        date_range[1] = datetime.strptime(date_range[1], '%Y/%m/%d').date()

    # 코인종류 선택시 filter

      # 심볼 filter
    currency_list = TradeJournal.objects.values('currency').distinct('currency') if symbol_value == 'all' else TradeJournal.objects.values('currency').distinct('currency').filter(symbol=symbol_value)
      #  날짜 범위 필터
    currency_list = currency_list if date_range_value == "날짜 선택" else currency_list.filter(created_at__range=[date_range[0],date_range[1] + timedelta(days=1)])

    # 거래소선택시 filter

      # 심볼 filter
    symbol_list = TradeJournal.objects.values('symbol').distinct('symbol') if currency_value == 'all' else TradeJournal.objects.values('symbol').distinct('symbol').filter(currency=currency_value)
      #  날짜 범위 필터
    symbol_list = symbol_list if date_range_value == "날짜 선택" else symbol_list.filter(created_at__range=[date_range[0],date_range[1] + timedelta(days=1)])


    # 로그인 되어있으면
    if request.user.is_authenticated:
        # 날짜순 정렬
        journal_list = TradeJournal.objects.order_by('-created_at') if sort_value == 'newest' else TradeJournal.objects.order_by('created_at')

        # 거래소별 정렬
        journal_list = journal_list if currency_value == 'all' else journal_list.filter(currency=currency_value)

        # 코인별 정렬
        journal_list = journal_list if symbol_value == 'all' else journal_list.filter(symbol=symbol_value)

        # 날짜범위 정렬
        journal_list = journal_list if date_range_value == '날짜 선택' else journal_list.filter(created_at__range=[date_range[0],date_range[1] + timedelta(days=1)])

        context = {
                   'start_end_date_list':start_end_date_list,
                   'journal_list': journal_list,
                   'sort_value': sort_value,
                   'currency_list': currency_list,
                   'currency_value': currency_value,
                   'symbol_list': symbol_list,
                   'symbol_value': symbol_value,
                   'date_range_value':date_range_value,
                   'date_range':date_range,
                  }

        return render(request, 'trade_journal/index.html', context)
    else:
        #매매일지 소개페이지 작성
        pass

    return render(request, 'trade_journal/index.html')
