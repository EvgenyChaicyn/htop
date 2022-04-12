import psutil

class procesor:

    def percent(self):
        for cp in psutil.cpu_percent(interval=1, percpu=True):
            print('Загрузка ядра процессора в %: {}'.format(cp))

d = procesor()
d.percent()

