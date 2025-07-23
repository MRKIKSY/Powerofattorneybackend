

# from flask import Flask, request, jsonify, send_from_directory
# import smtplib
# import os
# from email.message import EmailMessage

# app = Flask(__name__, static_folder='.', static_url_path='')

# YOUR_EMAIL = "kiksymyguy@gmail.com"
# YOUR_PASSWORD = "xnif vxqq aadj rwov"
# TO_EMAIL = "kiksymyguy@gmail.com"

# @app.route('/')
# def serve_index():
#     return send_from_directory('.', 'index.html')

# @app.route('/submit-poa', methods=['POST'])
# def submit_poa():
#     name = request.form.get('name')
#     email = request.form.get('email')
#     amount = request.form.get('amount')
#     fake_plot = request.form.get('fakePlot')
#     pwan_subsidiary = request.form.get('pwanSubsidiary')
#     account_details = request.form.get('accountDetails')
#     date = request.form.get('date')
#     contract_file = request.files.get('contractFile')

#     if not all([name, email, amount, fake_plot, pwan_subsidiary]):
#         return jsonify({"error": "All fields except account details and file are required."}), 400

#     # Compose email content
#     poa_content = f"""
# POWER OF ATTORNEY

# Name: {name}
# Email: {email}
# Claim Amount (₦): {amount}

# Non-existent Plot/Estate: {fake_plot}
# PWAN Subsidiary: {pwan_subsidiary}
# PWAN Subsidiary Bank Account Details: {account_details}

# SIGNED AND EXECUTED ELECTRONICALLY ON THIS {date}.
# """

#     # Create email message
#     msg = EmailMessage()
#     msg['Subject'] = f"New Power of Attorney - {name}"
#     msg['From'] = YOUR_EMAIL
#     msg['To'] = TO_EMAIL
#     msg.set_content(poa_content)

#     # Attach contract file
#     if contract_file:
#         file_data = contract_file.read()
#         file_name = contract_file.filename
#         msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)

#     try:
#         with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
#             server.login(YOUR_EMAIL, YOUR_PASSWORD)
#             server.send_message(msg)
#         return jsonify({"message": "POA and contract uploaded successfully"}), 200
#     except Exception as e:
#         print("Error:", e)
#         return jsonify({"error": str(e)}), 500

# if __name__ == "__main__":
#     port = int(os.environ.get("PORT", 5000))
#     app.run(debug=True, host='0.0.0.0', port=port)




from flask import Flask, request, jsonify, send_from_directory
import smtplib
import os
from email.message import EmailMessage

app = Flask(__name__, static_folder='.', static_url_path='')

YOUR_EMAIL = "kiksymyguy@gmail.com"
YOUR_PASSWORD = "xnif vxqq aadj rwov"
TO_EMAIL = "kiksymyguy@gmail.com"

@app.route('/')
def serve_index():
    return send_from_directory('.', 'index.html')

@app.route('/submit-poa', methods=['POST'])
def submit_poa():
    name = request.form.get('name')
    email = request.form.get('email')
    amount = request.form.get('amount')
    fake_plot = request.form.get('fakePlot')
    pwan_subsidiary = request.form.get('pwanSubsidiary')
    account_details = request.form.get('accountDetails')
    date = request.form.get('date')
    contract_file = request.files.get('contractFile')

    if not all([name, email, amount, fake_plot, pwan_subsidiary]):
        return jsonify({"error": "All fields except account details and file are required."}), 400

    # Compose email content
    poa_content = f"""
POWER OF ATTORNEY

Name: {name}
Email: {email}
Claim Amount (₦): {amount}

Non-existent Plot/Estate: {fake_plot}
PWAN Subsidiary: {pwan_subsidiary}
PWAN Subsidiary Bank Account Details: {account_details}

SIGNED AND EXECUTED ELECTRONICALLY ON THIS {date}.
"""

    # Create email message
    msg = EmailMessage()
    msg['Subject'] = f"New Power of Attorney - {name}"
    msg['From'] = YOUR_EMAIL
    msg['To'] = TO_EMAIL
    msg.set_content(poa_content)

    # Attach contract file
    if contract_file:
        file_data = contract_file.read()
        file_name = contract_file.filename
        msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(YOUR_EMAIL, YOUR_PASSWORD)
            server.send_message(msg)
        return jsonify({"message": "POA and contract uploaded successfully"}), 200
    except Exception as e:
        print("Error:", e)
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)

