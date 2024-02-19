# File Manager 2025

Description of the project.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [File Structure](#file-structure)
- [Dependencies](#dependencies)
- [Output](#output)
- [Contributing](#contributing)
- [License](#license)

## Installation

Describe how to install and set up the project, including any dependencies.

```bash
pip install -r requirements.txt

**Usage**
Provide examples and instructions for using your project.

bash
Copy code
python File_Manager.py
File Structure
bajranj.docx: Description of the file.
dpi_settings.json: Saves GUI settings for scaling widgets, default value is 96.
File_Manager.py: Main file where program execution starts, imports other .py files directly or in chain.
Icons/: Folder containing all images like .ico, .png.
mysql_conn.py: Contains code for all communication between database, e.g., insert, delete, update, or retrieve data to show in GUI.
open_details.py: Contains a class of frame used to create a custom frame with widgets to edit student details and save academic marks.
output/: Folder carrying .exe file of File_Manager.py.
output.txt: Simple text file containing saved database location and port number, edited from File_Manager if default is not connected or offline.
requirements.txt: Contains all dependent libraries for the project.
save_to_file.py: Contains GUI for saving database location and port number in output.txt file.
user_pic_upload.py: Used to communicate with data only to store images.
Dependencies
List of dependent libraries for the project.

Output
contains.exe file.
