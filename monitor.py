import psutil
import platform

CPU_COUNT_MONITOR = psutil.cpu_count()
processor_info = f'{platform.processor()}'
cpu_freq_info = f'{psutil.cpu_freq(percpu=True)}'
cpu_quantity = f'{CPU_COUNT_MONITOR} cores'
memory_info = f'{psutil.virtual_memory()}'
disk_partitions_info = f'{psutil.disk_partitions()}'
packets_info = f'{psutil.net_io_counters(pernic=False, nowrap=True).packets_sent} packets'

cpu_history = [[None]*100 for _ in range(CPU_COUNT_MONITOR)]
ram_history = [[None]*100 for _ in range(2)]
disk_history = [[None]*100 for _ in range(2)]
net_stat_history = [[None]*100 for _ in range(2)]
temp_history = [[None]*100 for _ in range(len(psutil.sensors_temperatures()))]

disk_io_counters_monitor = psutil.disk_io_counters(perdisk=True)

def update_monitor_data():
    _cpu_usage = psutil.cpu_percent(percpu=True)

    for i in range(CPU_COUNT_MONITOR):
        cpu_history[i][:-1] = cpu_history[i][1:]
        cpu_history[i][-1] = _cpu_usage[i]

    _ram_usage = psutil.virtual_memory().percent
    _swap_usage = psutil.swap_memory().percent
    disk_read = disk_io_counters_monitor[list(disk_io_counters_monitor.keys())[0]].read_bytes
    disk_write = disk_io_counters_monitor[list(disk_io_counters_monitor.keys())[0]].write_bytes
    net_sent = psutil.net_io_counters(pernic=False, nowrap=True).bytes_sent
    net_recv = psutil.net_io_counters(pernic=False, nowrap=True).bytes_recv
    
    ram_history[0][:-1] = ram_history[0][1:]
    ram_history[0][-1] = _ram_usage  
    ram_history[1][:-1] = ram_history[1][1:]    
    ram_history[1][-1] = _swap_usage 

    disk_history[0][:-1] = disk_history[0][1:]
    disk_history[0][-1] = disk_read
    disk_history[1][:-1] = disk_history[1][1:]
    disk_history[1][-1] = disk_write

    net_stat_history[0][:-1] = net_stat_history[0][1:]
    net_stat_history[0][-1] = net_sent  
    net_stat_history[1][:-1] = net_stat_history[1][1:]    
    net_stat_history[1][-1] = net_recv

    _temps = psutil.sensors_temperatures()  
    for i, (name, entries) in enumerate(_temps.items()):
        for entry in entries:
            temp_history[i][:-1] = temp_history[i][1:]
            temp_history[i][-1] = entry.current
