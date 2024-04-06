# # Importing library

import qrcode
from PIL import Image
 
# Data to be encoded
data = 'https://lcluc.umd.edu/projects/policy-market-and-climate-change-impacts-maize-production-mexico/'
 
# Encoding data using make() function
img = qrcode.make(data)

img.show() 
# print(img)
# Saving as an image file
# img.save(r"C:\Users\victorrp\OneDrive\qr_codes\lcluc_projects.png")




# Generate QR code
qr = qrcode.QRCode(version=3, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
qr.add_data(data)
qr.make(fit=True)

# Convert QR code to PIL image
img = qr.make_image(fill_color="red", back_color="white")

# Display the PIL image
img.show()