<h1 align="center">TorNetX <img src="https://cdn.pixabay.com/animation/2024/02/25/18/24/18-24-37-183_512.gif" width="40px"></h1>

<p align="center">
<a href="https://pypi.python.org/pypi/tornetx" rel="nofollow">
  <img src="http://img.shields.io/pypi/v/tornetx.png" alt="pypi">
</a>
</p>

> **TorNetX** is a fork of [TorNet](https://github.com/ByteBreach/tornet/) adapted for Windows and Mac, extending compatibility while providing the same automatic IP change benefits via the Tor network to enhance online security and anonymity.

<img alt="TorNetX" src="https://bytebreach.github.io/img/port.png" width="700"/>

## 📥 Installation

1. **Install [Tor](https://www.torproject.org/fr/download/)**:

2. **Add `tor.exe` to the System Path : System's Environment Variables**:

   (e.g., `C:\Program Files\Tor Browser\Browser\TorBrowser\Tor\tor.exe`)

4. **Install [Python](https://www.python.org/downloads/) and pip**:

5. **Install TorNetX**:

   ```bash
   pip install tornetx
   ```

## 🛠️ Usage

TorNetX provides a command-line interface for easy use. Here are the available options:

   ```bash
   tornetx --interval <seconds> --count <number>
```
- `--interval` (optional) : Time in seconds between IP changes (default is 60 seconds).
- `--count` (optional) : Nb of times to change the IP. If set to 0, the IP will be changed - indefinitely.
- `--stop` (optional) : Stop all Tor services and TorNet processes and exit.
- `--ip` (optional) : Display the current IP address and exit.
- `--auto-fix` (optional) : Automatically fix issues (install/upgrade packages).
- `--help` : Show the help message and exit.
- `--version` : Show the version number and exit.
