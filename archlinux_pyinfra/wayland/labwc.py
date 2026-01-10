from pyinfra.operations import pacman

# Labwc

pacman.packages(
    name="Desktop - Install Labwc",
    packages=[
        "kitty",
        "labwc",
        "rofi",
        "waybar",
    ],
    present=True,
    _sudo=True,
)

# XDG Desktop Portal (https://wiki.archlinux.org/title/XDG_Desktop_Portal)

pacman.packages(
    name="xdg-desktop-portal - Install xdg-desktop-portal and backend",
    packages=[
        "xdg-desktop-portal",
        "xdg-desktop-portal-wlr",
    ],
    present=True,
    _sudo=True,
)
