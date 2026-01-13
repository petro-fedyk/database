from extensions import db
from dao.models import (
    User, Genre, Author, Album, Label,
    Song, Playlist, UserFavoriteArtist,
    UserDownload, UserDownloadHasSong
)
from app import create_app

# Створюємо Flask app
app = create_app()

# Створюємо всі таблиці
with app.app_context():
    db.create_all()
    print("✅ Таблиці створено успішно!")
