import psutil

class memory():
    info = {}
    template = "{mem}\n"


    def get(self):
        self.info.update(mem=psutil.virtual_memory())

    def _prepare(self):
        self.template += "mem\n"
        for index in range(len(self.info["mem"])):
            self.template += "{mem[" + str(index) +"]}\n"

    def show(self):
        self._prepare()
        print(self.template.format(**self.info))



