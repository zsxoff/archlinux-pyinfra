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
