import psutil
import json
import speedtest


print(psutil.cpu_count())
# while True:
print(psutil.cpu_percent(1))
mem = psutil.virtual_memory()
print(type(mem))
# Convert to dictionary
mem_dict = mem._asdict()

# Convert dictionary to JSON
# mem_json = json.dumps(mem_dict, indent=4)
# mem_dict = json.loads(mem_json)
print(mem_dict['total'])
print(speedtest.Speedtest().download())
print(speedtest.Speedtest().upload())
print(speedtest.results.ping)

