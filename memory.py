import psutil

class memory:

      def  percent(self):
          print(psutil.virtual_memory())

a = memory()
a.percent()