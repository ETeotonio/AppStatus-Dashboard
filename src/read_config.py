import yaml

class read_config_file:
    def read_yaml_config_file(self,config_file_path):
        with open(config_file_path,'r') as config_file:
            data = yaml.load(config_file,Loader=yaml.FullLoader)
        return data