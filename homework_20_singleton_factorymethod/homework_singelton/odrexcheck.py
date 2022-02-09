from homework_20_singleton_factorymethod.homework_singelton import singelton_hw


@singelton_hw
class HealthOdrexCheck:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not HealthOdrexCheck._instance:
            HealthOdrexCheck._instance = super(HealthOdrexCheck, cls).__new__(cls, *args, **kwargs)
        return HealthOdrexCheck._instance

    def __init__(self):
        self._servers = []

    def addServer(self):
        self._servers.append("Server 1")
        self._servers.append("Server 2")
        self._servers.append("Server 3")

    def changeServer(self):
        def changeServer(self):
            self._servers.pop()
            self._servers.append("Server 2")

hoc1 = HealthOdrexCheck()
hoc3 = HealthOdrexCheck()
hoc2.addServer()



print("Check health patience for servers(1)...")
print("Check health patience for servers(2)...")
print("Check health patience for servers(3)...")






