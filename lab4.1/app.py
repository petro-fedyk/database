import yaml
from flask import Flask, jsonify
from flasgger import Swagger
from extensions import db
from controller.account_controller import account_bp 
from controller.soung_controller import songs_bp      
from controller.playlist_controller import playlists_bp 
from controller.genre_controller import genre_bp 
from controller.favorit_artist_controller import user_favorite_artist_bp  
from controller.user_download_controller import user_download_song_bp

def get_version():
    try:
        with open("version.txt", "r") as f:
            return f.read().strip()
    except FileNotFoundError:
        return "0.0.0"  

def create_app():
    app = Flask(__name__)

    with open("config/app.yml", "r") as ymlfile:
        config = yaml.safe_load(ymlfile)

    app.config['SQLALCHEMY_DATABASE_URI'] = (
        f"mysql+mysqlconnector://{config['database']['user']}:{config['database']['password']}"
        f"@{config['database']['host']}/{config['database']['database']}"
    )
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = config['database'].get('secret_key', 'default_secret_key')

    db.init_app(app)


    app.register_blueprint(account_bp, url_prefix='/api')
    app.register_blueprint(songs_bp, url_prefix='/api')
    app.register_blueprint(playlists_bp, url_prefix='/api')
    app.register_blueprint(genre_bp, url_prefix='/api')
    app.register_blueprint(user_favorite_artist_bp, url_prefix='/api')
    app.register_blueprint(user_download_song_bp, url_prefix='/api')


    swagger_template = {
        "swagger": "2.0",
        "info": {
            "title": "🎶 Music Service API",
            "description": "REST API з підтримкою Swagger UI",
            "version": get_version(),   #
        },
        "basePath": "/api",
    }

    swagger_config = {
        "headers": [],
        "specs": [
            {
                "endpoint": 'apispec',
                "route": '/apispec.json',
                "rule_filter": lambda rule: True,
                "model_filter": lambda tag: True,
            }
        ],
        "static_url_path": "/flasgger_static",
        "swagger_ui": True,
        "specs_route": "/swagger/"
    }
    Swagger(app, template=swagger_template, config=swagger_config)

    @app.route('/')
    def home():
        return f'Flask app is running  (version {get_version()}) - Swagger at /swagger/'

    @app.route('/version')
    def version():
        return jsonify({
            "status": "ok",
            "version": get_version(),
            "message": "Code updated via CodePipeline"
        })

    # @app.route('/demo')
    # def demo():
    #     """
    #     Demo endpoint
    #     ---
    #     responses:
    #       200:
    #         description: Повертає статус роботи API
    #         examples:
    #           application/json: { "status": "success", "message": "Demo endpoint is working " }
    #     """
    #     return jsonify({
    #         "status": "success",
    #         "message": "Demo endpoint is working ",
    #         "version": get_version()
    #     })

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(host="0.0.0.0", port=5000)
