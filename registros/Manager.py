from django.db import models
from django.db.models import Q
from django.db.models.query import QuerySet

class MyModelMixin(object):

    def q_for_search_word(self, word):
        return Q(name__icontains=word) | Q(customer__name__icontains=word) | \
               Q(store__name__icontains=word)

    def q_for_search(self, search):
        q = Q()
        if search:
            searches = search.split()
            for word in searches:
                q = q & self.q_for_search_word(word)
        return q

    def filter_on_search(self, search):
        return self.filter(self.q_for_search(search))


class MyModelQuerySet(QuerySet, MyModelMixin):
    pass


class MyModelManager(models.Manager, MyModelMixin):

    def get_queryset(self):
        return MyModelQuerySet(self.model, using=self._db)