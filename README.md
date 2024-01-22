h2. Подготовка

1. Установить зависимости:
   ```bash
   pip install --upgrade google-api-python-client && pip install pandas openpyxl python-dotenv
   ```
1. Создать файл `.env` со следующим наполнением:
   ```env
   YOUTUBE_API_KEY=XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
   ```
   Значения для YOUTUBE_API_KEY можно взять, пройдя по [этой инструкции](https://www.geeksforgeeks.org/youtube-data-api-set-1/).
   <img width="1067" alt="image" src="https://github.com/vasartam/yt-comments-analysis/assets/15614336/0d17eadb-7375-492a-a38f-b2eb9890fe5f">

h2. Запуск скрипта

```bash
python <имя_файла.py>
```

h2. Описание скриптов

`load_comments.py` загружает комментарии с данного YouTube-видео в локальный файл `comments.json`.

`create_csv.py` создает Excel-файл из имеющегося файла `comments.json`.

`talents.py` пытается вычленить таланты из всех комментариев и складывает их в `talents.json`. На данный момент может работать некорректно.

`create_text.py` соединяет все тексты комментариев в один большой текстовый файл на основе `comments.json`.
