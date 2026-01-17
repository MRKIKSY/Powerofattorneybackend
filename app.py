from flask import Flask, request, jsonify, send_from_directory
import smtplib, os
from email.message import EmailMessage

app = Flask(__name__, static_folder='.', static_url_path='')
app.config['MAX_CONTENT_LENGTH'] = 25 * 1024 * 1024  # 25MB

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
        return jsonify({"error": "Missing required fields"}), 400

    body = f"""
PWAN BUY2SELL SUBMISSION

Full Name: {full_name}
Email: {email}
Payment Date: {payment_date}

Account Paid Into:
{account_details}
"""

    msg = EmailMessage()
    msg["Subject"] = f"PWAN Buy2Sell Submission – {full_name}"
    msg["From"] = YOUR_EMAIL
    msg["To"] = TO_EMAIL
    msg.set_content(body)

    for file in documents:
        msg.add_attachment(
            file.read(),
            maintype="application",
            subtype="octet-stream",
            filename=file.filename
        )

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(YOUR_EMAIL, YOUR_PASSWORD)
            server.send_message(msg)
        return jsonify({"message": "Submission successful"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

