from flask import render_template,request,Blueprint
from .. request import get_random_quote
from flaskblog.models import Post

main = Blueprint('main',__name__)

@main.route("/")
@main.route("/home")
def home():
  posts = Post.query.all()
  random_quote = get_random_quote()
  return render_template('home.html', posts=posts, random_quote=random_quote)

@main.route("/about")
def about():
  return render_template('about.html' , title = 'About')