# Desktop File Organizer

A clean, modular Python application that organizes files in a directory by grouping them into folders based on their extensions (e.g., `.png` files into a `png` folder).

## Architecture
The project is built using a decoupled, modular structure:
* `file organizer.py`: Contains the core logic that reads directory paths and handles the sorting/moving of files.
* `gui.py`: Built with Tkinter to provide a desktop user interface, dynamically invoking the core logic.

## How to Run
1. Make sure you have Python installed.
2. Keep both files in the same directory.
3. Run the GUI:
   ```bash
   python gui.py
