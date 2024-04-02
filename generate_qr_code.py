# # Importing library
# import qrcode
 
# # Data to be encoded
# data = 'https://lcluc.umd.edu/projects/policy-market-and-climate-change-impacts-maize-production-mexico/'
 
# # Encoding data using make() function
# img = qrcode.make(data)
 


# # Saving as an image file
# img.save(r"C:\Users\victorrp\OneDrive\qr_codes\lcluc_projects.png")

import qrcode
from PIL import Image, ImageDraw, ImageFont

links_data = {"LCLUC project": 'https://lcluc.umd.edu/projects/policy-market-and-climate-change-impacts-maize-production-mexico',
              "@Meha__Jain": 'https://twitter.com/meha__jain' ,
              "@victorohden": 'https://twitter.com/victorohden',
              "Meha's Lab": 'https://mehajain.weebly.com/',
              "Poster" : 'https://1drv.ms/p/s!AjCsXAfmoh94m_kfSbYG3ByUfI-0JQ?e=LPlpzO' 
                }
for text, data in links_data.items():
    # Data to be encoded
    # data = 'https://lcluc.umd.edu/projects/policy-market-and-climate-change-impacts-maize-production-mexico/'

    # Encoding data using make() function
    img = qrcode.make(data)

    # Converting the image to RGB mode
    img = img.convert('RGB')

    # Creating a drawing object
    draw = ImageDraw.Draw(img)

    # Text to be added
    # text = "Project website"

    # Font style and size
    font = ImageFont.truetype("arial.ttf", 30)

    # Position to add the text (centered horizontally, top)
    text_position = (50, 5)

    # Adding the text to the image
    draw.text(text_position, text, fill="black", font=font)

    # Saving the image with text
    img.save(rf"C:\Users\victorrp\OneDrive\qr_codes\{text}.png")



# Define the contact information for the vCard
first_name = "Victor Hugo"
last_name = "Rohden Prudente"
email = "victorrp@umich.edu"
phone_number = "+1(734)450-8270"
url = "https://twitter.com/victorohden"
# Create the vCard string
# vcard = f"BEGIN:VCARD\nVERSION:3.0\nN:{last_name};{first_name};;;\nFN:{first_name}\nEMAIL;TYPE=INTERNET:{email}\nTEL;TYPE=CELL:{phone_number}\nEND:VCARD"
# vcard = f"BEGIN:VCARD\nVERSION:3.0\nN:{last_name};{first_name};;;\nFN:{first_name}\nEMAIL;TYPE=INTERNET:{email}\nTEL;TYPE=CELL:{phone_number}\nURL;TYPE=X:{url}\nEND:VCARD"
vcard = f"BEGIN:VCARD\nVERSION:3.0\nN:{last_name};{first_name};;;\nFN:{first_name}\nEMAIL;TYPE=INTERNET:{email}\nURL;TYPE=X:{url}\nEND:VCARD"
# Generate the QR code
img = qrcode.make(vcard)

# Converting the image to RGB mode
img = img.convert('RGB')

# Creating a drawing object
draw = ImageDraw.Draw(img)

# Text to be added
# text = "Project website"

# Font style and size
font = ImageFont.truetype("arial.ttf", 30)

# Position to add the text (centered horizontally, top)
text_position = (50, 5)

# Adding the text to the image
draw.text(text_position,  "Victor Prudente", fill="black", font=font)

img.save(rf"C:\Users\victorrp\OneDrive\qr_codes\vcard_victor.png")

# Define the contact information for the vCard
first_name = "Victor Hugo"
last_name = "Rohden Prudente"
email = "victorrp@umich.edu"
email2 = "victor.rprudente@gmail.com"
phone_number = "+1(734)450-8270"
url = "https://twitter.com/victorohden"
# Create the vCard string
# vcard = f"BEGIN:VCARD\nVERSION:3.0\nN:{last_name};{first_name};;;\nFN:{first_name}\nEMAIL;TYPE=INTERNET:{email}\nTEL;TYPE=CELL:{phone_number}\nEND:VCARD"
vcard = f"BEGIN:VCARD\nVERSION:3.0\nN:{last_name};{first_name};;;\nFN:{first_name}\nEMAIL;TYPE=INTERNET:{email}\nEMAIL;TYPE=INTERNET:{email2}\nTEL;TYPE=CELL:{phone_number}\nURL;TYPE=X:{url}\nEND:VCARD"
# vcard = f"BEGIN:VCARD\nVERSION:3.0\nN:{last_name};{first_name};;;\nFN:{first_name}\nEMAIL;TYPE=INTERNET:{email}\nURL;TYPE=X:{url}\nEND:VCARD"
# Generate the QR code
img = qrcode.make(vcard)

# Converting the image to RGB mode
img = img.convert('RGB')

# Creating a drawing object
draw = ImageDraw.Draw(img)

# Text to be added
# text = "Project website"

# Font style and size
font = ImageFont.truetype("arial.ttf", 30)

# Position to add the text (centered horizontally, top)
text_position = (50, 5)

# Adding the text to the image
draw.text(text_position,  "Victor Prudente", fill="black", font=font)

img.save(rf"C:\Users\victorrp\OneDrive\qr_codes\vcard_victor_v2.png")


# Define the contact information for the vCard
first_name = "Meha"
last_name = "Jain"
email = "mehajain@umich.edu"
phone_number = "+1(734)764-5707"
url = "https://twitter.com/meha__jain"
url2 = "https://mehajain.weebly.com/"
# Create the vCard string
# vcard = f"BEGIN:VCARD\nVERSION:3.0\nN:{last_name};{first_name};;;\nFN:{first_name}\nEMAIL;TYPE=INTERNET:{email}\nTEL;TYPE=CELL:{phone_number}\nEND:VCARD"
# vcard = f"BEGIN:VCARD\nVERSION:3.0\nN:{last_name};{first_name};;;\nFN:{first_name}\nEMAIL;TYPE=INTERNET:{email}\nTEL;TYPE=CELL:{phone_number}\nURL;TYPE=X:{url}\nURL;TYPE=WEBSITE:{url2}\nEND:VCARD"
vcard = f"BEGIN:VCARD\nVERSION:3.0\nN:{last_name};{first_name};;;\nFN:{first_name}\nEMAIL;TYPE=INTERNET:{email}\nURL;TYPE=X:{url}\nURL;TYPE=WEBSITE:{url2}\nEND:VCARD"
# Generate the QR code
img = qrcode.make(vcard)

# Converting the image to RGB mode
img = img.convert('RGB')

# Creating a drawing object
draw = ImageDraw.Draw(img)

# Text to be added
# text = "Project website"

# Font style and size
font = ImageFont.truetype("arial.ttf", 30)

# Position to add the text (centered horizontally, top)
text_position = (50, 5)

# Adding the text to the image
draw.text(text_position, "Meha Jain", fill="black", font=font)

img.save(rf"C:\Users\victorrp\OneDrive\qr_codes\vcard_meha.png")