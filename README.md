# Arch Linux with pyinfra

## What's inside

| File                                             | Description                                    |
| :----------------------------------------------- | :--------------------------------------------- |
| [./src/deploy.py](./src/deploy.py)               | Setup Arch Linux system from zero installation |
| [./src/mime.py](./src/mime.py)                   | Setup XDG MIME Applications                    |
| [./src/wayland/base.py](./src/wayland/base.py)   | Setup Wayland environment                      |
| [./src/wayland/labwc.py](./src/wayland/labwc.py) | Setup Labwc compositor                         |

## How to deploy this

> [!IMPORTANT]
> If you install Wayland, don't forget to run `sudo usermod -aG seat $USER` after installation.

### On local machine

```bash
pyinfra @local ./src/deploy.py
```

### On remote machine

```bash
pyinfra --ssh-user admin --ssh-key ~/.ssh/id_ed25519 192.168.0.100 ./src/deploy.py
```

### On many remote machines

Copy `inventory.py.example` to `inventory.py`, setup your hosts like official [Create a Deploy](https://docs.pyinfra.com/en/3.x/getting-started.html#create-a-deploy) docs and run:

```bash
pyinfra --ssh-user admin --ssh-key ~/.ssh/id_ed25519 inventory.py ./src/deploy.py
```

## License

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg?style=flat-square)](https://opensource.org/licenses/MIT)

This project is licensed under the terms of the [MIT](https://opensource.org/licenses/MIT) license (see [LICENSE](https://github.com/zsxoff/archlinux-pyinfra/blob/main/LICENSE) file).
