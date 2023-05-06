class Secret:
    def _method_1(self):
        print('Вам не стоит это видеть.')

    def __method_2(self):
        print('Вам нельзя это видеть!')

    def method_3(self):
        print('Это общедоступный метод.')

obj = Secret()
obj._method_1()
obj.__method_2()
obj.method_3()