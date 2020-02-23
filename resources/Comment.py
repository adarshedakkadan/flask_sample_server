from flask import jsonify, request
from flask_restful import Resource
from Model import db, Comment, Category, CommentSchema

comments_schema = CommentSchema(many=True)
comment_schema = CommentSchema()

class CommentResource(Resource):
    def get(self):
        comments = Comment.query.all()
        comments = comments_schema.dump(comments)
        if not comments:
            return {"status":"success", "data" : []}, 201
        else:
            return {"status":"success", "data":comments}, 200

    def post(self):
        json_data = request.get_json(force=True)
        if not json_data:
              return {'message': 'No input data provided'}, 400
        # Validate and deserialize input
        data = comment_schema.load(json_data)

        category_id = Category.query.filter_by(id=data['category_id']).first()
        if not category_id:
            return {'status': 'error', 'message': 'comment category not found'},201

        # if errors:
        #     return {"status": "error", "data": errors}, 422
        comments = Comment(
                category_id=json_data['category_id'],
                comment=json_data['comment']
            )

        db.session.add(comments)
        db.session.commit()

        result = comment_schema.dump(comments)
        return {'status': 'success', 'data': result},201
