from django.db.models import Q
# from database.Administrative.models import Document


def get_and_filtered_results(params, query):
    result = set()
    for key, value in params.items():
        try:
            value = int(value)
        except ValueError:
            pass
        temp = set([item.pk for item in query if getattr(item, key) == value])
        if result:
            result = result.intersection(temp)
        else:
            result = temp
    return list(result)


######### functions related to Telegram api menus #########


def get_query_related_to_telegram_choice(data):
    items = [
        {'name': 'os_id_card',
         'model': 'Document',
         'filters': [Q(user__username='olivier'), Q(type='ID card')],
         'fields_to_get': 'file_path'
         }
    ]
    # for item in items:
    #     if item['name'] == data:
    #         print('data to retrieve = ', data)
    #         queryset = eval(item['model']).objects.all()
    #         for filter in item['filters']:
    #             queryset = queryset.filter(filter)
    #         result = queryset.first()
    #         print(result)
    #         print(getattr(result, item['fields_to_get']))
