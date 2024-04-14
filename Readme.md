### Creating a QR Code

This repository contains a simple code snippet to generate a QR Code using Python and the qr-code package. The process involves setting up a virtual environment and installing necessary packages using pip. While the instructions are provided for a Windows environment with a .venv virtual environment, the process can be adapted for conda environments and other operating systems.

#### Setting Up Virtual Environment
1. Ensure Python is installed on your computer.
2. Create a virtual environment using the following command:

`python -m venv .venv

You can replace ".venv" with a different environment name if desired.

3. Activate the virtual environment by navigating to ".venv\Scripts\activate".

4. Once the virtual environment is activated, install the required packages:

`pip install qr-code
`pip install pillow


#### Generating QR Codes
- **General QR Code Generation:**
You can customize the colors and add text (such as a title) to the QR Code. Use the [General QR Code Notebook](qr_code_general.ipynb) to generate a QR code for general propouses.

![General QR-Code](./output/general_qr_code.png)

- **Virtual Business Card (Vcard):**
This feature enables you to share your contact information using a QR Code. Use the [Bussiness Card QR Code Notebook](qr-code-bussines-card.ipynb) to generate a QR code for general propouses

![Bussiness Card - QR Code](./output/vcard_Your%20Name.png)

Feel free to explore and modify the code to suit your needs!
