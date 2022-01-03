from flask import Flask, render_template, request, redirect, url_for, flash
import requests
import os
import smtplib
from flask_bootstrap import Bootstrap
from flask_ckeditor import CKEditor, CKEditorField



#initializing flask app
app = Flask(__name__)
# chrome_driver_path = r"C:\Users\tramr\OneDrive\Desktop\website\development\chromedriver.exe"
# driver = webdriver.Chrome(executable_path=chrome_driver_path)
GMAIL = os.environ.get('GMAIL')
PASSWORD = os.environ.get('GMAIL_PASSWORD')
ACCESS_KEY = os.environ.get("UNSPLASH_ACCESS_KEY")
SECRET_KEY = os.environ.get("UNSPLASH_SECRETE_KEY")
app.config['SECRET_KEY'] = os.environ.get("APP_SECRET_KEY")
ckeditor = CKEditor(app)
Bootstrap(app)


@app.route('/')
def home():
    # all_post = City.query.all()
    return render_template('index.html',)


@app.route('/about')
def about():
    return render_template('about.html', )


@app.route('/work')
def work():
    return render_template('work.html', )



@app.route('/contact', methods=['POST', 'GET'])
def contact():
    if request.method == "POST":
        data = request.form
        try:
            with smtplib.SMTP("smtp.gmail.com", port=587) as connection:

                connection.starttls()
                connection.login(user=GMAIL, password=PASSWORD)
                connection.sendmail(
                    from_addr=GMAIL,
                    to_addrs=data["email"],
                    msg=f"Subject: Message from {data['name']} \n\n {data['message'].encode('utf-8',errors='ignore')}"
                )
        except smtplib.SMTPAuthenticationError:
            print("Error enable less secure apps in google")
        # except UnicodeEncodeError:
        # print("'ascii' codec can't encode character")

        return render_template('contact.html', msg_sent=True)
    return render_template('contact.html', msg_sent=False,)

if __name__ == "__main__":
    # app.run(debug=True)
    app.run(host='0.0.0.0', port=5000)
