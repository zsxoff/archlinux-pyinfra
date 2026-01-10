# Arch Linux with pyinfra

## What's inside

| File                                                                         | Description                                    |
| :--------------------------------------------------------------------------- | :--------------------------------------------- |
| [./archlinux_pyinfra/deploy.py](./archlinux_pyinfra/deploy.py)               | Setup Arch Linux system from zero installation |
| [./archlinux_pyinfra/mime.py](./archlinux_pyinfra/mime.py)                   | Setup XDG MIME Applications                    |
| [./archlinux_pyinfra/wayland/base.py](./archlinux_pyinfra/wayland/base.py)   | Setup Wayland environment                      |
| [./archlinux_pyinfra/wayland/labwc.py](./archlinux_pyinfra/wayland/labwc.py) | Setup Labwc compositor                         |

## How to deploy this

### On local machine

```bash
pyinfra @local ./archlinux_pyinfra/deploy.py
```

### On remote machine

```bash
pyinfra --ssh-user admin --ssh-key ~/.ssh/id_ed25519 192.168.0.100 ./archlinux_pyinfra/deploy.py
```

### On many remote machines

Copy `inventory.py.example` to `inventory.py`, setup your hosts like official [Create a Deploy](https://docs.pyinfra.com/en/3.x/getting-started.html#create-a-deploy) docs and run:

```bash
pyinfra --ssh-user admin --ssh-key ~/.ssh/id_ed25519 inventory.py ./archlinux_pyinfra/deploy.py
```

## License

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg?style=flat-square)](https://opensource.org/licenses/MIT)

This project is licensed under the terms of the [MIT](https://opensource.org/licenses/MIT) license (see [LICENSE](https://github.com/zsxoff/archlinux-pyinfra/blob/master/LICENSE) file).
