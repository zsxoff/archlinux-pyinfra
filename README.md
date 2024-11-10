# Arch Linux with pyinfra

![Arch Linux with GNOME](./assets/archlinux.png)

## What's inside

See [./archlinux_pyinfra/deploy.py](./archlinux_pyinfra/deploy.py) file.

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

Better copy `inventory.py.example` to `inventory.py`, setup your hosts like official [Create a Deploy](https://docs.pyinfra.com/en/3.x/getting-started.html#create-a-deploy) docs, then run:

```bash
pyinfra --ssh-user admin --ssh-key ~/.ssh/id_ed25519 inventory.py ./archlinux_pyinfra/deploy.py
```

## License

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg?style=flat-square)](https://opensource.org/licenses/MIT)

This project is licensed under the terms of the [MIT](https://opensource.org/licenses/MIT) license (see [LICENSE](<https://github.com/zsxoff/archlinux-pyinfra/blob/master/LICENSE>) file).
