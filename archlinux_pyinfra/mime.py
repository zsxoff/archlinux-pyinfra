from pyinfra.operations import server

# ----------------------------------------------------------------------------------------------------------------------
# xdg-mime

application_mimetype = [
    ("firefox.desktop", "text/html"),
    ("imv.desktop", "image/jpeg"),
    ("imv.desktop", "image/png"),
    ("mpv.desktop", "audio/flac"),
    ("mpv.desktop", "audio/mp3"),
    ("mpv.desktop", "audio/mp4"),
    ("mpv.desktop", "audio/wav"),
    ("mpv.desktop", "video/mp4"),
    ("org.pwmt.zathura.desktop", "application/pdf"),
]

server.shell(
    name="xdg-mime - Set application and mimetype",
    commands=[f"xdg-mime default {application} {mimetype}" for application, mimetype in application_mimetype],
)
