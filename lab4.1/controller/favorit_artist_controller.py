from flask import Blueprint, jsonify, request
from service.favorit_artist_servise import UserFavoriteArtistService

# Create Blueprint for the controller
user_favorite_artist_bp = Blueprint('user_favorite_artist', __name__)

@user_favorite_artist_bp.route('/favorites', methods=['POST'])
def create_favorite():
    """
    Create a new favorite artist record
    ---
    tags:
      - Favorite Artists
    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          required: [user_id, author_id, added_date]
          properties:
            user_id:
              type: integer
            author_id:
              type: integer
            added_date:
              type: string
              format: date
            comment:
              type: string
            listen_count:
              type: integer
            last_listen_date:
              type: string
              format: date
    responses:
      201:
        description: Favorite artist created
      400:
        description: Invalid data
    """
    data = request.get_json()
    user_id = data.get('user_id')
    author_id = data.get('author_id')
    added_date = data.get('added_date')
    comment = data.get('comment', None)
    listen_count = data.get('listen_count', 0)
    last_listen_date = data.get('last_listen_date', None)
    
    new_favorite = UserFavoriteArtistService.create_favorite(
        user_id=user_id,
        author_id=author_id,
        added_date=added_date,
        comment=comment,
        listen_count=listen_count,
        last_listen_date=last_listen_date
    )
    return jsonify(new_favorite), 201

@user_favorite_artist_bp.route('/favorites/<int:favorite_id>', methods=['GET'])
def get_favorite(favorite_id):
    """
    Get favorite artist record by ID
    ---
    tags:
      - Favorite Artists
    parameters:
      - name: favorite_id
        in: path
        type: integer
        required: true
        description: Favorite artist ID
    responses:
      200:
        description: Favorite artist found
      404:
        description: Favorite artist not found
    """
    favorite = UserFavoriteArtistService.get_favorite_by_id(favorite_id)
    if favorite:
        return jsonify(favorite), 200
    return jsonify({'message': 'Favorite artist not found'}), 404

@user_favorite_artist_bp.route('/favorites', methods=['GET'])
def get_all_favorites():
    """
    Get all favorite artist records
    ---
    tags:
      - Favorite Artists
    responses:
      200:
        description: List of favorite artists
    """
    favorites = UserFavoriteArtistService.get_all_favorites()
    return jsonify(favorites), 200

@user_favorite_artist_bp.route('/favorites/<int:favorite_id>', methods=['PUT'])
def update_favorite(favorite_id):
    """
    Update favorite artist record by ID
    ---
    tags:
      - Favorite Artists
    parameters:
      - name: favorite_id
        in: path
        type: integer
        required: true
        description: Favorite artist ID
      - in: body
        name: body
        required: true
        schema:
          type: object
          properties:
            user_id:
              type: integer
            author_id:
              type: integer
            added_date:
              type: string
              format: date
            comment:
              type: string
            listen_count:
              type: integer
            last_listen_date:
              type: string
              format: date
    responses:
      200:
        description: Favorite artist updated
      404:
        description: Favorite artist not found
    """
    data = request.get_json()
    updated_favorite = UserFavoriteArtistService.update_favorite(favorite_id, **data)
    if updated_favorite:
        return jsonify(updated_favorite), 200
    return jsonify({'message': 'Favorite artist not found'}), 404

@user_favorite_artist_bp.route('/favorites/<int:favorite_id>', methods=['DELETE'])
def delete_favorite(favorite_id):
    """
    Delete favorite artist record by ID
    ---
    tags:
      - Favorite Artists
    parameters:
      - name: favorite_id
        in: path
        type: integer
        required: true
        description: Favorite artist ID
    responses:
      200:
        description: Favorite artist deleted successfully
      404:
        description: Favorite artist not found
    """
    if UserFavoriteArtistService.delete_favorite(favorite_id):
        return jsonify({'message': 'Favorite artist deleted successfully'}), 200
    return jsonify({'message': 'Favorite artist not found'}), 404