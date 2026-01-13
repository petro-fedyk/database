from flask import Blueprint, jsonify, request
from service.song_servise import SongService

# Initialize Blueprint for songs
songs_bp = Blueprint('songs', __name__)

@songs_bp.route('/songs', methods=['POST'])
def create_song():
    """
    Create a new song
    ---
    tags:
      - Songs
    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          required: [title, artist_id]
          properties:
            title:
              type: string
            artist_id:
              type: integer
            genre_id:
              type: integer
            duration:
              type: integer
            release_date:
              type: string
              format: date
    responses:
      201:
        description: Song created
      400:
        description: Invalid data
    """
    data = request.json
    result, status_code = SongService.create_song(data)
    return jsonify(result), status_code

@songs_bp.route('/songs', methods=['GET'])
def get_songs():
    """
    Get all songs
    ---
    tags:
      - Songs
    responses:
      200:
        description: List of songs
    """
    songs = SongService.get_all_songs()
    return jsonify(songs)

@songs_bp.route('/songs/<int:song_id>', methods=['GET'])
def get_song(song_id):
    """
    Get song by ID
    ---
    tags:
      - Songs
    parameters:
      - name: song_id
        in: path
        type: integer
        required: true
        description: Song ID
    responses:
      200:
        description: Song found
      404:
        description: Song not found
    """
    result, status_code = SongService.get_song_by_id(song_id)
    return jsonify(result), status_code

@songs_bp.route('/songs/<int:song_id>', methods=['PUT'])
def update_song(song_id):
    """
    Update song by ID
    ---
    tags:
      - Songs
    parameters:
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
            title:
              type: string
            artist_id:
              type: integer
            genre_id:
              type: integer
            duration:
              type: integer
            release_date:
              type: string
              format: date
    responses:
      200:
        description: Song updated
      404:
        description: Song not found
    """
    data = request.json
    result, status_code = SongService.update_song(song_id, data)
    return jsonify(result), status_code

@songs_bp.route('/songs/<int:song_id>', methods=['DELETE'])
def delete_song(song_id):
    """
    Delete song by ID
    ---
    tags:
      - Songs
    parameters:
      - name: song_id
        in: path
        type: integer
        required: true
        description: Song ID
    responses:
      200:
        description: Song deleted successfully
      404:
        description: Song not found
    """
    result, status_code = SongService.delete_song(song_id)
    return jsonify(result), status_code