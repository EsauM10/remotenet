import httpx

class RemoteWorker:
    def __init__(self, ip: str) -> None:
        self.url        = f'http://{ip}:5000'
        self.is_running = False


    def add_controller(self, name: str, ip: str, port: int):
        data = {'name': name, 'ip': ip, 'port': port}
        response = httpx.post(url=f'{self.url}/controllers', json=data, timeout=None)
        
        if(response.is_error):
            raise Exception(response.json()['error'])
        print(f'{response.json()["content"]}')


    def start(self):
        response = httpx.get(url=f'{self.url}/start', timeout=None)
        
        if(response.is_error):
            raise Exception(response.json()['error'])
        self.is_running = True
        print(f'{response.json()["content"]}')


    def stop(self):
        response = httpx.get(url=f'{self.url}/stop', timeout=None)
        
        if(response.is_error):
            print(response.json()['error'])
        else:
            self.is_running = False
            print(f'{response.json()["content"]}')
