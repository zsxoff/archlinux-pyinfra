from typing import NamedTuple

from pyinfra.operations import pacman, server, systemd


# Locales

server.locale(
    name="Locales - Ensure en_US.UTF-8 locale is present",
    locale="en_US.UTF-8",
    _sudo=True,
)

server.locale(
    name="Locales - Ensure ru_RU.UTF-8 locale is present",
    locale="ru_RU.UTF-8",
    _sudo=True,
)

# Network

pacman.packages(
    name="Network - Install NetworkManager",
    packages=[
        "networkmanager",
        "wireless-regdb",
        "wpa_supplicant",
    ],
    present=True,
    _sudo=True,
)

systemd.service(
    name="Network - Enable the NetworkManager service",
    service="NetworkManager.service",
    running=True,
    enabled=True,
    _sudo=True,
)

server.shell(
    name="Network - Set regdomain to RU",
    commands=['echo "WIRELESS_REGDOM="RU"" > /etc/conf.d/wireless-regdom'],
    _sudo=True,
)

systemd.service(
    name="Network - Enable the systemd-resolved service",
    service="systemd-resolved.service",
    running=True,
    enabled=True,
)

# Time

server.timezone(
    name="Time - Set the timezone to Europe/Moscow",
    timezone="Europe/Moscow",
    _sudo=True,
)

pacman.packages(
    name="Time - Install chrony",
    packages=[
        "chrony",
    ],
    present=True,
    _sudo=True,
)

systemd.service(
    name="Time - Disable the systemd-timesyncd service",
    service="systemd-timesyncd.service",
    running=False,
    enabled=False,
    _sudo=True,
)

systemd.service(
    name="Time - Enable the chrony service",
    service="chronyd.service",
    running=True,
    enabled=True,
    _sudo=True,
)

# Filesystem

pacman.packages(
    name="Filesystem - Install filesystem packages",
    packages=[
        "btrfs-progs",
        "dosfstools",
        "exfat-utils",
        "mdadm",
        "mtools",
        "nfs-utils",
        "ntfs-3g",
        "parted",
        "xfsprogs",
    ],
    present=True,
    _sudo=True,
)

systemd.service(
    name="Filesystem - Enable fstrim.timer",
    service="fstrim.timer",
    running=True,
    enabled=True,
    _sudo=True,
)

# Firmware

pacman.packages(
    name="Firmware - Install Linux Firmware",
    packages=["linux-firmware"],
    present=True,
    _sudo=True,
)

pacman.packages(
    name="Firmware - Install Intel microcode",
    packages=["intel-ucode"],
    present=True,
    _sudo=True,
)

pacman.packages(
    name="Firmware - Install tool to manipulate Intel® IA-32/X86-64 microcode bundles",
    packages=["iucode-tool"],
    present=True,
    _sudo=True,
)

server.modprobe(
    name="Firmware - Load the cpuid kernel module",
    module="cpuid",
    present=True,
    _sudo=True,
)

# Audio

pacman.packages(
    name="Audio - Install Pipewire",
    packages=[
        "pipewire",
        "pipewire-alsa",
        "pipewire-jack",
        "pipewire-pulse",
        "wireplumber",
    ],
    present=True,
    _sudo=True,
)

# Bluetooth

pacman.packages(
    name="Bluetooth - Install bluez",
    packages=[
        "blueman",
        "bluez",
        "bluez-utils",
    ],
    present=True,
    _sudo=True,
)

systemd.service(
    name="Bluetooth - Enable the bluetooth service",
    service="bluetooth.service",
    running=True,
    enabled=True,
    _sudo=True,
)

# Fonts

pacman.packages(
    name="Fonts - Install fontconfig & fonts",
    packages=[
        "fontconfig",
        "adobe-source-code-pro-fonts",
        "cantarell-fonts",
        "gnu-free-fonts",
        "noto-fonts",
        "noto-fonts-cjk",
        "noto-fonts-emoji",
        "noto-fonts-extra",
        "otf-font-awesome",
        "ttf-bitstream-vera",
        "ttf-croscore",
        "ttf-dejavu",
        "ttf-droid",
        "ttf-fira-code",
        "ttf-fira-mono",
        "ttf-fira-sans",
        "ttf-hack",
        "ttf-ibm-plex",
        "ttf-jetbrains-mono",
        "ttf-jetbrains-mono-nerd",
        "ttf-liberation",
        "ttf-nerd-fonts-symbols",
        "ttf-nerd-fonts-symbols-common",
        "ttf-nerd-fonts-symbols-mono",
        "ttf-opensans",
        "ttf-roboto",
        "ttf-roboto-mono",
        "ttf-ubuntu-font-family",
    ],
    present=True,
    _sudo=True,
)

server.shell(
    name="Fonts - Generate fc-cache",
    commands=[
        "fc-cache -f -v",
    ],
    _sudo=True,
)

# Tools

pacman.packages(
    name="Tools - Install pacman-contrib",
    packages=[
        "pacman-contrib",
    ],
    present=True,
    _sudo=True,
)

pacman.packages(
    name="Tools - Install base-devel",
    packages=[
        "base-devel",
    ],
    present=True,
    _sudo=True,
)

pacman.packages(
    name="Tools - Install system tools",
    packages=[
        "bolt",
        "file",
        "hwinfo",
        "hwloc",
        "upower",
        "usbmuxd",
        "usbutils",
    ],
    present=True,
    _sudo=True,
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
        "mlocate",
        "nano",
        "python-pygments",
        "ripgrep",
        "ripgrep-all",
        "skim",
        "starship",
        "wget",
        "yazi",
        "yq",
        "zoxide",
        "zsh",
    ],
    present=True,
    _sudo=True,
)

pacman.packages(
    name="Tools - Install archive tools",
    packages=[
        "7zip",
        "atool",
        "tar",
        "unrar",
        "unzip",
        "xz",
        "zip",
        "zstd",
    ],
    present=True,
    _sudo=True,
)

pacman.packages(
    name="Tools - Install hunspell",
    packages=[
        "hunspell",
        "hunspell-en_us",
        "hunspell-ru",
    ],
    present=True,
    _sudo=True,
)

# Performance

pacman.packages(
    name="Performance - Install memtest86+-efi",
    packages=["memtest86+-efi"],
    present=True,
    _sudo=True,
)

pacman.packages(
    name="Performance - Install systemtap",
    packages=["systemtap"],
    present=True,
    _sudo=True,
)

pacman.packages(
    name="Performance - Install wireless_tools",
    packages=["wireless_tools"],
    present=True,
    _sudo=True,
)

pacman.packages(
    name="Performance - Install cpupower",
    packages=["cpupower"],
    present=True,
    _sudo=True,
)

systemd.service(
    name="Performance - Enable cpupower.service",
    service="cpupower.service",
    running=True,
    enabled=True,
    _sudo=True,
)

pacman.packages(
    name="Performance - Install thermald",
    packages=["thermald"],
    present=True,
    _sudo=True,
)

systemd.service(
    name="Performance - Enable thermald.service",
    service="thermald.service",
    running=True,
    enabled=True,
    _sudo=True,
)

pacman.packages(
    name="Performance - Install tuned-ppd",
    packages=["tuned-ppd"],
    present=True,
    _sudo=True,
)

systemd.service(
    name="Performance - Enable tuned.service",
    service="tuned.service",
    running=True,
    enabled=True,
    _sudo=True,
)

systemd.service(
    name="Performance - Enable tuned-ppd.service",
    service="tuned-ppd.service",
    running=True,
    enabled=True,
    _sudo=True,
)

pacman.packages(
    name="Performance - Install fwupd",
    packages=[
        "dmidecode",
        "fwupd",
    ],
    present=True,
    _sudo=True,
)

# systemd.service(
#     name="Performance - Enable fwupd-refresh.timer",
#     service="fwupd-refresh.timer",
#     running=True,
#     enabled=True,
#     _sudo=True,
# )

systemd.service(
    name="Performance - Enable nvidia-powerd.service",
    service="nvidia-powerd.service",
    running=True,
    enabled=True,
    _sudo=True,
)

pacman.packages(
    name="Performance - Install earlyoom",
    packages=["earlyoom"],
    present=True,
    _sudo=True,
)

systemd.service(
    name="Performance - Enable earlyoom.service",
    service="earlyoom.service",
    running=True,
    enabled=True,
    _sudo=True,
)

# paccache

systemd.service(
    name="paccache - Enable paccache.timer",
    service="paccache.timer",
    running=True,
    enabled=True,
    _sudo=True,
)

# Desktop

pacman.packages(
    name="Desktop - Install media",
    packages=[
        "ffmpeg",
        "ffmpegthumbnailer",
        "gst-libav",
        "gst-plugin-pipewire",
        "gst-plugin-va",
        "gst-plugins-bad",
        "gst-plugins-bad-libs",
        "gst-plugins-base",
        "gst-plugins-base-libs",
        "gst-plugins-good",
        "gst-plugins-ugly",
        "gstreamer",
        "imagemagick",
        "x264",
        "x265",
    ],
    present=True,
    _sudo=True,
)

pacman.packages(
    name="Desktop - Install GTK",
    packages=[
        "gtk3",
        "gtk4",
        "libappindicator",
        "webkitgtk-6.0",
    ],
    present=True,
    _sudo=True,
)

pacman.packages(
    name="Desktop - Install colord",
    packages=[
        "colord",
        "colord-gtk",
        "colord-gtk-common",
        "colord-gtk4",
    ],
    present=True,
    _sudo=True,
)

pacman.packages(
    name="Desktop - Install Qt",
    packages=[
        "qt5-base",
        "qt5-imageformats",
        "qt5-svg",
        "qt5-wayland",
        "qt6-base",
        "qt6-imageformats",
        "qt6-svg",
        "qt6-wayland",
    ],
    present=True,
    _sudo=True,
)

pacman.packages(
    name="Desktop - Install Desktop tools",
    packages=[
        "firefox",
        "foot",
        "imv",
        "mpv",
        "wl-clipboard",
        "zathura",
    ],
    present=True,
    _sudo=True,
)

# Tuning

server.shell(
    name="Tuning - Disable power safe mode on Wi-Fi",
    commands=[
        'echo \'ACTION=="add", SUBSYSTEM=="net", KERNEL=="wl*", RUN+="/usr/bin/iw dev $name set power_save off"\' > /etc/udev/rules.d/81-wifi-powersave.rules',  # noqa: E501
    ],
    _sudo=True,
)


# sysctl

SYSCTL_UDP_SOCKET_R_BUFFER_SIZE = 134217728
SYSCTL_UDP_SOCKET_W_BUFFER_SIZE = 134217728


class SysctlSetting(NamedTuple):
    key: str
    sysctl_value: int | list[str | int]


sysctl_settings: list[SysctlSetting] = [
    SysctlSetting("net.core.rmem_max", SYSCTL_UDP_SOCKET_R_BUFFER_SIZE),
    SysctlSetting("net.core.wmem_max", SYSCTL_UDP_SOCKET_W_BUFFER_SIZE),
    SysctlSetting("net.ipv4.tcp_sack", 1),
    SysctlSetting("net.ipv4.tcp_timestamps", 1),
    SysctlSetting("net.ipv4.tcp_window_scaling", 1),
    SysctlSetting("net.ipv4.tcp_rmem", [4096, 87380, 134217728]),
    SysctlSetting("net.ipv4.tcp_wmem", [4096, 65536, 134217728]),
]

for sysctl_setting in sysctl_settings:  # noqa[WPS481]
    server.sysctl(
        name=f"sysctl - Set {sysctl_setting.key}",
        key=sysctl_setting.key,
        value=sysctl_setting.sysctl_value,
        persist=True,
        _sudo=True,
    )
