# Hotel Management System

## Requirement

Applikasi hotel ini berbasis web, dengan menggunakan python 3.12.3.

## Setup

Disini saya menyarankan untuk menggunakan virtual environment, untuk memudahkan pengaturan dependencie project.

1. Masuk ke dalam folder project.
2. Buat virtual environment:
    ```bash
   python -m venv venv
    ```
3. Aktivkan virtual environment:
    ```bash
   #Windows
   venv\Scripts\activate

   #MacOS dan Linux
   source venv/bin/activate
    ```
4. install dependecies dari requirements.txt:
    ```bash
   pip install -r requirements.txt
    ```
5. Create seed data:
    ```bash
    python seed.py
    ```
6. Jalankan applikasi:
    ```bash
    python app.py
    ```

Selesai, happy coding.