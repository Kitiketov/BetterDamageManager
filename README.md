# BetterDamageManager

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/PyQt5-desktop_app-41CD52?style=for-the-badge&logo=qt&logoColor=white" alt="PyQt5">
  <img src="https://img.shields.io/badge/QtSerialPort-COM_serial-2563EB?style=for-the-badge&logo=qt&logoColor=white" alt="QtSerialPort">
  <img src="https://img.shields.io/badge/BetterDamage-supported-F97316?style=for-the-badge" alt="BetterDamage">
</p>

Менеджер для модов и игр с поддержкой BetterDamage. Программа отслеживает изменения в txt-файле от мода, получает данные об уроне и передаёт команды на устройство через COM-порт.

## Table of Contents

- [About](#about)
- [Supported mods](#supported-mods)
- [How it works](#how-it-works)
- [Installation](#installation)
- [Tech Stack](#tech-stack)
- [Project structure](#project-structure)
- [Authors](#authors)

## About

BetterDamageManager нужен как десктопный менеджер для связки игры, BetterDamage-мода и внешнего устройства.

Программа:
- подключается к COM-порту;
- отслеживает txt-файл, в который мод записывает события;
- читает режим, силу и время события;
- отправляет соответствующую команду на устройство;
- позволяет вручную проверить вибрацию, разряд и изменение мощности.

Сейчас проект поддерживает работу через txt-файл и последовательный порт, поэтому его удобно использовать как отдельный менеджер между игрой и железом.

## Supported mods

Поддерживаются моды для следующих игр и приложений:

- **The Binding of Isaac: Repentance** — [BetterDamageForIsaac](https://pastebin.com/byihJ8cN)
- **Minecraft: Java Edition** — [BetterDamage](https://github.com/Kitiketov/BetterDamage)

## Additional resources

- **Arduino Nano script** — [скрипт для Arduino Nano](https://pastebin.com/TrbSHPYu)

## How it works

### 1. Выбор файла

Пользователь выбирает txt-файл, в который мод записывает события урона.

### 2. Запуск отслеживания

После нажатия **Start tracking** приложение начинает следить за изменениями файла.

### 3. Обработка события

Когда файл обновляется, менеджер читает строку в формате:

```text
mode/dmg/timestamp
```

Например:

```text
shock/1/1725200000
```

### 4. Отправка команды

После чтения данных программа формирует короткую serial-команду и отправляет её на выбранный COM-порт.

### 5. Тестирование

В интерфейсе есть отдельные кнопки для проверки:
- vibro
- shock
- power up
- power down

## Installation

Клонируйте репозиторий:

```bash
git clone https://github.com/Kitiketov/BetterDamageManager.git
cd BetterDamageManager
```

Установите зависимости:

```bash
pip install -r requirements.txt
```

Запуск:

```bash
python MainWindow.py
```

## Tech Stack

- Python
- PyQt5
- QtSerialPort
- QFileSystemWatcher
- auto-py-to-exe / PyInstaller

## Project structure

- `MainWindow.py` — точка входа и запуск главного окна
- `handler.py` — логика работы с файлом, COM-портом и отправкой команд
- `design.py` — интерфейс, сгенерированный из Qt Designer
- `untitled.ui` — ui-файл формы
- `BD.ico` — иконка приложения
- `build_cfg.json` — конфиг сборки для auto-py-to-exe
- `requirements.txt` — зависимости проекта

## Authors

- [Kitiketov](https://github.com/Kitiketov)
