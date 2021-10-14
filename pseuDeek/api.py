from flask import Flask
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
import sqlite3 as sql

TRACKS, ALBUMS, ARTISTS = {}, {}, {}

app = Flask(__name__)

class api(Resource):
    def __init__(self):
        app.run(port=8000, debug=True)

    def track_put_args(a=None):
        args = reqparse.RequestParser()
        args.add_argument('name', type=str, help='Name of Video is required', required=True)
        args.add_argument('deezer_id', type=int, help='Deezer id is required', required=True)
        return args


    def album_put_args(a=None):
        args = reqparse.RequestParser()
        args.add_argument('name', type=str, help='Name of Video is required', required=True)
        args.add_argument('deezer_id', type=int, help='Deezer id is required', required=True)
        args.add_argument('artist_id', type=int, help='Deezer id is required', required=False)
        return args

    @app.route('/tracks', methods=['GET'])
    def get_tracks(a=None):
        return {
            'ok': 'yes',
            'no': 'not ok'
        }

    @app.route('/track/<int:id>', methods=['GET'])
    def get_track(a=None, id=0):
        """GET ONE specific Track"""
        return {
            'track':'info'
        }


    @app.route('/track', methods=['POST'])
    def post_track(a=None):
        args = api.track_put_args().parse_args()
        '''POST A Specific ONE Track'''
        return {
            'track':args['name'],
            'id':args['deezer_id']
        }

    @app.route('/albums/<int:album_id>', methods=['GET'])
    def get_album(a=None, album_id=0):
        '''GET info about a specific album'''
        return {
            'album':'info',
            'id':album_id
        }


    @app.route('/albums', methods=['POST'])
    def post_album(a=None):
        '''POST info about album after the album has been created and tracks individually added'''
        args = api.album_put_args().parse_args()

        return {
            'album': args['name'],
            'id': args['deezer_id'],
            'artist': args['artist_id']
        }, 201

    @app.route('/artists/<int:art_id>', methods=['GET'])
    def get_artists(a=None, art_id=0):
        '''GET artist info'''
        return {
            'arist':'fm',
            'id': art_id
        }, 200

    @app.route('/artists', methods=['POST'])
    def post_artists(a=None):
        '''POST new artist'''
        return {
                   'arist': 'fm',
                   'id': 'posted'
               }, 201




#@app.route('/movies', methods=['GET'])
#nothing.get_movies()
# def get_movies():
#     '''Function to get all the movies in the database'''
#     return {
#         'ok':'yes',
#         'no':'not ok'
#     }


if __name__ == "__main__":
    no = api()