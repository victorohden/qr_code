from flask import Flask, jsonify, send_file
import subprocess
import datetime
import calendar

import qrcode
from PIL import Image
from io import BytesIO
import base64

app = Flask(__name__)

@app.route('/date', methods=['GET'])
def get_date():
    current_date = datetime.datetime.now()
    return jsonify({'date': current_date.strftime('%Y-%m-%d %H:%M:%S')})


@app.route('/cal', methods=['GET'])
def get_cal():
    now = datetime.datetime.now()
    current_calendar = calendar.TextCalendar().formatmonth(now.year, now.month)
    return jsonify({'calendar': current_calendar})

@app.route('/docker', methods=['GET'])
def get_docker():
    result = subprocess.check_output(['docker', 'ps']).decode('utf-8')
    return jsonify({'docker': result.strip()})

def clear_screen():
    subprocess.call('cls' if subprocess.os.name == 'nt' else 'clear', shell=True)

@app.route('/cls', methods=['GET'])
def get_cls():
    clear_screen()
    return jsonify({'cls': 'Console screen cleared'})

@app.route('/test', methods=['GET'])
def get_qrcode_url():
    # Data to be encoded
    data = 'https://lcluc.umd.edu/projects/policy-market-and-climate-change-impacts-maize-production-mexico/'
    
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
    return send_file(img_buffer, mimetype='image/png')



if __name__ == '__main__':
    app.run(debug=True)