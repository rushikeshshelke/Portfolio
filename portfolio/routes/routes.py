from flask import Blueprint, render_template, url_for, abort
from portfolio.commonLibs.globalVariables import GlobalVariables

pages = Blueprint("portfolio",__name__,template_folder="../templates")

@pages.route("/")
def home():
    return render_template('home.html', projects=GlobalVariables.PROJECTS)

@pages.route("/about")
def about():
    return render_template("about.html")

@pages.route("/contact")
def contact():
    return render_template("contact.html")

@pages.route("/project/<string:slug>")
def project(slug):
    if slug not in GlobalVariables.SLUG_IN_PROJECT:
        abort(404)
    return render_template(
        "project_{}.html".format(slug),
        project=GlobalVariables.SLUG_IN_PROJECT[slug]
    )

@pages.errorhandler(404)
def pageNotFound(error):
    return render_template("404.html"), 404