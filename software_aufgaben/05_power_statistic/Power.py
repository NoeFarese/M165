from datetime import datetime
import psutil


class Power:
    def __init__(self, cpu_percent=None, ram_total=None, ram_used=None, timestamp=None, _id=None):
        if cpu_percent is None:
            self.cpu_percent = psutil.cpu_percent(interval=1)
        else:
            self.cpu_percent = cpu_percent

        ram = psutil.virtual_memory()
        if ram_total is None:
            self.ram_total = ram.total / (1024 ** 2)
        else:
            self.ram_total = ram_total

        if ram_used is None:
            self.ram_used = ram.used / (1024 ** 2)
        else:
            self.ram_used = ram_used

        self.timestamp = timestamp if timestamp else datetime.now()
        if _id is not None:
            self._id = _id
