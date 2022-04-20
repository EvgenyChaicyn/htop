import psutil

class cpu():
    info = {}
    template = "{count}\n"


    def get(self):
        self.info.update(count=psutil.cpu_count())
        self.info.update(percent=psutil.cpu_percent(interval=1, percpu=True))
        self.info.update(freq=[freq.current for freq in psutil.cpu_freq(percpu=True)])


    def _prepare(self):
        self.template += "Freq\n"
        for index in range(len(self.info["freq"])):
            self.template += "{freq[" + str(index) +"]}\n"

        self.template += "Percent\n"
        for index in range(len(self.info["percent"])):
            self.template += "{percent[" + str(index) +"]}\n"

    def show(self):
        self._prepare()
        print(self.template.format(**self.info))





