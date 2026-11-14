"""Command line interface: the "spectrometer" command"""

import argparse

from spectrometer.stream import start_stream


def main(argv=None):
    parser = argparse.ArgumentParser(prog="spectrometer", description="Raspberry Pi spectrometer")
    commands = parser.add_subparsers(dest="command", required=True)

    stream_parser = commands.add_parser("stream", help="show the live camera on the monitor")
    stream_parser.add_argument("--fullscreen", action="store_true", help="fill the whole screen")
    stream_parser.add_argument("--framerate", type=int, default=30)

    args = parser.parse_args(argv)
    if args.command == "stream":
        try:
            start_stream(args.fullscreen, args.framerate)
        except RuntimeError as error:
            parser.exit(1, f"error: {error}\n")


if __name__ == "__main__":
    main()
