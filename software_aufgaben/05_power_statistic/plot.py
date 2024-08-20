from pymongo import MongoClient
import os
import matplotlib.pyplot as plt
from Power import Power

connection_string = os.getenv('MONGODB_PATH')
client = MongoClient(connection_string)
db_name = 'system_monitor'
collection_name = 'usage_data'

db = client[db_name]
collection = db[collection_name]

powerlist = []
for power in list(collection.find()):
    powerlist.append(Power(**power)) # erstellt die power objekte aus den documents und fügt sie zur liste hinzu

# daten holen für den plot
timestamps = [stats.timestamp for stats in powerlist]
cpu_percents = [stats.cpu_percent for stats in powerlist]
ram_used = [stats.ram_used for stats in powerlist]
ram_total = [stats.ram_total for stats in powerlist]
ram_precents = [100/stats.ram_total*stats.ram_used for stats in powerlist]

plt.plot(timestamps, cpu_percents, label='CPU Usage (%)')
plt.plot(timestamps, ram_precents, label='RAM Used (%)', linestyle='--')

plt.xlabel('Timestamp')
plt.ylabel('Usage')
plt.title('System Stats Over Time')
plt.legend()
plt.grid(True)

plt.gcf().autofmt_xdate() # formatiert datum
plt.show()