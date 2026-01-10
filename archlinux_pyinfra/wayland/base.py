from pyinfra.operations import pacman, systemd

# Display manager (https://github.com/fairyglade/ly)

pacman.packages(
    name="Display manager - Install ly",
    packages=[
        "ly",
    ],
    present=True,
    _sudo=True,
)

systemd.service(
    name="Display manager - Enable the ly@tty1.service",
    service="ly@tty1.service",
    running=True,
    enabled=True,
    _sudo=True,
)

systemd.service(
    name="Display manager - Disable the getty@tty1.service",
    service="getty@tty1.service",
    running=True,
    enabled=True,
    _sudo=True,
)

# seat (https://man.archlinux.org/man/seatd.1.en)

pacman.packages(
    name="seat - Install seatd",
    packages=[
        "seatd",
    ],
    present=True,
    _sudo=True,
)

systemd.service(
    name="seat - Enable the seatd.service",
    service="seatd.service",
    running=True,
    enabled=True,
    _sudo=True,
)

# Polkit (https://wiki.archlinux.org/title/Polkit)

pacman.packages(
    name="Polkit - Install polkit and backend",
    packages=[
        "polkit",
        "polkit-gnome",
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

# Software

pacman.packages(
    name="Wayland - Install needed software",
    packages=[
        "brightnessctl",
        "grim",
        "mako",
        "slurp",
        "sway-contrib",
        "swaybg",
        "swayidle",
        "swaylock",
        "wlr-randr",
    ],
    present=True,
    _sudo=True,
)

pacman.packages(
    name="Wayland - Install additional software",
    packages=[
        "imv",
        "playerctl",
    ],
    present=True,
    _sudo=True,
)
