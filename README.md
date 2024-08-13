# JetBrains IDE Reset Util

This utility provides a graphical user interface (GUI) for resetting JetBrains IDEs. It allows users to select a JetBrains IDE, perform necessary reset actions, and open the selected IDE. 

## Features

- Select from a list of JetBrains IDEs.
- Reset the IDE by removing certain configuration files.
- Open the IDE after resetting.

## Setup

1. **Install Dependencies:**
   
   Make sure you have Python and PyQt5 installed. You can install the dependencies using pip:

   ```
   pip install PyQt5
   ```

## Usage

To run the application, execute the Python script `main.py`:

```
python main.py
```

## Creating Executable

You can create an executable file for the application using PyInstaller. 

### With Python Interpreter:

```
python -m PyInstaller --onefile --hidden-import=PyQt5 main.py
```

### Without Python Interpreter:

If you have PyInstaller installed globally, you can run:

```
pyinstaller --onefile --hidden-import=PyQt5 main.py
```

This will generate a standalone executable file in the `dist` directory.

---
