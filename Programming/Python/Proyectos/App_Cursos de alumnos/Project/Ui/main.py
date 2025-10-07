
#* importar sys y os para que python reconozca las rutas de los carpetas y archivos py
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

## importar interfaz login
from login import iniciar_login


def main():
    iniciar_login()

if __name__ == "__main__":
    main()