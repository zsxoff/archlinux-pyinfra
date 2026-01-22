from pyinfra.operations import pacman

TERMINAL = "alacritty"
LAUNCHER_PACKAGE = "rofi"
LAUNCHER_COMMAND = "-show run"

pacman.packages(
    name="Desktop - Install Xfce",
    packages=[
        "xfce4",
        "xfce4-screensaver",
        "xfce4-screenshooter",
        LAUNCHER_PACKAGE,
        TERMINAL,
    ],
    present=True,
    _sudo=True,
)

pacman.packages(
    name="Desktop - Install GVfs",
    packages=[
        "gvfs",
    ],
    present=True,
    _sudo=True,
)
