import os
import time

class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    B = '\033[1;34m'  # Color 'b'
    RED = '\033[91m'

def search_files(keyword, directory="."):
    found_entries = []
    start_time = time.time()

    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".txt"):
                file_path = os.path.join(root, file)
                matching_lines = []  # Stocker les lignes correspondantes dans ce fichier
                with open(file_path, 'r', encoding='latin1') as f:
                    for line_number, line in enumerate(f, start=1):
                        if keyword in line:
                            entry = {
                                "file_path": os.path.relpath(file_path, directory),
                                "line_number": line_number,
                                "line_content": line.strip()
                            }
                            found_entries.append(entry)
                            matching_lines.append(line.strip())  # Stocker la ligne correspondante
                    if matching_lines:
                        print(f"{Colors.HEADER}Mot trouvé dans le fichier : {Colors.GREEN}{file_path}{Colors.ENDC}")
                        for line_number, line in enumerate(matching_lines, start=1):
                            print(f"{Colors.BLUE}Ligne {line_number}:{Colors.ENDC} {line}")
                        print()  # Ligne vide pour séparer les fichiers

    end_time = time.time()
    search_duration = end_time - start_time
    return found_entries, search_duration

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    clear_screen()
    root_directory = os.path.join(os.path.dirname(os.path.abspath(__file__)), "DB")

    if not os.path.exists(root_directory) or not os.path.isdir(root_directory):
        print(f"{Colors.FAIL}Le répertoire DB n'existe pas.{Colors.ENDC}")
        return

    menu_text = (
        f"{Colors.BLUE} _   _      _ _       \n"
        "| | | |    | | |      \n"
        "| |_| | ___| | | ___  \n"
        "|  _  |/ _ \ | |/ _ \ \n"
        "| | | |  __/ | | (_) |\n"
        "\_| |_/\___|_|_|\___/ \n"
    )

    discord_text = f"{Colors.RED}discord : helloguys.uhq{Colors.ENDC}"

    formatted_text = f"{Colors.B}{' ' * 12} Dedi a Luz et Celcius {' ' * 12}{Colors.ENDC}"  # Utilisation de Colors.B pour la couleur 'b'
    print("\n".join(menu_text.split("\n")[:-1]).center(os.get_terminal_size().columns))
    print(formatted_text.center(os.get_terminal_size().columns))
    print(menu_text.split("\n")[-1])
    print("\n" + discord_text + "\n")

    while True:
        keyword = input(f"{Colors.BOLD}\nMet le nom ou l'id du mec que tu veux bz : {Colors.ENDC}")

        if keyword.lower() == "q":
            break

        entries, search_duration = search_files(keyword, root_directory)

        if entries:
            print(f"{Colors.HEADER}\nRésultats :{Colors.ENDC}")
            for entry in entries:
                print(f"{Colors.GREEN}Mot trouvé dans le fichier : {entry['file_path']}{Colors.ENDC}")
                print(f"{Colors.BLUE}Ligne {entry['line_number']}:{Colors.ENDC} {entry['line_content']}\n")
            print(f"{Colors.BOLD}Temps de recherche : {search_duration:.2f} secondes{Colors.ENDC}")
        else:
            print(f"{Colors.WARNING}\nAucun résultat trouvé.{Colors.ENDC}")

if __name__ == "__main__":
    main()
