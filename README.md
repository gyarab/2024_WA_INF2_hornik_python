

Tento projekt je webová aplikace postavená na Django frameworku pro správu a zobrazování diskografie různých (mých oblíbených) hudebních kapel.

## Požadavky

- Python 3.8+
- Django 4.0+

## Instalace

1. Naklonujte repozitář:
   ```bash
   git clone https://github.com/gyarab/2024_WA_INF2_hornik_python.git

2. Vytvořte a aktivujte virtuální prostředí:
    ```bash
    python -m venv venv
    source venv/bin/activate  # Na Windows: venv\Scripts\activate

3. Nainstalujte poždavky:
    ```bash
    pip install -r requirements.txt

4. Proveďte migraci databáze:
    ```bash
    python manage.py migrate

5. Spusťte vývojový server:
    ```bash
    python manage.py runserver

## Autor
Šimon Horník
