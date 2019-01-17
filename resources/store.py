from flask_restful import Resource
from models.store import StoreModel

class Store(Resource):
    def get(self, name):
        store=StoreModel.find_by_name(name)
        if store:
            return store.json()
        return {'message':'store not found!'}, 404

    def post(self, name):
        store=StoreModel.find_by_name(name)
        if store:
            return {'message':'A store with that name already exists!'}, 400
        
        new_store=StoreModel(name)

        try:
            new_store.save_to_db()
        except:
            return {'message': 'An error occured while creating the store'}, 500
        
        return new_store.json(), 201
    
    def delete(self, name):
        store=StoreModel.find_by_name(name)
        if store:
            store.delete_from_db()
        return {'message':'store deleted!'}, 201

class StoreList(Resource):
    def get(self):
        return {'stores':[store.json() for store in StoreModel.query.all()]}

