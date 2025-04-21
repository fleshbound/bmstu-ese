# Создание исполняемого файла

main.py - исходный код

Установка зависимостей poetry:
```
poetry install
```

Запуск создания исполняемого файла:
```
poetry run pyinstaller --hidden-import='PIL._tkinter_finder' --onefile --windowed main.py
```

Запуск полученного файла:
```
./dist/main
```
