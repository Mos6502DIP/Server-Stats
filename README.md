# Server stats

Server stats is a simple way to get basic system info with a simple api request with more features planed.
Currently, you are able to ge the temp, uptime and cpu utilisation. With more system info being available in the future.

## Compatibility

Currently, i have been able to test on a hp prolient, Dell power edge and raspberry pi (running ubuntu server.).
I believe that it should be compatible with most systems running ubuntu server.

# Setup

Start by downloading the repo

### Server requirements

```bash
sudo apt-get install lm-sensors
sudo sensors-detect
```

### Python library's
(note this requires python 3)
```Bash
pip install psutil
pip install flask
```

## Run
### To run (basic)
```bash
python3 app.py
```
### To run (advanced)

I have made a guide to deploy a flask application using nginx and gunicorn which you can use to deploy this.
[Google Docs guide](https://docs.google.com/document/d/1wu7clIfKV04Ki3q2lx0FEz2CeuAbyuPNfX3itJxdrU0/edit?usp=sharing)

# Contributing

While this is a personal project, contributions are welcome! Please follow these steps to contribute:

1. Fork the repository.
2. Create a feature branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a pull request.

There will be a list of features at the bottom of the page for future updates that I am planning to work on feel free to give them a shot any help is appreciated.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

# Features to add

- Disk usage
- Recording data over time (Storing this in a csv or db)
- Waring (via email) if temp or usage goes over
- Ping

