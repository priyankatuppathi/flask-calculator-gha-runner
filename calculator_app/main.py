from flask import Blueprint, jsonify, request

from calculator_app.calculator import add, subtract, multiply, divide

bp = Blueprint("main", __name__)

OPERATIONS = {
    "add": add,
    "subtract": subtract,
    "multiply": multiply,
    "divide": divide,
}


@bp.route("/")
def index():
    return jsonify({"message": "Flask calculator CI app", "status": "ok"})


@bp.route("/health")
def health():
    return jsonify({"status": "healthy"}), 200


@bp.route("/calculate", methods=["POST"])
def calculate():
    data = request.get_json(silent=True) or {}
    op = data.get("operation")
    a = data.get("a")
    b = data.get("b")

    if op not in OPERATIONS:
        return jsonify({"error": f"Unknown operation: {op}"}), 400
    if a is None or b is None:
        return jsonify({"error": "Both 'a' and 'b' are required"}), 400

    try:
        result = OPERATIONS[op](a, b)
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

    return jsonify({"operation": op, "a": a, "b": b, "result": result})