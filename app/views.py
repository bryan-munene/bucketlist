from flask import Blueprint, request, jsonify, make_response, session

# Local imports
from app.models import BucketList

bucketlists_bp = Blueprint('bucketlists', __name__, url_prefix='/api/v1')
bucketlists_model = BucketList()


class BucketListViews():
    pass
