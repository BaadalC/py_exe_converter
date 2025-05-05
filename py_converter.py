import PyInstaller.__main__
import os
import sys
from tkinter import Tk
from tkinter.filedialog import askopenfilename, askopenfilenames
from tkinter.messagebox import showinfo, showwarning

def get_file_path(title, file_types):
    """
    Opens a file dialog and returns the path of the selected file.

    Args:
        title (str): The title of the file dialog window.
        file_types (list): A list of tuples specifying file types and their extensions.
            Example: [("Python Files", "*.py"), ("All Files", "*.*")]

    Returns:
        str: The path of the selected file, or an empty string if no file is selected.
    """
    root = Tk()
    root.withdraw()  # Hide the main window
    file_path = askopenfilename(title=title, filetypes=file_types)
    root.destroy()  # Clean up
    return file_path

def get_files_path(title, file_types):
    """
    Opens a file dialog and returns the paths of the selected files.

    Args:
        title (str): The title of the file dialog window.
        file_types (list): A list of tuples specifying file types and their extensions.
            Example: [("Image Files", "*.png;*.jpg;*.jpeg"), ("All Files", "*.*")]

    Returns:
        list: The paths of the selected files, or an empty list if no file is selected.
    """
    root = Tk()
    root.withdraw()
    file_paths = askopenfilenames(title=title, filetypes=file_types)
    root.destroy()
    return list(file_paths) # Ensure it is a list

def create_pyinstaller_command(script_path, onefile=True, console=False, icon_path=None, additional_files=None, name=None):
    """
    Constructs the PyInstaller command based on user-provided options.

    Args:
        script_path (str): Path to the main Python script.
        onefile (bool, optional):  If True, creates a single executable. Defaults to True.
        console (bool, optional): If True, keeps the console window open. Defaults to False.
        icon_path (str, optional): Path to the icon file. Defaults to None.
        additional_files (list, optional): List of tuples containing file paths
            and destination paths.  Defaults to None.
        name (str, optional): Name of the output executable. Defaults to None.

    Returns:
        list: A list representing the PyInstaller command.
    """
    command = [
        script_path,
        '--name', name if name else os.path.splitext(os.path.basename(script_path))[0], # set name
    ]

    if onefile:
        command.append('--onefile')
    if not console:
        command.append('--windowed')  # Use --windowed for GUI apps (no console)
    if icon_path:
        command.extend(['--icon', icon_path])
    if additional_files:
        for file_path in additional_files:
            # Important: Handle potential errors in user-provided paths.
            if not os.path.exists(file_path):
                print(f"Warning: File not found: {file_path}. Skipping.")
                continue
            command.extend(['--add-data', f'{file_path}{os.pathsep}.']) # Add file and destination

    return command

def run_pyinstaller_command(command):
    """
    Executes the PyInstaller command.

    Args:
        command (list): The PyInstaller command as a list.
    """
    try:
        print(f"Running PyInstaller with command: {' '.join(command)}")
        PyInstaller.__main__.run(command)
        print("PyInstaller execution completed.")
    except SystemExit as e:
        if e.code != 0:
            print(f"PyInstaller failed with exit code {e.code}.  Check the output for errors.")
        else:
            print("PyInstaller completed successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")
        print("Please check your installation and script.")

def main():
    """
    Main function to orchestrate the conversion process.
    """
    print("Welcome to the Python to EXE Converter!")

    # 1. Get the Python script path
    script_path = get_file_path("Select your Python script (.py)", [("Python Files", "*.py")])
    if not script_path:
        print("No script selected. Exiting.")
        return

    # 2. Get the icon file (optional)
    icon_path = get_file_path("Select an icon file (optional)", [("Icon Files", "*.ico"), ("All Files", "*.*")]) if input("Do you want to add an icon? (y/n): ").lower() == 'y' else None

    # 3. Get additional files (optional)
    additional_files = []
    if input("Do you want to add additional files (images, data, etc.)? (y/n): ").lower() == 'y':
        file_paths = get_files_path("Select additional files", [("All Files", "*.*")])
        if file_paths: # check if the user selected files
             additional_files = file_paths

    # 4. Get the name of the executable
    executable_name = input("Enter the name of the executable (or press Enter for script name): ")

    # 5. Configure options (onefile, console) - added options
    onefile = input("Create a single executable file? (y/n): ").lower() == 'y'
    console = input("Keep the console window open? (y/n): ").lower() == 'y'

    # 6. Construct the PyInstaller command
    command = create_pyinstaller_command(script_path, onefile, not console, icon_path, additional_files, executable_name)

    # 7. Run PyInstaller
    run_pyinstaller_command(command)

    print("Conversion process finished.")
    print("The executable file(s) should be in the 'dist' folder.") # inform the user

if __name__ == "__main__":
    main()

