from flask import Blueprint, jsonify, request
from service.playlist_servise import PlaylistService

# Initialize Blueprint for playlists
playlists_bp = Blueprint('playlists', __name__)

@playlists_bp.route('/playlists', methods=['POST'])
def create_playlist():
    """
    Create a new playlist
    ---
    tags:
      - Playlists
    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          required: [name]
          properties:
            name:
              type: string
            description:
              type: string
            user_id:
              type: integer
    responses:
      201:
        description: Playlist created
      400:
        description: Invalid data
    """
    data = request.json
    result, status_code = PlaylistService.create_playlist(data)
    return jsonify(result), status_code

@playlists_bp.route('/playlists', methods=['GET'])
def get_playlists():
    """
    Get all playlists
    ---
    tags:
      - Playlists
    responses:
      200:
        description: List of playlists
    """
    playlists, status_code = PlaylistService.get_all_playlists()
    return jsonify(playlists), status_code

@playlists_bp.route('/playlists/<int:playlist_id>', methods=['GET'])
def get_playlist(playlist_id):
    """
    Get playlist by ID
    ---
    tags:
      - Playlists
    parameters:
      - name: playlist_id
        in: path
        type: integer
        required: true
        description: Playlist ID
    responses:
      200:
        description: Playlist found
      404:
        description: Playlist not found
    """
    result, status_code = PlaylistService.get_playlist_by_id(playlist_id)
    return jsonify(result), status_code

@playlists_bp.route('/playlists/<int:playlist_id>', methods=['PUT'])
def update_playlist(playlist_id):
    """
    Update playlist by ID
    ---
    tags:
      - Playlists
    parameters:
      - name: playlist_id
        in: path
        type: integer
        required: true
        description: Playlist ID
      - in: body
        name: body
        required: true
        schema:
          type: object
          properties:
            name:
              type: string
            description:
              type: string
            user_id:
              type: integer
    responses:
      200:
        description: Playlist updated
      404:
        description: Playlist not found
    """
    data = request.json
    result, status_code = PlaylistService.update_playlist(playlist_id, data)
    return jsonify(result), status_code

@playlists_bp.route('/playlists/<int:playlist_id>', methods=['DELETE'])
def delete_playlist(playlist_id):
    """
    Delete playlist by ID
    ---
    tags:
      - Playlists
    parameters:
      - name: playlist_id
        in: path
        type: integer
        required: true
        description: Playlist ID
    responses:
      200:
        description: Playlist deleted successfully
      404:
        description: Playlist not found
    """
    result, status_code = PlaylistService.delete_playlist(playlist_id)
    return jsonify(result), status_code