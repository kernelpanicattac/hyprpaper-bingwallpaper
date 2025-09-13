# Bing Daily Wallpaper for Hyprland

Автономный скрипт для Hyprland, который ежедневно скачивает актуальные обои с Bing и обновляет текущий фон рабочего стола через `hyprpaper`.

## Установка

1. Склонируйте репозиторий:

   ```bash
   git clone https://github.com/ваш-логин/bing-daily-wallpaper.git
   cd bing-daily-wallpaper
   ```

2. Сделайте скрипт исполняемым:

   ```bash
   chmod +x bingdg.py
   ```

3. Настройте путь к папке для сохранения обоев в скрипте (по умолчанию `/home/username/Изображения/backgrounds/`):

   ```bash
   BASE_PATH = "/home/username/Изображения/backgrounds/"
   CURRENT_BACKGROUND = os.path.join(BASE_PATH, "current.jpg")
   ```

---

## Настройка hyprpaper

Отредактируйте `~/.config/hypr/hyprpaper.conf`:

   ```bash
   preload = /home/username/Изображения/backgrounds/current.jpg
   wallpaper = DP-3,/home/username/Изображения/backgrounds/current.jpg
   ```

* Замените `DP-3` на имя вашего монитора (`hyprctl monitors`).
* Для нескольких мониторов добавьте строки `wallpaper = ...` для каждого.

---

## Автоматический запуск

### Через cron 

1. Откройте crontab:

   ```bash
   crontab -e
   ```

2. Добавьте строку:

   ```bash
   @daily /usr/bin/python3 /home/username/scripts/bingdg.py
   ```

Скрипт будет выполняться раз в день.

---



