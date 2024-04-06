##Import algorithms
from flask import Flask, jsonify, send_file, request
from flask_cors import CORS
import subprocess
import datetime
import calendar
import qrcode
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO
import base64
import os

app = Flask(__name__)
CORS(app)


@app.route('/qr_code', methods=['POST'])
def qr_code():

    # Data to be encoded
    # data = 'https://lcluc.umd.edu/projects/policy-market-and-climate-change-impacts-maize-production-mexico/'
    data = request.form.get('data')
    
    # Generate QR code
    qr = qrcode.QRCode(version=3, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
    qr.add_data(data)
    qr.make(fit=True)

    # Convert QR code to PIL image
    img = qr.make_image(fill_color="black", back_color="white")

    # Save PIL image to bytes buffer
    img_buffer = BytesIO()
    img.save(img_buffer, format="PNG")
    img_buffer.seek(0)

    # Return image data with appropriate content type
    response =  send_file(img_buffer, mimetype='image/png')
    return response

@app.route('/qr_code_card', methods=['POST'])
def qr_code_card():

    # Get data from the request
    first_name = request.form.get('first_name', '')
    last_name = request.form.get('last_name', '')
    email = request.form.get('email', '')
    email2 = request.form.get('email2', '')
    phone_number = request.form.get('phone_number', '')
    url = request.form.get('url', '')
    
    # Create the vCard string
    vcard = f"BEGIN:VCARD\nVERSION:3.0\nN:{last_name};{first_name};;;\nFN:{first_name}\nEMAIL;TYPE=INTERNET:{email}\nEMAIL;TYPE=INTERNET:{email2}\nTEL;TYPE=CELL:{phone_number}\nURL;TYPE=URL:{url}\nEND:VCARD"

    # Generate QR code
    qr = qrcode.QRCode(version=3, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
    qr.add_data(vcard)
    qr.make(fit=True)

    # Convert QR code to PIL image
    img = qr.make_image(fill_color="black", back_color="white")

    # Save PIL image to bytes buffer
    img_buffer = BytesIO()
    img.save(img_buffer, format="PNG")
    img_buffer.seek(0)

    # Return image data with appropriate content type
    response =  send_file(img_buffer, mimetype='image/png')
    return response

if __name__ == '__main__':
    # app.run(debug=True)
    app.run(host='0.0.0.0', port=5000, debug=True, threaded=True)



# if __name__ == '__main__':
#     app.run(host='192.168.43.81', port=5000, debug=True, threaded=False)