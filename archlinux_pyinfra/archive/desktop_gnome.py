from pyinfra.operations import pacman

pacman.packages(
    name="Desktop - Install Gnome",
    packages=[
        "baobab",
        "evince",
        "eyedropper",
        "file-roller",
        "gnome-backgrounds",
        "gnome-browser-connector",
        "gnome-calendar",
        "gnome-clocks",
        "gnome-color-manager",
        "gnome-contacts",
        "gnome-control-center",
        "gnome-disk-utility",
        "gnome-firmware",
        "gnome-font-viewer",
        "gnome-keyring",
        "gnome-logs",
        "gnome-menus",
        "gnome-music",
        "gnome-session",
        "gnome-settings-daemon",
        "gnome-shell-extensions",
        "gnome-shell",
        "gnome-system-monitor",
        "gnome-text-editor",
        "gnome-tweaks",
        "gnome-user-docs",
        "gnome-weather",
        "grilo-plugins",
        "gvfs-afc",
        "gvfs-dnssd",
        "gvfs-gphoto2",
        "gvfs-mtp",
        "gvfs-nfs",
        "gvfs-wsdd",
        "gvfs",
        "loupe",
        "nautilus",
        "rygel",
        "snapshot",
        "sushi",
        "tecla",
        "xdg-desktop-portal-gnome",
        "xdg-user-dirs-gtk",
    ],
    present=True,
    _sudo=True,
)

# pacman.packages(
#     name="Desktop - Install GDM",
#     packages=["gdm"],
#     present=True,
#     _sudo=True,
# )

# systemd.service(
#     name="Desktop - Enable gdm.service",
#     service="gdm.service",
#     running=True,
#     enabled=True,
#     _sudo=True,
# )

# server.shell(
#     name="Desktop - Enable graphical.target",
#     commands=["systemctl set-default graphical.target"],
#     _sudo=True,
# )
