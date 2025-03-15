# Функція яка аналізує файл.txt і повертає загальну та середню суму заробітної плати всіх розробників.

from pathlib import Path

current_directory = Path.cwd()
print(current_directory)

script_directory = Path(__file__).parent
print(script_directory)


def total_salary(path):
    relative_path = Path(path)
    path = relative_path
    print(path.read_text()) 
    print("Exists:", path.exists()) 

total_salary("salary.txt")