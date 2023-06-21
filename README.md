# Python as a systemd service

**run a python function as a systemd service. Having exceptions handling with a custom mail sent in case of a critical error, and complete logging with traceback.**

# Requirements
- Python 3.10+
- pip
- git
- Linux based system running on systemd

# Setup
1. Clone the repository and install its dependencies.
```
 git clone https://github.com/willnaoosmith/Python-systemd-service
 cd Python-systemd-service
 pip install -r requirements.txt
```

2. Edit `main.py` to your desired use.

3. Edit the `service.service` file with your service name, user, and directory, also renaming it to your desired service name.

4. Move your `.service` file to `/lib/systemd/system/`.

5. Reload your systemd Daemon and try out your service!
```
systemctl daemon-reload
sudo systemctl start YourServiceNameHere
sudo systemctl status YourServiceNameHere
```

# Todo
1. Pooling on the MySQL connector, as made [here](https://stackoverflow.com/questions/32658679/how-to-create-a-mysql-connection-pool-or-any-better-way-to-initialize-the-multip)
