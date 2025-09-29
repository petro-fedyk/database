from flask import Blueprint, request, jsonify
from service.userdownload_song_service import UserDownloadSongService
from sqlalchemy.orm import joinedload
from dao.models import UserDownloadHasSong, Song, UserDownload

user_download_song_bp = Blueprint('user_download_song_bp', __name__)

@user_download_song_bp.route('/userdownloads_has_songs', methods=['GET'])
def get_all_user_downloads_songs():
    """
    Get all records from userdownloads_has_songs table
    ---
    tags:
      - UserDownloadsHasSongs
    responses:
      200:
        description: List of user download-song records
    """
    records = UserDownloadSongService.get_all_records()
    return jsonify(records), 200

@user_download_song_bp.route('/userdownloads_has_songs/<int:download_id>/<int:song_id>', methods=['GET'])
def get_user_download_song(download_id, song_id):
    """
    Get a specific record by download_id and song_id, or detailed data from songs and downloads tables
    ---
    tags:
      - UserDownloadsHasSongs
    parameters:
      - name: download_id
        in: path
        type: integer
        required: true
        description: Download ID
      - name: song_id
        in: path
        type: integer
        required: true
        description: Song ID
    responses:
      200:
        description: Record found
      404:
        description: Record not found
    """
    record = UserDownloadHasSong.query.filter_by(
        userdownloads_download_id=download_id,
        songs_song_id=song_id
    ).join(
        Song, UserDownloadHasSong.songs_song_id == Song.song_id
    ).join(
        UserDownload, UserDownloadHasSong.userdownloads_download_id == UserDownload.download_id
    ).add_columns(
        Song.song_title, Song.genre_id, Song.duraction, Song.realease_date,
        UserDownload.device_type, UserDownload.operating_system, UserDownload.location
    ).first()

    if record:
        response = {
            "userdownloads_download_id": download_id,
            "songs_song_id": song_id,
            "song_details": {
                "title": record.song_title,
                "genre_id": record.genre_id,
                "duraction": str(record.duraction),
                "realease_date": str(record.realease_date)
            },
            "download_details": {
                "device_type": record.device_type,
                "operating_system": record.operating_system,
                "location": record.location
            }
        }
        return jsonify(response), 200

    basic_record = UserDownloadSongService.get_record(download_id, song_id)
    if basic_record:
        return jsonify(basic_record), 200

    return jsonify({"error": "Record not found"}), 404

@user_download_song_bp.route('/userdownloads_has_songs', methods=['POST'])
def create_user_download_song():
    """
    Create a new record in userdownloads_has_songs table
    ---
    tags:
      - UserDownloadsHasSongs
    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          required: [userdownloads_download_id, songs_song_id]
          properties:
            userdownloads_download_id:
              type: integer
            songs_song_id:
              type: integer
    responses:
      201:
        description: Record created
      400:
        description: Invalid input
    """
    data = request.get_json()
    if not data:
        return jsonify({"error": "Invalid input"}), 400

    record = UserDownloadSongService.create_record(data)
    return jsonify(record), 201

@user_download_song_bp.route('/userdownloads_has_songs/<int:download_id>/<int:song_id>', methods=['PUT'])
def update_user_download_song(download_id, song_id):
    """
    Update an existing record by download_id and song_id
    ---
    tags:
      - UserDownloadsHasSongs
    parameters:
      - name: download_id
        in: path
        type: integer
        required: true
        description: Download ID
      - name: song_id
        in: path
        type: integer
        required: true
        description: Song ID
      - in: body
        name: body
        required: true
        schema:
          type: object
          properties:
            userdownloads_download_id:
              type: integer
            songs_song_id:
              type: integer
    responses:
      200:
        description: Record updated
      400:
        description: Invalid input
      404:
        description: Record not found
    """
    data = request.get_json()
    if not data:
        return jsonify({"error": "Invalid input"}), 400

    updated_record = UserDownloadSongService.update_record(download_id, song_id, data)
    if updated_record:
        return jsonify(updated_record), 200
    return jsonify({"error": "Record not found"}), 404

@user_download_song_bp.route('/userdownloads_has_songs/<int:download_id>/<int:song_id>', methods=['DELETE'])
def delete_user_download_song(download_id, song_id):
    """
    Delete a record from userdownloads_has_songs table by download_id and song_id
    ---
    tags:
      - UserDownloadsHasSongs
    parameters:
      - name: download_id
        in: path
        type: integer
        required: true
        description: Download ID
      - name: song_id
        in: path
        type: integer
        required: true
        description: Song ID
    responses:
      200:
        description: Record deleted
      404:
        description: Record not found
    """
    success = UserDownloadSongService.delete_record(download_id, song_id)
    if success:
        return jsonify({"message": "Record deleted"}), 200
    return jsonify({"error": "Record not found"}), 404