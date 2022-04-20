from htop.cpu import cpu
from htop.memory import memory
from htop.sistem import sistem

def main():
    cpu_info = cpu()
    cpu_info.get()
    cpu_info.show()

    memory_info = memory()
    memory_info.get()
    memory_info.show()

    sistem_info = sistem()
    sistem_info.get()
    sistem_info.show()


if __name__ == "__main__":
    main()

