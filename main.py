from flask import Flask, render_template, request
#used to import json file of blog posts
import requests
#used to send email to site owner (me)
import smtplib

app = Flask(__name__)

# use api where the json file is stored for the blog posts
posts = requests.get("https://api.npoint.io/a31c7e2c5f7dce0e8ecf",  verify=False).json()
MY_EMAIL = "maiaaudreysarwer@gmail.com"
MY_PASSWORD = "jugy ktqv nxly kmnm"

#working for loop will be re-fromatted using Jinja formatting and put into index.html
# for post in posts:
#     print(post["title"])
#     print(post["subtitle"])

#Update the code in contact.html and main.py so that you print the information the user has entered into the form and return a <h1> that says "Successfully sent your message". e.g.

#/ refers to home page
@app.route("/")
def  get_all_posts():
    return render_template("index.html", all_posts=posts)

@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        data = request.form
        data = request.form
        send_email(data["name"], data["email"], data["phone"], data["message"])
        return render_template("contact.html", msg_sent=True)
    return render_template("contact.html", msg_sent=False)


def send_email(name, email, phone, message):
    email_message = f"Subject:New Message\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage:{message}"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(MY_EMAIL, MY_EMAIL, email_message)

# @app.route("/form-entry", methods=["POST"])
# def receive_data():
#     #['pwd'] is connected to index.html --> <label for="pwd"> and <input id="pwd">
#     name_input = request.form['name']
#     email_input = request.form['email']
#     phone_input = request.form['phone']
#     print(name_input)
#     print(email_input)
#     print(phone_input)
#     return "Successfully sent your message"

# @app.route("/post/<int:index>")
# def show_post(index):
#     #set up empty python variable
#     requested_post = None
#     #loop through posts to find the id # that matches the <int:index>
#     for x in posts:
#         if x["id"] == index:
#             requested_post = x
#     return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    #debug auto reloads server --> good
    app.run(debug=True)