import socket
import subprocess
from fastapi import FastAPI
from starlette.responses import FileResponse

app = FastAPI()


@app.get('/{title}')
def get_html(title: str):
    file_path = f'./rendered/{title}.html'
    return FileResponse(file_path, media_type="text/html")


def is_port_in_use(port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        return s.connect_ex(('localhost', port)) == 0


def run_fastapi():
    if not is_port_in_use(8000):
        fastapi_cmd = ["uvicorn", "serv:app", "--host", "0.0.0.0", "--port", "8000"]
        subprocess.run(fastapi_cmd)
