# Функція яка аналізує файл.txt і повертає загальну та середню суму заробітної плати всіх розробників.

from pathlib import Path

def total_salary(path: str) -> tuple:

     # Check if the file exists before proceeding
    if not Path(path).exists():
        print("Error: File not found.")
        return 0, 0
    
    try:
        # Open and read the file
        with open(path, 'r', encoding='utf-8') as file:

            # Make list of employers
            employer_list = file.read().split('\n')

            # Empty list with salaries
            salary_list = []

            # Fill up salary_list
            for el in employer_list:
                el = int(el.split(',')[-1])
                salary_list.append(el)

        # Total salary calculation
        total = sum(salary_list)

        # Avarage salary calculation
        average = int(total / len(salary_list))
    
        return total, average
    
    except ValueError:
        # Handle the case when there's an issue with the file's content (corrupted format)
        print("Помилка: Невірний формат файлу Перевірте дані у файлі.")
        return 0, 0

    except Exception as e:
        # Catch any other unexpected exceptions and handle them
        print(f"Помилка: Сталася непередбачена помилка. Деталі: {str(e)}")
        return 0, 0

# Test function
total, average = total_salary("salary.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")