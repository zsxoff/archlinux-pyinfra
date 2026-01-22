from pyinfra.operations import server

# xdg-mime

application_mimetypes: dict[str, list[str]] = {
    "firefox.desktop": [
        "text/html",
    ],
    "mpv.desktop": [
        "audio/flac",
        "audio/mp3",
        "audio/mp4",
        "audio/wav",
        "video/mp4",
    ],
    "imv.desktop": [
        "image/jpeg",
        "image/png",
    ],
    "org.pwmt.zathura.desktop": [
        "application/pdf",
    ],
}

server.shell(
    name="xdg-mime - Set application and mimetype",
    commands=[
        f"xdg-mime default {application} {mimetype}"
        for application, mimetypes in application_mimetypes.items()
        for mimetype in mimetypes
    ],
)
