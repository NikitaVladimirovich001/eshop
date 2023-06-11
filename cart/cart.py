# карзина будет хронится в виде пор "ключ-значения"
# в качестве ключа будет использоваться id товара, а в качестве значения - количество
# данного товара

class Cart:
    def __init__(self, request):
        self.session = request.session # сохроняем ссылку на сессию в переменной self.session
        if 'cart' not in self.session.keys():
            self.session['cart'] = dict()

    def add(self, prod_id, prod_count):
        if prod_id in self.session['cart'].keys():
            raise AttributeError(f'Товар с id{prod_id} уже есть в корзине')
        self.session['cart'][prod_id] = prod_count
        self.save()

    def __aidd__(self, kv_pair):
        self.add(*kv_pair)
        self.add(kv_pair[0], kv_pair[1])

    def change(self, prod_id, prod_count):
        try: # если get генерирует исключение то переходим к блоку except
            self.get(prod_id)
            self.session['cart'][prod_id] = prod_count
        except AttributeError as e: # пробрасываем исключение вверх
             raise e

        self.save()

    # [] = value
    def __setitem__(self, key, value):
        try:
            self.add(key, value)
        except AttributeError:
            self.change(key,value)

    # cart[key]
    def __getitem__(self, key):
        return self.get(key)

    def get(self,key):
        if key not in self.session['cart']: # если товара с key нет в корзине
            raise  AttributeError(f'Товар с id{key} нет в корзине! ')
        return self.session['cart'][key] # возврощаем количество id  с товаром

    def del_(self, key): # удаление товара из корщины
        del self.session['cart'][key]
        self.save()

    def __delitem__(self, key):
        self.del_(key)

    def __iter__(self): # для переборки корзины в циклах
        for key, value in self.session['cart'].items():
            yield (key, value) # порождаем пары ключ значение

    def save(self):
        self.session.modified = True

    def keys(self):
        return self.session['cart'].keys()
