from flask import Flask
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
#from dictionary import dictionary
from flask_sqlalchemy import SQLAlchemy
import websocket

app = Flask(__name__)
api = Api(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

class VideoModel(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100), nullable=False)
    channel_name = db.Column(db.String(100), nullable = False)
    channel_id = db.Column(db.Integer, nullable = False)
    views = db.Column(db.Integer, nullable = False)
    likes = db.Column(db.Integer, nullable = False)
    date = db.Column(db.Integer, nullable = False)

    def __repr__(self):
        return '<User %r>' % self.name

#db.create_all()


# videos = {}

vid_put_args = reqparse.RequestParser()
vid_put_args.add_argument('name', type=str, help='Name of Video', required=True)
vid_put_args.add_argument('channel_name', type=str, help='Creator of Video')
vid_put_args.add_argument('channel_id', type=int, help='Channel id of creator of Video is required', required=True)
vid_put_args.add_argument('views', type=int, help='views of Video')
vid_put_args.add_argument('likes', type=int, help='likes on Video')
vid_put_args.add_argument('date', type=int, help='date the Video was created is required', required=True)


vid_update_args = reqparse.RequestParser()
vid_update_args.add_argument('name', type=str, help='Name of Video')
vid_update_args.add_argument('channel_name', type=str, help='Creator of Video')
vid_update_args.add_argument('channel_id', type=int, help='Channel id of creator of Video is required')
vid_update_args.add_argument('views', type=int, help='views of Video')
vid_update_args.add_argument('likes', type=int, help='likes on Video')
vid_update_args.add_argument('date', type=int, help='date the Video was created is required')

resource_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'channel_name': fields.String,
    'channel_id':fields.Integer,
    'views':fields.Integer,
    'likes': fields.Integer,
    'date': fields.Integer
}

class Videos(Resource):

    def vid_doesnt_exist(self, vid_id):
        results = VideoModel.query.filter_by(id=vid_id).first()
        if not results:
            abort(404, message='Video does not exist')

    def vid_already_exists(self, vid_id):
        results = VideoModel.query.filter_by(id=vid_id).first()
        if results:
            abort(409, message='Video already exists')

    @marshal_with(resource_fields)
    def get(self, vid_id):
        results = VideoModel.query.filter_by(id=vid_id).first()
        self.vid_doesnt_exist(vid_id=vid_id)
        return results

    @marshal_with(resource_fields)
    def put(self, vid_id):
        args = vid_put_args.parse_args()
        video = VideoModel(id=vid_id, name=args['name'], channel_name=args['channel_name'], channel_id=args['channel_id'], views=args['views'], likes=args['likes'], date=args['date'])
        self.vid_already_exists(vid_id=vid_id)
        db.session.add(video)
        db.session.commit()
        return video, 201

        #return videos[vid_id], 201

    @marshal_with(resource_fields)
    def patch(self, vid_id):
        args = vid_update_args.parse_args()
        results = VideoModel.query.filter_by(id=vid_id).first()
        old = results
        if not results:
            abort(404, message='Video does not exist')

        if args['name']:
            results.name = args['name']
        if args['channel_name']:
            results.channel_name = args['channel_name']
        if args['channel_id']:
            results.channel_id = args['channel_id']
        if args['views']:
            results.views = args['views']
        if args['likes']:
            results.likes = args['likes']
        if args['date']:
            results.date = args['date']

        db.session.commit()

        return results
    # def delete(self, vid_id):
    #     self.vid_doesnt_exist(vid_id=vid_id)
    #     del videos[vid_id]
    #     return {'message': 'deleted succesfully',
    #             'status': 204}

api.add_resource(Videos, '/watch/<int:vid_id>')


# class HelloWorld(Resource):
#
#     def get(self, word, age):
#         return {
#             'data':{
#                 'message':'maniacs say hello world',
#                 'name':word,
#                 'meaning': dictionary[word],
#                 'Word Count': len(dictionary[word])
#             }
#         }
#
#     def post(self):
#         return {
#             'message': 'the maniacs posted'
#         }
#
# api.add_resource(HelloWorld, "/helloworld/<string:word>/<int:age>")

if __name__ == '__main__':
    app.run(debug=True)
