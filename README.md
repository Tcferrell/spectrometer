# Spectrometer

A DIY Czerny-Turner  spectrometer built on a Raspberry Pi 4 and an Arducam IMX477 camera.

> **Status:** early development. Not yet usable.

## Hardware

- Raspberry Pi 4
- Arducam IMX477 (12.3MP) camera
- Diffraction grating *(details to come)*

## Requirements

- Raspberry Pi OS (64-bit, Bookworm or newer)
- Python 3.11+

## Installation

```bash
git clone git@github.com:Tcferrell/spectrometer.git
cd spectrometer
python3 -m venv .venv --system-site-packages
source .venv/bin/activate
pip install -e ".[dev]"
```

## Usage

*Coming soon.*

## Development

Set up the pre-commit hooks once:

```bash
pre-commit install
```

Run the tests:

```bash
pytest
```

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.
