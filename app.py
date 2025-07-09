# from flask import Flask, request, jsonify, send_from_directory
# import smtplib
# from email.mime.text import MIMEText
# import os

# app = Flask(__name__, static_folder='.', static_url_path='')

# # ✅ UPDATE these with your actual email & app password
# YOUR_EMAIL = "kiksymyguy@gmail.com"
# YOUR_PASSWORD = "xnif vxqq aadj rwov"
# TO_EMAIL = "kiksymyguy@gmail.com"

# @app.route('/')
# def serve_index():
#     return send_from_directory('.', 'index.html')

# @app.route('/submit-poa', methods=['POST'])
# def submit_poa():
#     data = request.get_json()
#     name = data.get('name')
#     email = data.get('email')
#     amount = data.get('amount')
#     date = data.get('date')

#     if not name or not email or not amount:
#         return jsonify({"error": "Name, email, and amount are required."}), 400

#     poa_content = f"""
# POWER OF ATTORNEY

# KNOW ALL MEN BY THESE PRESENTS that I, {name}, of {email}, (“the Donor”), do hereby APPOINT Akinola Samuel Eluyefa, a Legal Practitioner duly qualified under the Legal Practitioners Act, Cap L11, Laws of the Federation of Nigeria 2004, and the Powers of Attorney Law, Cap P6, Laws of Lagos State 2015 (“the Attorney”), to be my true and lawful Attorney.

# WHEREAS:
# I have claims totalling the sum of ₦{amount} (Naira) against the Chairman, Directors, and relevant officers of PWAN GROUP OF COMPANIES, which arose as a result of various fraudulent actions and representations, and I am desirous of empowering my Attorney to act on my behalf in all lawful ways.

# NOW THIS DEED WITNESSES as follows:

# 1. I hereby authorise and empower my Attorney to:
#    a) Draft, adopt, sign, swear to, attest, and submit on my behalf any petitions, criminal complaints, affidavits, or statements to any law enforcement agency, including but not limited to the Economic and Financial Crimes Commission (EFCC), the Nigeria Police Force, or any other competent regulatory or prosecuting authority within the Federal Republic of Nigeria.
#    b) Represent me in writing, in person, or through electronic means in all official communications, hearings, and proceedings connected with my complaints and claims against PWAN GROUP OF COMPANIES.
#    c) Take any other lawful steps necessary to protect, pursue, and enforce my interests under applicable Nigerian law.

# 2. I hereby ratify and confirm all lawful acts which my Attorney shall lawfully do or cause to be done in pursuance of this Power of Attorney as if done by me personally.

# 3. This Power of Attorney is made voluntarily and shall remain valid and binding until expressly revoked by me in writing.

# 4. This Power of Attorney may be signed and delivered electronically and, if required, may be printed, signed by hand, and sworn before a Commissioner for Oaths or Notary Public within the Federal Republic of Nigeria for further authentication.

# 5. This Power of Attorney shall be governed by and construed in accordance with the Laws of Lagos State and the Laws of the Federation of Nigeria.

# IN WITNESS WHEREOF, I have executed this Power of Attorney by typing my full name below as my signature under Nigerian law.

# SIGNED AND EXECUTED ELECTRONICALLY ON THIS {date}.

# Full Name (Typed as Signature): {name}

# Email: {email}
# """

#     msg = MIMEText(poa_content)
#     msg['Subject'] = f"New Power of Attorney - {name}"
#     msg['From'] = YOUR_EMAIL
#     msg['To'] = TO_EMAIL

#     try:
#         with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
#             server.login(YOUR_EMAIL, YOUR_PASSWORD)
#             server.sendmail(YOUR_EMAIL, TO_EMAIL, msg.as_string())
#         return jsonify({"message": "POA sent successfully"}), 200
#     except Exception as e:
#         print("Error:", e)
#         return jsonify({"error": str(e)}), 500

# if __name__ == "__main__":
#     port = int(os.environ.get("PORT", 5000))
#     app.run(debug=True, host='0.0.0.0', port=port)




# ✅ UPDATE these with your actual email & app password


from flask import Flask, request, jsonify, send_from_directory
import smtplib
from email.mime.text import MIMEText
import os

app = Flask(__name__, static_folder='.', static_url_path='')

YOUR_EMAIL = "kiksymyguy@gmail.com"
YOUR_PASSWORD = "xnif vxqq aadj rwov"
TO_EMAIL = "kiksymyguy@gmail.com"

@app.route('/')
def serve_index():
    return send_from_directory('.', 'index.html')

@app.route('/submit-poa', methods=['POST'])
def submit_poa():
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    amount = data.get('amount')
    fake_plot = data.get('fakePlot')
    pwan_subsidiary = data.get('pwanSubsidiary')
    account_details = data.get('accountDetails')
    date = data.get('date')

    if not all([name, email, amount, fake_plot, pwan_subsidiary, account_details]):
        return jsonify({"error": "All fields are required."}), 400

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

    msg = MIMEText(poa_content)
    msg['Subject'] = f"New Power of Attorney - {name}"
    msg['From'] = YOUR_EMAIL
    msg['To'] = TO_EMAIL

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(YOUR_EMAIL, YOUR_PASSWORD)
            server.sendmail(YOUR_EMAIL, TO_EMAIL, msg.as_string())
        return jsonify({"message": "POA sent successfully"}), 200
    except Exception as e:
        print("Error:", e)
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
