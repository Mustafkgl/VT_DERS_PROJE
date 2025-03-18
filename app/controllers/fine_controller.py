from flask import Blueprint, request, jsonify
from app.services.fine_service import FineService
from app.controllers.middleware import token_required, admin_required
import logging

logger = logging.getLogger(__name__)

fine_bp = Blueprint('fine', __name__, url_prefix='/api/fines')

@fine_bp.route('/my', methods=['GET'])
@token_required