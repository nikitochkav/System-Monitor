from fastapi import FastAPI, Depends, HTTPException, Request, status
from fastapi.middleware.wsgi import WSGIMiddleware
from fastapi.security import HTTPBasic, HTTPAuthorizationCredentials
from passlib.context import CryptContext
from dash_app import dash_app
from typing import Annotated
import psutil
from monitor import update_monitor_data, CPU_COUNT_MONITOR, cpu_history, ram_history, temp_history

app = FastAPI()
app.mount("/dash/", WSGIMiddleware(dash_app.server))

security = HTTPBasic()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

SECRET_KEY = '1d404b2f7df64b75092005c86438ba590222d5e3c39357c672c6072eb8c6f632'
ALGORITHM = 'HS256'

HASHED_PASSWORD = pwd_context.hash("admin")

def verify_password(hashed_password, plain_password):
    return pwd_context.verify(plain_password, hashed_password)

def authenticate_user(credentials: Annotated[HTTPAuthorizationCredentials, Depends(security)]):
    if not verify_password(HASHED_PASSWORD, credentials.password):
        return False
    if credentials.username != "admin":
        return False
    return True

@app.get("/cpu/")
def get_cpu(request: Request, user: Annotated[dict, Depends(authenticate_user)], cpu_id: int | None = None):
    
    update_monitor_data()

    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    
    if cpu_id is not None:
        return {f"cpu{cpu_id+1}": cpu_history[cpu_id][-1]}
    else:
        return {f"cpu": [cpu_history[i][-1] for i in range(CPU_COUNT_MONITOR)]}

@app.get("/ram/")
def get_ram(request: Request, user: Annotated[dict, Depends(authenticate_user)]):

    update_monitor_data()

    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    
    return {"ram": ram_history[0][-1]}

@app.get("/disk/")
def get_disk(request: Request, user: Annotated[dict, Depends(authenticate_user)]):
    
    update_monitor_data()

    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    
    disk_usage = psutil.disk_usage('/')
    disk_io_counters = psutil.disk_io_counters()

    return {
        "total": disk_usage.total,
        "used": disk_usage.used,
        "free": disk_usage.free,
        "read_count": disk_io_counters.read_count,
        "write_count": disk_io_counters.write_count,
        "read_bytes": disk_io_counters.read_bytes,
        "write_bytes": disk_io_counters.write_bytes
    }

@app.get("/network/")
def get_network(request: Request, user: Annotated[dict, Depends(authenticate_user)]):
    
    update_monitor_data()

    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    
    net_io_counters = psutil.net_io_counters()
    
    return {
        "bytes_sent": net_io_counters.bytes_sent,
        "bytes_recv": net_io_counters.bytes_recv,
        "packets_sent": net_io_counters.packets_sent,
        "packets_recv": net_io_counters.packets_recv,
        "connections": [
            {
                "local_address": conn.laddr,
                "remote_address": conn.raddr,
                "status": conn.status,
                "pid": conn.pid
            }
            for conn in psutil.net_connections()
        ]
    }

@app.get("/temp/")
def get_temperature(request: Request, user: Annotated[dict, Depends(authenticate_user)]):
    
    update_monitor_data()

    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)

    return {"temperature": [temp_history[i][-1] for i in range(len(temp_history))]}
