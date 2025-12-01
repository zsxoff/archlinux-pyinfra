from pyinfra.operations import pacman, server

# --------------------------------------------------------------------------------------

# TODO(zsxoff): Complete this setup.

# --------------------------------------------------------------------------------------

TERMINAL = "alacritty"

pacman.packages(
    name="Desktop - Install Xfce",
    packages=[
        "xfce4",
        "xfce4-screensaver",
        "xfce4-screenshooter",
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


server.shell(
    # Show keybinds: `xfconf-query -c xfce4-keyboard-shortcuts -l -v`
    #
    name="Keybinds - Add Xfce keybinds",
    commands=[
        # Terminal
        f"xfconf-query -c xfce4-keyboard-shortcuts -p '/commands/custom/<Alt>Return' --create -v -t string -s ${TERMINAL}",
        # Change workspace
        "xfconf-query -c xfce4-keyboard-shortcuts -p '/xfwm4/custom/<Alt>1' --create -v -t string -s workspace_1_key",
        "xfconf-query -c xfce4-keyboard-shortcuts -p '/xfwm4/custom/<Alt>2' --create -v -t string -s workspace_2_key",
        "xfconf-query -c xfce4-keyboard-shortcuts -p '/xfwm4/custom/<Alt>3' --create -v -t string -s workspace_3_key",
        "xfconf-query -c xfce4-keyboard-shortcuts -p '/xfwm4/custom/<Alt>4' --create -v -t string -s workspace_4_key",
        "xfconf-query -c xfce4-keyboard-shortcuts -p '/xfwm4/custom/<Alt>5' --create -v -t string -s workspace_5_key",
        "xfconf-query -c xfce4-keyboard-shortcuts -p '/xfwm4/custom/<Alt>6' --create -v -t string -s workspace_6_key",
        "xfconf-query -c xfce4-keyboard-shortcuts -p '/xfwm4/custom/<Alt>7' --create -v -t string -s workspace_7_key",
        "xfconf-query -c xfce4-keyboard-shortcuts -p '/xfwm4/custom/<Alt>8' --create -v -t string -s workspace_8_key",
        "xfconf-query -c xfce4-keyboard-shortcuts -p '/xfwm4/custom/<Alt>9' --create -v -t string -s workspace_9_key",
        "xfconf-query -c xfce4-keyboard-shortcuts -p '/xfwm4/custom/<Alt>0' --create -v -t string -s workspace_10_key",
    ],
    _sudo=True,
)
