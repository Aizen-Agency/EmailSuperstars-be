# app/routes/contact.py
from flask import Blueprint, request, jsonify, current_app
from flask_mail import Message

contact = Blueprint('contact', __name__)

@contact.route('/contact', methods=['POST'])
def handle_contact():
    try:
        data = request.json.get("data")
        print("Encrypted data:", data)

        if not data:
            return jsonify({"error": "Missing data"}), 400

        from app import mail  # Moved inside the route to avoid circular import

        msg = Message(
            subject=f"New Contact from {data['name']}",
            recipients=["junitcp21@gmail.com"],
            body=f"""
                New contact submission:

                Name: {data['name']}
                Email: {data['email']}
                Message:
                {data['message']}
                """
        )
        mail.send(msg)
        return jsonify({"message": "Message sent successfully"}), 200

    except Exception as e:
        print("Error:", e)
        return jsonify({"error": "Failed to send message"}), 500
