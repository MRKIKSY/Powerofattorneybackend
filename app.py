from flask import Flask, request, jsonify, send_from_directory
import smtplib
import os
from email.message import EmailMessage

app = Flask(__name__, static_folder='.', static_url_path='')
app.config['MAX_CONTENT_LENGTH'] = 25 * 1024 * 1024  # 25MB limit

# Environment variables (set these on Render)
YOUR_EMAIL = os.environ.get("YOUR_EMAIL")
YOUR_PASSWORD = os.environ.get("YOUR_PASSWORD")
TO_EMAIL = os.environ.get("TO_EMAIL")


@app.route('/')
def serve_index():
    return send_from_directory('.', 'index.html')


@app.route('/submit-poa', methods=['POST'])
def submit_poa():
    full_name = request.form.get('fullName')
    email = request.form.get('email')
    payment_date = request.form.get('paymentDate')
    account_details = request.form.get('accountDetails')
    documents = request.files.getlist('documents')

    if not full_name or not email or not payment_date or not account_details or not documents:
        return jsonify({"error": "All fields and at least one document are required"}), 400

    email_body = f"""
PWAN BUY2SELL PETITION SUBMISSION

Full Name: {full_name}
Email: {email}
Date Payment Was Made: {payment_date}

Account Paid Into:
{account_details}

This submission was executed electronically.
"""

    msg = EmailMessage()
    msg['Subject'] = f"PWAN Buy2Sell Submission - {full_name}"
    msg['From'] = YOUR_EMAIL
    msg['To'] = TO_EMAIL
    msg.set_content(email_body)

    for file in documents:
        if file and file.filename:
            msg.add_attachment(
                file.read(),
                maintype='application',
                subtype='octet-stream',
                filename=file.filename
            )

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(YOUR_EMAIL, YOUR_PASSWORD)
            server.send_message(msg)
        return jsonify({"message": "Submission successful"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

