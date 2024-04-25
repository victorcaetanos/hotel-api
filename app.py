from flask import Flask
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///database.db"
db = SQLAlchemy(app)


class HotelModel(db.Model):
    __tablename__ = "hotels"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    city = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"Hotel(name = {self.name}, city = {self.city}, address = {self.address})"


db.create_all()

hotel_put_args = reqparse.RequestParser()
hotel_put_args.add_argument("name", type=str, help="Name is required")
hotel_put_args.add_argument("city", type=str, help="City is required")
hotel_put_args.add_argument("address", type=str, help="Address is required")

hotel_update_args = reqparse.RequestParser()
hotel_update_args.add_argument("name", type=str, help="Name is required")
hotel_update_args.add_argument("city", type=str, help="City is required")
hotel_update_args.add_argument("address", type=str, help="Address is required")

resource_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'city': fields.String,
    'address': fields.String
}


class Hotels(Resource):

    @marshal_with(resource_fields)
    def get(self):
        result = HotelModel.query.all()
        if not result:
            abort(404, message="Could not find any hotel")
        return result, 200


class Hotel(Resource):

    @marshal_with(resource_fields)
    def get(self, hotel_id):
        result = HotelModel.query.filter_by(id=hotel_id).first()
        if not result:
            abort(404, message="Could not find a hotel with that id")
        return result, 200

    @marshal_with(resource_fields)
    def put(self, hotel_id):
        args = hotel_put_args.parse_args()
        if not args['name']:
            abort(400, message="Missing name, cannot insert")
        elif not args['city']:
            abort(400, message="Missing city, cannot insert")
        elif not args['address']:
            abort(400, message="Missing address, cannot insert")

        result = HotelModel.query.filter_by(id=hotel_id).first()
        if result:
            abort(409, message="Hotel id taken")

        hotel = HotelModel(id=hotel_id, name=args['name'], city=args['city'], address=args['address'])
        db.session.add(hotel)
        db.session.commit()
        return hotel, 201

    @marshal_with(resource_fields)
    def patch(self, hotel_id):
        args = hotel_update_args.parse_args()
        if not (args['name'] or args['city'] or args['address']):
            abort(400, message="Missing all parameters, cannot update")

        result = HotelModel.query.filter_by(id=hotel_id).first()
        if not result:
            abort(404, message="Hotel doesn't exist, cannot update")

        if args['name']:
            result.name = args['name']
        if args['city']:
            result.city = args['city']
        if args['address']:
            result.address = args['address']

        db.session.commit()

        return result, 200

    @marshal_with(resource_fields)
    def delete(self, hotel_id):
        result = HotelModel.query.filter_by(id=hotel_id).first()
        if not result:
            abort(404, message="Hotel doesn't exist, cannot delete")

        db.session.delete(result)
        db.session.commit()

        return "", 204


api.add_resource(Hotel, "/api/hotels/<int:hotel_id>")
api.add_resource(Hotels, "/api/hotels/")

if __name__ == "__main__":
    app.run(debug=True)
