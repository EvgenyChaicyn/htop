import psutil

class info:

    def pid(self):
        for p in psutil.process_iter(['pid']):
            print(p)

a = info()
a.pid()

