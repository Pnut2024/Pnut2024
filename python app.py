from flask import Flask, render_template, request, redirect, url_for, send_file
from fpdf import FPDF
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    response1 = request.form.get('partner1')
    response2 = request.form.get('partner2')

    if response1 == 'i_do' and response2 == 'i_do':
        status = "Certified Husband and Wife"
        filename = generate_certificate(status)
    else:
        status = "Marriage Invalid"
        filename = generate_certificate(status)

    return send_file(filename, as_attachment=True)

def generate_certificate(status):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="Marriage Certificate", ln=True, align='C')
    pdf.ln(10)
    pdf.cell(200, 10, txt=status, ln=True, align='C')

    filename = "certificate.pdf"
    pdf.output(filename)
    return filename

if __name__ == '__main__':
    app.run(debug=True)
Step 3: Create the HTML Form
templates/index.html
html
Copy code
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Online Marriage Platform</title>
</head>
<body>
    <h1>Online Marriage Ceremony</h1>
    <form action="{{ url_for('submit') }}" method="post">
        <h3>Partner 1:</h3>
        <input type="radio" id="i_do" name="partner1" value="i_do">
        <label for="i_do">I Do</label><br>
        <input type="radio" id="decline" name="partner1" value="decline">
        <label for="decline">Decline</label><br>

        <h3>Partner 2:</h3>
        <input type="radio" id="i_do" name="partner2" value="i_do">
        <label for="i_do">I Do</label><br>
        <input type="radio" id="decline" name="partner2" value="decline">
        <label for="decline">Decline</label><br>

        <input type="submit" value="Submit">
    </form>
</body>
</html>
