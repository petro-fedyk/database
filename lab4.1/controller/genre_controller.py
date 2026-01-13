from flask import Blueprint, jsonify, request
from service.genre_servise import GenreService

# Initialize Blueprint for genres
genre_bp = Blueprint('genres', __name__)

@genre_bp.route('/genres', methods=['POST'])
def create_genre():
    """
    Create a new genre
    ---
    tags:
      - Genres
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
    responses:
      201:
        description: Genre created
      400:
        description: Invalid data
    """
    data = request.json
    result, status_code = GenreService.create_genre(data)
    return jsonify(result), status_code

@genre_bp.route('/genres', methods=['GET'])
def get_all_genres():
    """
    Get all genres
    ---
    tags:
      - Genres
    responses:
      200:
        description: List of genres
    """
    genres, status_code = GenreService.get_all_genres()
    return jsonify(genres), status_code

@genre_bp.route('/genres/<int:genre_id>', methods=['GET'])
def get_genre_by_id(genre_id):
    """
    Get genre by ID
    ---
    tags:
      - Genres
    parameters:
      - name: genre_id
        in: path
        type: integer
        required: true
        description: Genre ID
    responses:
      200:
        description: Genre found
      404:
        description: Genre not found
    """
    result, status_code = GenreService.get_genre_by_id(genre_id)
    return jsonify(result), status_code

@genre_bp.route('/genres/<int:genre_id>', methods=['PUT'])
def update_genre(genre_id):
    """
    Update genre by ID
    ---
    tags:
      - Genres
    parameters:
      - name: genre_id
        in: path
        type: integer
        required: true
        description: Genre ID
      - in: body
        name: body
        required: true
        schema:
          type: object
          properties:
            name:
              type: string
    responses:
      200:
        description: Genre updated
      404:
        description: Genre not found
    """
    data = request.json
    result, status_code = GenreService.update_genre(genre_id, data)
    return jsonify(result), status_code

@genre_bp.route('/genres/<int:genre_id>', methods=['DELETE'])
def delete_genre(genre_id):
    """
    Delete genre by ID
    ---
    tags:
      - Genres
    parameters:
      - name: genre_id
        in: path
        type: integer
        required: true
        description: Genre ID
    responses:
      200:
        description: Genre deleted successfully
      404:
        description: Genre not found
    """
    result, status_code = GenreService.delete_genre(genre_id)
    return jsonify(result), status_code