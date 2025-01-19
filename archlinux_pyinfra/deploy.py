from pyinfra import config
from pyinfra.operations import pacman, server, systemd

config.SUDO = True

# ----------------------------------------------------------------------------------------------------------------------
# Locales

server.shell(
    name="Locale - Generate en_US and ru_RU locales",
    commands=[
        'echo "en_US.UTF-8 UTF-8" > /etc/locale.gen',
        'echo "ru_RU.UTF-8 UTF-8" >> /etc/locale.gen',
        "locale-gen",
    ],
)

# ----------------------------------------------------------------------------------------------------------------------
# Network

pacman.packages(
    name="Network - Install NetworkManager",
    packages=["networkmanager", "wpa_supplicant"],
    present=True,
)

systemd.service(
    name="Network - Enable the NetworkManager service",
    service="NetworkManager.service",
    running=True,
    enabled=True,
)

pacman.packages(
    name="Network - Install wireless-regdb",
    packages=["wireless-regdb"],
    present=True,
)

server.shell(
    name="Network - Set regdomain to RU",
    commands=['echo "WIRELESS_REGDOM="RU"" > /etc/conf.d/wireless-regdom'],
)

# ----------------------------------------------------------------------------------------------------------------------
# Time

server.shell(
    name="Time - Set timezone to Europe/Moscow",
    commands=[
        "rm -rf /etc/localtime",
        "ln -s /usr/share/zoneinfo/Europe/Moscow /etc/localtime",
        "hwclock --systohc",
    ],
)

pacman.packages(
    name="Time - Install chrony",
    packages=["chrony"],
    present=True,
)

systemd.service(
    name="Time - Enable the chrony service",
    service="chronyd.service",
    running=True,
    enabled=True,
)

systemd.service(
    name="Time - Disable the systemd-timesyncd service",
    service="systemd-timesyncd.service",
    running=False,
    enabled=False,
)

# ----------------------------------------------------------------------------------------------------------------------
# Filesystem

pacman.packages(
    name="Filesystem - Install filesystem packages",
    packages=[
        "btrfs-progs",
        "dosfstools",
        "exfat-utils",
        "mtools",
        "nfs-utils",
        "ntfs-3g",
        "xfsprogs",
    ],
    present=True,
)

systemd.service(
    name="Filesystem - Enable fstrim.timer",
    service="fstrim.timer",
    running=True,
    enabled=True,
)

# ----------------------------------------------------------------------------------------------------------------------
# Firmware

pacman.packages(
    name="Firmware - Install Linux Firmware",
    packages=["linux-firmware"],
    present=True,
)

pacman.packages(
    name="Firmware - Install Intel microcode",
    packages=["intel-ucode"],
    present=True,
)

pacman.packages(
    name="Firmware - Install tool to manipulate Intel® IA-32/X86-64 microcode bundles",
    packages=["iucode-tool"],
    present=True,
)

server.modprobe(
    name="Firmware - Load the cpuid kernel module",
    module="cpuid",
    present=True,
)

# ----------------------------------------------------------------------------------------------------------------------
# Audio

pacman.packages(
    name="Audio - Install Pipewire",
    packages=["pipewire", "pipewire-alsa", "pipewire-jack", "pipewire-pulse", "wireplumber"],
    present=True,
)

# ----------------------------------------------------------------------------------------------------------------------
# Bluetooth

pacman.packages(
    name="Bluetooth - Install bluez",
    packages=["bluez", "bluez-libs", "bluez-utils", "blueman"],
    present=True,
)

systemd.service(
    name="Bluetooth - Enable the bluetooth service",
    service="bluetooth.service",
    running=True,
    enabled=True,
)

# ----------------------------------------------------------------------------------------------------------------------
# Polkit

pacman.packages(
    name="Polkit - Install polkit",
    packages=["polkit"],
    present=True,
)

# ----------------------------------------------------------------------------------------------------------------------
# Python

pacman.packages(
    name="Python - Install Python",
    packages=["python"],
    present=True,
)

pacman.packages(
    name="Python - Install Python tools",
    packages=["python-pip", "python-pipx", "python-setuptools"],
    present=True,
)

# ----------------------------------------------------------------------------------------------------------------------
# Go

pacman.packages(
    name="Go - Install Go",
    packages=["go"],
    present=True,
)

# ----------------------------------------------------------------------------------------------------------------------
# NodeJS

pacman.packages(
    name="NodeJS - Install NodeJS",
    packages=["nodejs"],
    present=True,
)

pacman.packages(
    name="NodeJS - Install npm",
    packages=["npm"],
    present=True,
)

# ----------------------------------------------------------------------------------------------------------------------
# Java

pacman.packages(
    name="Java - Install OpenJDK",
    packages=["jdk-openjdk"],
    present=True,
)

# ----------------------------------------------------------------------------------------------------------------------
# Fonts

pacman.packages(
    name="Fonts - Install fontconfig",
    packages=["fontconfig"],
    present=True,
)

pacman.packages(
    name="Fonts - Install fonts",
    packages=[
        "adobe-source-code-pro-fonts",
        "cantarell-fonts",
        "gnu-free-fonts",
        "noto-fonts-cjk",
        "noto-fonts-emoji",
        "noto-fonts-extra",
        "noto-fonts",
        "otf-font-awesome",
        "ttf-bitstream-vera",
        "ttf-croscore",
        "ttf-dejavu",
        "ttf-droid",
        "ttf-fira-code",
        "ttf-fira-mono",
        "ttf-fira-sans",
        "ttf-ibm-plex",
        "ttf-jetbrains-mono-nerd",
        "ttf-jetbrains-mono",
        "ttf-liberation",
        "ttf-nerd-fonts-symbols-common",
        "ttf-nerd-fonts-symbols-mono",
        "ttf-nerd-fonts-symbols",
        "ttf-opensans",
        "ttf-roboto-mono",
        "ttf-roboto",
        "ttf-ubuntu-font-family",
    ],
    present=True,
)

server.shell(name="Fonts - Generate fc-cache", commands=["fc-cache -f -v"])

# ----------------------------------------------------------------------------------------------------------------------
# Tools

pacman.packages(
    name="Tools - Install pacman-contrib",
    packages=["pacman-contrib"],
    present=True,
)

pacman.packages(
    name="Tools - Install base-devel",
    packages=["base-devel"],
    present=True,
)

pacman.packages(
    name="Tools - Install development packages",
    packages=["cmake", "gcc", "make", "meson", "ninja"],
    present=True,
)

pacman.packages(
    name="Tools - Install system tools",
    packages=["file", "hwinfo", "hwloc", "upower", "usbmuxd", "usbutils"],
    present=True,
)

pacman.packages(
    name="Tools - Install base tools",
    packages=[
        "bash-completion",
        "bat",
        "curl",
        "fd",
        "fzf",
        "git",
        "highlight",
        "jq",
        "nano",
        "ripgrep",
        "ripgrep-all",
        "rsync",
        "starship",
        "wget",
        "yazi",
        "yq",
        "zellij",
        "zoxide",
        "zsh",
    ],
    present=True,
)

pacman.packages(
    name="Tools - Install archive tools",
    packages=["7zip", "atool", "tar", "unrar", "unzip", "xz", "zip", "zstd"],
    present=True,
)

pacman.packages(
    name="Tools - Install hunspell",
    packages=["hunspell", "hunspell-en_us", "hunspell-ru"],
    present=True,
)

# ----------------------------------------------------------------------------------------------------------------------
# Performance

pacman.packages(
    name="Performance - Install memtest86+-efi",
    packages=["memtest86+-efi"],
    present=True,
)

pacman.packages(
    name="Performance - Install systemtap",
    packages=["systemtap"],
    present=True,
)

pacman.packages(
    name="Performance - Install wireless_tools",
    packages=["wireless_tools"],
    present=True,
)

pacman.packages(
    name="Performance - Install cpupower",
    packages=["cpupower"],
    present=True,
)

systemd.service(
    name="Performance - Enable cpupower.service",
    service="cpupower.service",
    running=True,
    enabled=True,
)

pacman.packages(
    name="Performance - Install thermald",
    packages=["thermald"],
    present=True,
)

systemd.service(
    name="Performance - Enable thermald.service",
    service="thermald.service",
    running=True,
    enabled=True,
)

pacman.packages(
    name="Performance - Install tuned-ppd",
    packages=["tuned-ppd"],
    present=True,
)

systemd.service(
    name="Performance - Enable tuned.service",
    service="tuned.service",
    running=True,
    enabled=True,
)

systemd.service(
    name="Performance - Enable tuned-ppd.service",
    service="tuned-ppd.service",
    running=True,
    enabled=True,
)

pacman.packages(
    name="Performance - Install fwupd",
    packages=["fwupd", "dmidecode"],
    present=True,
)

systemd.service(
    name="Performance - Enable fwupd-refresh.timer",
    service="fwupd-refresh.timer",
    running=True,
    enabled=True,
)

# ----------------------------------------------------------------------------------------------------------------------
# Desktop

pacman.packages(
    name="Desktop - Install media",
    packages=[
        "ffmpeg",
        "ffmpegthumbnailer",
        "gst-libav",
        "gst-plugin-pipewire",
        "gst-plugin-va",
        "gst-plugins-bad-libs",
        "gst-plugins-bad",
        "gst-plugins-base-libs",
        "gst-plugins-base",
        "gst-plugins-good",
        "gst-plugins-ugly",
        "gstreamer",
        "imagemagick",
        "x264",
        "x265",
    ],
    present=True,
)

pacman.packages(
    name="Desktop - Install GTK",
    packages=["gtk3", "gtk4", "libappindicator-gtk3", "webkit2gtk"],
    present=True,
)

pacman.packages(
    name="Desktop - Install Qt",
    packages=["qt5-base", "qt5-svg", "qt5-wayland", "qt6-base", "qt6-svg", "qt6-wayland"],
    present=True,
)

pacman.packages(
    name="Desktop - Install terminal",
    packages=["kitty"],
    present=True,
)

pacman.packages(
    name="Desktop - Install Firefox",
    packages=["firefox"],
    present=True,
)

pacman.packages(
    name="Desktop - Install MPV",
    packages=["mpv"],
    present=True,
)

pacman.packages(
    name="Desktop - Install KeePassXC",
    packages=["keepassxc"],
    present=True,
)

pacman.packages(
    name="Desktop - Install GDM",
    packages=["gdm"],
    present=True,
)

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
        "papirus-icon-theme",
        "python-pygments",
        "rygel",
        "snapshot",
        "sushi",
        "tecla",
        "xdg-desktop-portal-gnome",
        "xdg-user-dirs-gtk",
    ],
    present=True,
)

pacman.packages(
    name="Desktop - Install wl-clipboard",
    packages=["wl-clipboard"],
    present=True,
)

systemd.service(
    name="Desktop - Enable gdm.service",
    service="gdm.service",
    running=True,
    enabled=True,
)

server.shell(
    name="Desktop - Enable graphical.target",
    commands=["systemctl set-default graphical.target"],
)


# ----------------------------------------------------------------------------------------------------------------------
# sysctl

server.sysctl(
    name="sysctl - Enable tcp_window_scaling",
    key="net.ipv4.tcp_window_scaling",
    value=1,
    persist=True,
)
