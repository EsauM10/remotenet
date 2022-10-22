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

    
    def add_docker(self, name: str, **params):
        data = {'name': name, **params}
        response = httpx.post(url=f'{self.url}/containers', json=data, timeout=None)
        
        if(response.is_error):
            raise Exception(response.json()['error'])
        print(f'{response.json()["content"]}')


    def add_link(self, node1: str, node2: str, **params):
        data = {'node1': node1, 'node2': node2, **params}
        response = httpx.post(url=f'{self.url}/links', json=data, timeout=None)
        
        if(response.is_error):
            raise Exception(response.json()['error'])
        print(f'{response.json()["content"]}')


    def add_switch(self, name: str):
        data = {'name': name}
        response = httpx.post(url=f'{self.url}/switches', json=data, timeout=None)
        
        if(response.is_error):
            raise Exception(response.json()['error'])
        print(f'{response.json()["content"]}')
    

    def config_default(self, name: str):
        response = httpx.get(url=f'{self.url}/hosts/{name}/config', timeout=None)
        
        if(response.is_error):
            raise Exception(response.json()['error'])
        print(f'{response.json()["content"]}')
    

    def remove_docker(self, name: str):
        response = httpx.delete(url=f'{self.url}/containers/{name}', timeout=None)
        
        if(response.is_error):
            raise Exception(response.json()['error'])
        print(f'{response.json()["content"]}')


    def remove_link(self, node1: str, node2: str):
        data = {'node1': node1, 'node2': node2}
        response = httpx.post(url=f'{self.url}/links/remove', json=data, timeout=None)
        
        if(response.is_error):
            raise Exception(response.json()['error'])
        print(f'{response.json()["content"]}')


    def run_command(self, name: str, command: str):
        data = {'command': command}
        response = httpx.post(url=f'{self.url}/hosts/{name}/cmd', json=data, timeout=None)
        
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
