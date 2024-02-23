# Kafka YouTube Playlist Updates Project

Use:
- Python
- Confluent Kafka
- YouTube Data API
- Poetry (Dependency management)
- Google Cloud (Cloud function & scheduled execution)

Using Kafka, this program monitor changes to the views, likes, and comments count of videos in a given playlist, and notify the user via Telegram messages.

For manual code execution:

1. Install dependencies with Poetry commands. Dependencies list is in requirements.txt

2. Edit configuration variables in config.py

3. Open Poetry shell and run main.py:
```
$ poetry shell
$ poetry run python3 main.py
```

Roughly based on: https://www.youtube.com/watch?v=jItIQ-UvFI4

**In case of Poetry error, try deleting poetry.lock and re-installing from pyproject.toml