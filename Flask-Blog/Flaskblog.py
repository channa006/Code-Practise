from flask import Flask, render_template, url_for

app = Flask(__name__)

posts = [
    {
        'title': 'BlogPost1',
        'author': 'Channa',
        'content': 'Blogspot Posts 1',
        'date_posted': 'Jan 21 2021'
    },
    {
        'title': 'BlogPost2',
        'author': 'Channa2',
        'content': 'Blogspot Posts 2',
        'date_Posted': 'Jan 22 2021'
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", posts=posts)


@app.route("/about")
def about():
    return render_template("about.html", title='About Page')


if __name__ == '__main__':
    app.run(debug=True)
