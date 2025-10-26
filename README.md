# Music Service API

This project is a **Flask-based REST API** for a music service. It provides endpoints for **accounts, songs, playlists, genres, user favorites, and downloads**, with **Swagger UI** for documentation.

---

## Features

- REST API endpoints for:
  - User accounts
  - Songs
  - Playlists
  - Genres
  - User favorite artists
  - User downloaded songs
- Swagger UI documentation at `/swagger/`
- Version endpoint at `/version`
- Demo endpoint at `/demo`
- Uses **MySQL** as the database backend
- Configurable via `config/app.yml`
- SQLAlchemy ORM integration

---

## Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/music-service-api.git
cd music-service-api
