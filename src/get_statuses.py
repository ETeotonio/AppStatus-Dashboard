import requests

class status:
    def get_status(self,configs):
        service_status=dict()
        i=0
        for config in configs['hosts']: 
            health_check=''
            version_check=''
            if ('http' not in config['host']['address']) :
                if ('https' not in config['host']['address']):
                    print('Protocol not specified - using http as default')
                    health_check='http://'
                    version_check='http://'
            health_check=health_check+config['host']['address']+config['host']['health_check']
            try:
                health_check_test = requests.get(health_check,timeout=5)
                health_check=False
                if health_check_test.status_code==200:
                    health_status = True
                else:
                    health_status = False
            except requests.exceptions.RequestException:
                health_status=False
            version_check=version_check+config['host']['address']+config['host']['version_check']
            try:
                version_check_test = requests.get(version_check,timeout=5)
                version_number=''
                if version_check_test.status_code==200:
                    version_number = version_check_test.text
                else:
                    version_number = False
            except requests.exceptions.RequestException:
                version_number=False
            service_status[i] = {'app_name':config['host']['app_name'],'status': health_status,'version':version_number}
            i+=1
        return service_status
            