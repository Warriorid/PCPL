goods = [
    {'title': 'Ковер', 'price': 2000, 'color': 'green'},
    {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'}
]


def field(items, *args):
    assert len(args) > 0

    if len(args) == 1:
        for item in items:
            value = item.get(args[0])
            if value is not None:
                yield value
    else:
        for item in items:
            item_dict = {arg: item[arg] for arg in args if item.get(arg) is not None}
            if item_dict:
                yield item_dict


print(list(field(goods, 'title')))
print(list(field(goods, 'title', 'price')))``