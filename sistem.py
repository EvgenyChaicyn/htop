import psutil

class sistem():
    info = {}
    template = "{times}\n"


    def get(self):
        self.info.update(times=psutil.cpu_times())

    def _prepare(self):
        self.template += "times\n"
        for index in range(len(self.info["times"])):
            self.template += "{times[" + str(index) +"]}\n"

    def show(self):
        self._prepare()
        print(self.template.format(**self.info))



