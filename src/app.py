from flask import Flask,render_template
import read_config
import get_statuses
import argparse


parser = argparse.ArgumentParser(description='Dashboard configs')
parser.add_argument(dest='config',action='store')
args = parser.parse_args()


if args.configs == None:
    config = 'config.yaml'
else:
    config=args.config

app=Flask(__name__)

@app.route('/')
def base_dashboard():
    return render_template('index.html')

@app.route('/api/statuses')
def api_statuses():
    config_data = read_config.read_config_file()
    yaml_data=config_data.read_yaml_config_file(config)
    status_config = get_statuses.status()
    status = status_config.get_status(yaml_data)
    return render_template('index.html',statuses=status)

@app.route('/api/get_config')
def get_config():
    config_data = read_config.read_config_file()
    yaml_data=config_data.read_yaml_config_file(config)
    return render_template('config.html',configs=yaml_data['hosts'])

@app.route('/api/version')
def get_version():
    return '0.0.1-beta'

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5001,debug=True)