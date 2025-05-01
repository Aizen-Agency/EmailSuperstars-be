from flask import Blueprint, request, jsonify
from flask_mail import Message
from app.utils import mail
from app.utils.crypto import decrypt_data

contact = Blueprint('contact', __name__)

@contact.route('/contact', methods=['POST'])
def handle_contact():
    try:
        data = request.json.get("data")
        print("Encrypted data:", data)
        if not data:
            return jsonify({"error": "Missing data"}), 400

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
