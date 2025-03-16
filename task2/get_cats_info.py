# Функція яка аналізує файл.txt та повертає список словників з інформацією про кожного кота.

from pathlib import Path

def get_cats_info(path: str) -> list[dict]:

     # Check if the file exists before proceeding
    if not Path(path).exists():
        print("Error: File not found.")
        return []
    
    try:
        # Open and read the file
        with open(path, 'r', encoding='utf-8') as file:

            # Make list of cats
            cats_list = file.read().splitlines()

            # Empty list cats_info_list
            cats_info_list = []
            
            # Fill up cats_info
            for el in cats_list:
                el = el.split(',')

                # Handle the case when there's an issue with the file's content (corrupted format)
                if len(el) != 3:
                    print(f"Warning: Incorrect format in line, skipping: {el}")
                    continue  # Skip this line and move to the next one

                # Handle the case when the information is missing
                for i in range(len(el)):
                    if el[i] == '':
                        el[i] = 'Missing info in database'

                # Validate age to be an integer, if it's invalid, mark it
                try:
                    el[2] = int(el[2])
                except ValueError:
                    el[2] = 'Invalid age'

                cat_dict = {
                "id": el[0],
                "name": el[1],
                "age": el[2]}

                cats_info_list.append(cat_dict)
    
        return cats_info_list
    
    except ValueError:
        # Handle the case when there's an issue with the file's content (corrupted format)
        print("Помилка: Невірний формат файлу Перевірте дані у файлі.")
        return []

    except Exception as e:
        # Catch any other unexpected exceptions and handle them
        print(f"Помилка: Сталася непередбачена помилка. Деталі: {str(e)}")
        return []

# Test function
cats_info = get_cats_info("cats.txt")
print(cats_info)