# Cкрипт, який приймає шлях до директорії в якості аргументу командного рядка і візуалізує структуру цієї директорії, виводячи імена всіх піддиректорій та файлів.
# Для кращого візуального сприйняття, імена директорій та файлів мають відрізнятися за кольором.

import sys
from pathlib import Path
from colorama import Fore

def list_directory(directory, indent = 0):

    # Loop through all items in the directory
    for item in directory.iterdir():
        # Create indent to visually represent hierarchy
        indentation = "  " * indent

        # If it's a directory, print it with color and indentation
        if item.is_dir():
            print(Fore.BLUE + f"{indentation} {item.name}/")
            # Call the function to list the subdirectory contents (with increased indent)
            list_directory(item, indent + 1)
        # If it's a file, print it with color and indentation
        elif item.is_file():
            print(Fore.YELLOW + f"{indentation}{item.name}")

def main():
    # Check if the user provided a directory as an argument
    if len(sys.argv) != 2:
        print(Fore.RED + "Будь ласка, вкажіть шлях до директорії.")
        sys.exit(1)

    # Get the path of the directory from the command line argument
    directory_path = sys.argv[1]
    directory = Path(directory_path)

    # Check if the directory exists
    if not directory.exists():
        print(Fore.RED + "Помилка: Директорія не існує.")
        sys.exit(1)
    if not directory.is_dir():
        print(Fore.RED + f"Помилка: {directory} не є директорією.")
        sys.exit(1)

    # Print initial directory
    print(Fore.BLUE + f"{directory.name}/")

    # Call the function to display the contents of the directory
    list_directory(directory)

if __name__ == "__main__":
    main()