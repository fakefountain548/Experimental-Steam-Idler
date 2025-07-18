import psutil

def set_low_resource_usage(name_contains):
    for proc in psutil.process_iter(['pid', 'name']):
        if name_contains.lower().replace(" ", "") in proc.info['name'].lower():
            try:
                p = psutil.Process(proc.info['pid'])
                p.nice(psutil.IDLE_PRIORITY_CLASS)
                p.cpu_affinity([0])
                return
            except Exception:
                continue