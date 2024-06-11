Project NetProbeX
Overview
Project NetProbeX aims to create a user-friendly Wireshark data analysis tool that facilitates a comprehensive understanding of Wireshark functionalities and proficient network data analysis. This tool enables users to capture network data, conduct thorough data analysis, and present insights through an intuitive graphical user interface (GUI). Developed primarily in Python, this project enhances members' expertise in network analysis.

Features
Network Data Capture: Utilize Wireshark to capture real-time network data packets.
Thorough Data Analysis: Perform detailed analysis of captured network data to identify patterns, anomalies, and potential security threats.
Graphical User Interface: An intuitive GUI for easy navigation and visualization of data, making network analysis accessible to users of all skill levels.
Sidebar Menu: Quick access to various functionalities including basic information, byte analysis, session initiation, packet analysis, attack detection, and file path updates.
Modular Design: Modular design with separate scripts for different analysis tasks.
Prerequisites
Python 3.12.3 or higher
Kivy: A Python framework for developing multitouch applications.
PySide6: Python bindings for Qt, used for additional GUI elements.
pyqtgraph: A pure-Python graphics and GUI library built on PyQt / PySide for scientific applications.
scapy: A Python library used for network packet manipulation.
Wireshark: Network protocol analyzer needed for capturing network data.
Installation
Clone the Repository:

sh
Copy code
git clone https://github.com/yourusername/Project-NetProbeX.git
cd Project-NetProbeX
Install Dependencies:
Ensure you have the required dependencies installed. You can use pip to install them:

sh
Copy code
pip install kivy PySide6 pyqtgraph scapy
Setup Wireshark Path:
Ensure Wireshark is installed and the path is set correctly. Update the path in the constants.py file if necessary:

python
Copy code
def get_wireshark_file_path():
    return "C:\\Path\\To\\Wireshark.exe"
Running the Application
To run the application, execute the following command:

sh
Copy code
python home.py
File Structure
home.py: Main application script that launches the GUI.
constants.py: Contains configuration constants like the Wireshark executable path.
visualaid.py: Script for byte analysis and visual aid.
filter_analysis_win.py: Script for filter analysis window.
packetsandlinks.py: Script for displaying personal information.
performanceAnalysis.py: Script for performance analysis.
open_wireshark.py: Script to initiate Wireshark session.
update_wireshark_path.py: Script for updating Wireshark file path.
testing/: Contains test scripts for the application.
Usage
Sidebar Menu
Basic Information: Displays general information about the captured network data.
Byte Analysis: Opens a visual aid tool for byte-level analysis.
Start a Session: Launches Wireshark to start a new network data capture session.
Packet Analysis: Performs detailed packet analysis.
Attack Detection: Identifies potential security threats based on the captured data.
Update File Path: Allows updating the file path for Wireshark executable.
Closing the Application
Press the 'Close' button in the GUI.
Confirm the closure in the popup window that appears.
Testing
Automated tests for the application are located in the testing directory. To run the tests, execute the following command:

sh
Copy code
python testing/testhome.py
Contributing
Contributions are welcome! Please fork the repository and submit a pull request with your changes. Ensure your code adheres to the project's coding standards and includes relevant tests.
