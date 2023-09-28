# AppStatus-Dashboard

## Description
Dashboard to Monitor the Application Status, getting the version and checking if the service is up

## Pre-requisites
- Python 3.11
- Pip
- Virtualenv (Not mandatory but recommended)
- Packages on requirements.txt

### Installing Pre-requisites

```console
pip install -r requirements.txt
```

## Configuring the application
The configuration is read by the application from the config.yaml file. This file has the followin structure:
```yaml
---
hosts:
  - host:
      app_name: Your Application Name
      address: Your application address, if just the FQDN or IP, the application will automatically look for the http
      health_check: Path to your health check
      version_check: Path to your version check
```

## Starting the Application
On the src folder run:

```console
flask run
```

The application will automatically start on port 5000.

## Future Improvements
- Async call for the dashboard - to update in real time
- Set the update time on the front end
- Dockerize the application
- Improve the Dashboard interface - Currently just using Bootstrap