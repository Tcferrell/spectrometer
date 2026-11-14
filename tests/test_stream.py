import pytest

from spectrometer import stream


def test_build_command_defaults():
    command = stream.build_command()
    assert command[0] == "rpicam-hello"
    assert command[command.index("-t") + 1] == "0"
    assert "--fullscreen" not in command


def test_build_command_fullscren():
    command = stream.build_command(fullscreen=True)
    assert "--fullscreen" in command


def test_build_command_framerate():
    command = stream.build_command(framerate=15)
    assert command[command.index("--framerate") + 1] == "15"


def test_stream_without_rpicam(monkeypatch):
    monkeypatch.setattr(stream.shutil, "which", lambda name: None)
    with pytest.raises(RuntimeError):
        stream.start_stream()
