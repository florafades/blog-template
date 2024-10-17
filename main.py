from flask import Flask, render_template

#used to import json file of blog posts
import requests

# use api where the json file is stored for the blog posts
posts = requests.get("https://api.npoint.io/a31c7e2c5f7dce0e8ecf",  verify=False).json()

#working for loop will be re-fromatted using Jinja formatting and put into index.html
# for post in posts:
#     print(post["title"])
#     print(post["subtitle"])

app = Flask(__name__)

#/ refers to home page
@app.route("/")
def  get_all_posts():
    return render_template("index.html", all_posts=posts)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/post/<int:index>")
def show_post(index):
    #set up empty python variable
    requested_post = None
    #loop through posts to find the id # that matches the <int:index>
    for x in posts:
        if x["id"] == index:
            requested_post = x
    return render_template("post.html", post=requested_post)




if __name__ == "__main__":
    #debug auto reloads server --> good
    app.run(debug=True)