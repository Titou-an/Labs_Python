import subprocess
import sys
import importlib

def verify_and_install_library(library_name):
  try:
    print(f"Essayons d'importer {library_name}...", end='')
    importlib.import_module(library_name)
    print(f"{library_name.capitalize()} est installé!")
  except ModuleNotFoundError:
    print(f"{library_name.capitalize()} n'est pas installé. Nous allons essayer de l'installer...")
    # Try to install the library using pip.
    subprocess.check_call([sys.executable, "-m", "pip", "install", library_name])

    print("\n\n\n\nC'est fait! Exécutez ce script à nouveau pour valider l'installation.")
    print("S'il y a des erreurs, demandez de l'aide à votre chargé de laboratoire.")

if __name__ == '__main__':
  verify_and_install_library("matplotlib")
  verify_and_install_library("numpy")