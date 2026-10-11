import psutil

import asyncio

async def get_server_stats() -> dict:
    # Run CPU intensive psutil calls in a thread if needed, but for now just interval=0.1
    # However, let's keep it simple first.
    cpu = psutil.cpu_percent(interval=0.1)
    memory = psutil.virtual_memory()
    disk = psutil.disk_usage("/")


    return {
        "cpu": {
            "usage_percent": cpu,
        },
        "ram": {
            "total_gb": round(memory.total / (1024**3), 2),
            "used_gb": round(memory.used / (1024**3), 2),
            "available_gb": round(memory.available / (1024**3), 2),
            "usage_percent": memory.percent,
        },
        "disk": {
            "total_gb": round(disk.total / (1024**3), 2),
            "used_gb": round(disk.used / (1024**3), 2),
            "free_gb": round(disk.free / (1024**3), 2),
            "usage_percent": disk.percent,
        },
    }
