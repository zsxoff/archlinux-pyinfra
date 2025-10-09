from pyinfra.operations import pacman, server, systemd

# --------------------------------------------------------------------------------------
# Locales

server.shell(
    name="Locale - Generate en_US and ru_RU locales",
    commands=[
        'echo "en_US.UTF-8 UTF-8" > /etc/locale.gen',
        'echo "ru_RU.UTF-8 UTF-8" >> /etc/locale.gen',
        "locale-gen",
    ],
    _sudo=True,
)

# --------------------------------------------------------------------------------------
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

# --------------------------------------------------------------------------------------
# Time

server.shell(
    name="Time - Set timezone to Europe/Moscow",
    commands=[
        "rm -rf /etc/localtime",
        "ln -s /usr/share/zoneinfo/Europe/Moscow /etc/localtime",
        "hwclock --systohc",
    ],
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

# --------------------------------------------------------------------------------------
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
    _sudo=True,
)

systemd.service(
    name="Filesystem - Enable fstrim.timer",
    service="fstrim.timer",
    running=True,
    enabled=True,
    _sudo=True,
)

# --------------------------------------------------------------------------------------
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

# --------------------------------------------------------------------------------------
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

# --------------------------------------------------------------------------------------
# Bluetooth

pacman.packages(
    name="Bluetooth - Install bluez",
    packages=[
        "blueman",
        "bluez",
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

# --------------------------------------------------------------------------------------
# Polkit

pacman.packages(
    name="Polkit - Install polkit",
    packages=[
        "polkit",
    ],
    present=True,
    _sudo=True,
)

# --------------------------------------------------------------------------------------
# Python

pacman.packages(
    name="Python - Install Python",
    packages=[
        "python",
    ],
    present=True,
    _sudo=True,
)

# --------------------------------------------------------------------------------------
# Fonts

pacman.packages(
    name="Fonts - Install fontconfig",
    packages=[
        "fontconfig",
    ],
    present=True,
    _sudo=True,
)

pacman.packages(
    name="Fonts - Install fonts",
    packages=[
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

# --------------------------------------------------------------------------------------
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
    name="Tools - Install development packages",
    packages=[
        "cmake",
        "gcc",
        "gdb",
        "make",
        "meson",
        "ninja",
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

# --------------------------------------------------------------------------------------
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

# --------------------------------------------------------------------------------------
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
        "libappindicator-gtk2",
        "libappindicator-gtk3",
        "webkit2gtk",
    ],
    present=True,
    _sudo=True,
)

pacman.packages(
    name="Desktop - Install colord",
    packages=[
        "colord",
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

# --------------------------------------------------------------------------------------
# Tuning

server.shell(
    name="Tuning - Disable power safe mode on Wi-Fi",
    commands=[
        'echo \'ACTION=="add", SUBSYSTEM=="net", KERNEL=="wl*", RUN+="/usr/bin/iw dev $name set power_save off"\' > /etc/udev/rules.d/81-wifi-powersave.rules',
    ],
    _sudo=True,
)

# --------------------------------------------------------------------------------------
# sysctl

server.sysctl(
    name="sysctl - Set net.ipv4.tcp_window_scaling",
    key="net.ipv4.tcp_window_scaling",
    value=1,
    persist=True,
    _sudo=True,
)
server.sysctl(
    name="sysctl - Set net.ipv4.tcp_timestamps",
    key="net.ipv4.tcp_timestamps",
    value=1,
    persist=True,
    _sudo=True,
)
server.sysctl(
    name="sysctl - Set net.ipv4.tcp_sack",
    key="net.ipv4.tcp_sack",
    value=1,
    persist=True,
    _sudo=True,
)
server.sysctl(
    name="sysctl - Set net.core.rmem_max",
    key="net.core.rmem_max",
    value=134217728,
    persist=True,
    _sudo=True,
)
server.sysctl(
    name="sysctl - Set net.core.wmem_max",
    key="net.core.wmem_max",
    value=134217728,
    persist=True,
    _sudo=True,
)
server.sysctl(
    name="sysctl - Set net.ipv4.tcp_rmem",
    key="net.ipv4.tcp_rmem",
    value=[4096, 87380, 134217728],
    persist=True,
    _sudo=True,
)
server.sysctl(
    name="sysctl - Set net.ipv4.tcp_wmem",
    key="net.ipv4.tcp_wmem",
    value=[4096, 65536, 134217728],
    persist=True,
    _sudo=True,
)
server.sysctl(
    name="sysctl - Set net.ipv4.tcp_wmem",
    key="net.ipv4.tcp_wmem",
    value=[4096, 65536, 134217728],
    persist=True,
    _sudo=True,
)
