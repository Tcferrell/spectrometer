"""Begin a livestrean of the camera feed and display it in a window."""

import shutil
import subprocess


def build_command(fullscreen=False, framerate=30):
    command = ["rpicam-hello", "-t", "0", "--framerate", str(framerate)]
    if fullscreen:
        command.append("--fullscreen")

    return command


def start_stream(fullscreen=False, framerate=30):

    # Check to make sure the system has rpicam-apps
    if shutil.which("rpicam-hello") is None:
        raise RuntimeError("rpicam-hello not found: Install with: sudo apt install rpicam-apps")

    command = build_command(fullscreen=fullscreen, framerate=framerate)

    print("Beginning Stream")
    try:
        subprocess.run(command, check=True)
    except KeyboardInterrupt:
        print("\n--Stream Stopped--")
