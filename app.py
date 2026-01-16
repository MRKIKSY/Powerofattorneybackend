from flask import Flask, request, jsonify, send_from_directory
import smtplib
import os
from email.message import EmailMessage

app = Flask(__name__, static_folder='.', static_url_path='')

# USE ENV VARIABLES (Render / Production Safe)
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

    if not all([full_name, email, payment_date, account_details]):
        return jsonify({"error": "All fields are required."}), 400

    if not documents or len(documents) == 0:
        return jsonify({"error": "At least one document must be uploaded."}), 400

    poa_content = f"""
POWER OF ATTORNEY – SUPPORTING INFORMATION

FULL NAME:
{full_name}

EMAIL ADDRESS:
{email}

DATE PAYMENT WAS MADE INTO PWAN ACCOUNT:
{payment_date}

NAME AND ACCOUNT DETAILS PAID INTO (BUY 2 SELL):
{account_details}

This submission was made electronically
for the purpose of filing and adopting a criminal petition
before the EFCC and other relevant authorities.
"""

    msg = EmailMessage()
    msg['Subject'] = f"PWAN BUY2SELL PETITION – {full_name}"
    msg['From'] = YOUR_EMAIL
    msg['To'] = TO_EMAIL
    msg.set_content(poa_content)

    for doc in documents:
        if doc and doc.filename:
            msg.add_attachment(
                doc.read(),
                maintype='application',
                subtype='octet-stream',
                filename=doc.filename
            )

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(YOUR_EMAIL, YOUR_PASSWORD)
            server.send_message(msg)

        return jsonify({"message": "Submission successful"}), 200

    except Exception as e:
        print("Email error:", e)
        return jsonify({"error": "Submission failed"}), 500


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
