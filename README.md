````markdown
# Bing Daily Wallpaper for Hyprland

Автономный скрипт для Linux (Hyprland), который ежедневно скачивает актуальные обои с Bing и обновляет текущий фон рабочего стола через `hyprpaper`.

---

## Особенности

- Скачивает UHD-обои Bing напрямую, без сторонних сервисов.  
- Обновляет файл `current.jpg` в указанной папке.  
- Работает с `hyprpaper` (Hyprland) для установки фона.  
- Настраивается для одного или нескольких мониторов через конфиг `hyprpaper.conf`.  

---

## Установка

1. Склонируйте репозиторий:
   ```bash
   git clone https://github.com/ваш-логин/bing-daily-wallpaper.git
   cd bing-daily-wallpaper
````

2. Сделайте скрипт исполняемым:

   ```bash
   chmod +x bingdg.py
   ```

3. Настройте путь к папке для сохранения обоев в скрипте (по умолчанию `/home/username/Изображения/backgrounds/`):

   ```python
   BASE_PATH = "/home/username/Изображения/backgrounds/"
   CURRENT_BACKGROUND = os.path.join(BASE_PATH, "current.jpg")
   ```

---

## Настройка hyprpaper

Отредактируйте `~/.config/hypr/hyprpaper.conf`:

```ini
preload = /home/username/Изображения/backgrounds/current.jpg
wallpaper = DP-3,/home/username/Изображения/backgrounds/current.jpg
```

* Замените `DP-3` на имя вашего монитора (`hyprctl monitors`).
* Для нескольких мониторов добавьте строки `wallpaper = ...` для каждого.

---

## Автоматический запуск

### Через cron (рекомендовано для юзера)

1. Откройте crontab:

   ```bash
   crontab -e
   ```

2. Добавьте строку:

   ```bash
   @daily /usr/bin/python3 /home/username/scripts/bingdg.py
   ```

Скрипт будет выполняться раз в день.

> Если компьютер был выключен в момент запуска cron, задача не выполнится. Для этого есть systemd timer или anacron (см. документацию).

---

## Использование

Просто запустите скрипт вручную:

```bash
python3 bingdg.py
```

После этого `current.jpg` обновится, и `hyprpaper` установит новый фон согласно конфигу.

---

## Лицензия

MIT License

```

---

Если хочешь, я могу сразу добавить **ссылку на примеры конфигурации для нескольких мониторов** и небольшой раздел «Отладка», чтобы видеть скачанный файл и URL картинки. Это удобно для GitHub.
```
