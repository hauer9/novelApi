from django_filters.rest_framework import FilterSet
from django_filters import DateFromToRangeFilter
from .models import History, SearchRecord


class HistoryFilter(FilterSet):
    """
    历史记录过滤
    """
    update_time = DateFromToRangeFilter(help_text='日期')

    class Meta:
        model = History
        fields = ['update_time']


class SearchRecordFilter(FilterSet):
    """
    搜索记录过滤
    """
    update_time = DateFromToRangeFilter(help_text='日期')

    class Meta:
        model = SearchRecord
        fields = ['update_time']
