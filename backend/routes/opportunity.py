from flask import Blueprint, request, jsonify
from models import db, Opportunity

opp_bp = Blueprint('opp', __name__)

@opp_bp.route('/opportunities/<int:user_id>', methods=['GET'])
def get_opps(user_id):
    opps = Opportunity.query.filter_by(user_id=user_id).all()
    
    result = []
    for o in opps:
        result.append({
            "id": o.id,
            "name": o.name,
            "duration": o.duration,
            "start_date": o.start_date,
            "description": o.description,
            "skills": o.skills,
            "category": o.category,
            "future": o.future,
            "max_applicants": o.max_applicants
        })
    return jsonify(result)


@opp_bp.route('/opportunity', methods=['POST'])
def create_opp():
    data = request.json

    opp = Opportunity(**data)
    db.session.add(opp)
    db.session.commit()

    return jsonify({"message": "Created"})


@opp_bp.route('/opportunity/<int:id>', methods=['PUT'])
def update_opp(id):
    data = request.json
    opp = Opportunity.query.get(id)

    for key, value in data.items():
        setattr(opp, key, value)

    db.session.commit()
    return jsonify({"message": "Updated"})


@opp_bp.route('/opportunity/<int:id>', methods=['DELETE'])
def delete_opp(id):
    opp = Opportunity.query.get(id)
    db.session.delete(opp)
    db.session.commit()

    return jsonify({"message": "Deleted"})