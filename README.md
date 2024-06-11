# Project NetProbeX

## Overview

Project NetProbeX aims to create a user-friendly Wireshark data analysis tool that facilitates a comprehensive understanding of Wireshark functionalities and proficient network data analysis. This tool enables users to capture network data, conduct thorough data analysis, and present insights through an intuitive graphical user interface (GUI). Developed primarily in Python, this project enhances members' expertise in network analysis.

## Features

- **Network Data Capture**: Utilize Wireshark to capture real-time network data packets.
- **Thorough Data Analysis**: Perform detailed analysis of captured network data to identify patterns, anomalies, and potential security threats.
- **Graphical User Interface**: An intuitive GUI for easy navigation and visualization of data, making network analysis accessible to users of all skill levels.
- **Sidebar Menu**: Quick access to various functionalities including basic information, byte analysis, session initiation, packet analysis, attack detection, and file path updates.
- **Modular Design**: Modular design with separate scripts for different analysis tasks.

## Prerequisites

- **Python 3.12.3** or higher
- **Kivy**: A Python framework for developing multitouch applications.
- **PySide6**: Python bindings for Qt, used for additional GUI elements.
- **pyqtgraph**: A pure-Python graphics and GUI library built on PyQt / PySide for scientific applications.
- **scapy**: A Python library used for network packet manipulation.
- **Wireshark**: Network protocol analyzer needed for capturing network data.

## Installation

1. **Clone the Repository**:
    ```sh
    git clone https://github.com/yourusername/Project-NetProbeX.git
    cd Project-NetProbeX
    ```

2. **Install Dependencies**:
    Ensure you have the required dependencies installed. You can use `pip` to install them:
    ```sh
    pip install kivy PySide6 pyqtgraph scapy
    ```

3. **Setup Wireshark Path**:
    Ensure Wireshark is installed and the path is set correctly. Update the path in the `constants.py` file if necessary:
    ```python
    def get_wireshark_file_path():
        return "C:\\Path\\To\\Wireshark.exe"
    ```

## Running the Application

To run the application, execute the following command:
```sh
python home.py
