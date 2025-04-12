from flask import Flask, render_template, request, redirect, url_for, flash

from src.data import data_actions
from src.data.forms import ReviewForm


app = Flask(__name__, template_folder="src/templates")
app.secret_key="32523252Q"


@app.get("/")
def index():
    products = data_actions.get_products()
    return render_template("index.html", products=products)


@app.route("/product/<product_id>", methods=["GET", "POST"])
def get_product(product_id):
    form = ReviewForm()

    if form.validate_on_submit():
        text = form.text.data
        name = form.name.data
        data_actions.add_review(product_id, text, name)
        return redirect(url_for("get_product", product_id=product_id))
    
    product = data_actions.get_product(product_id)
    return render_template("product.html", product=product, form=form)

@app.post("/buy_product/<product_id>")
def buy_product(product_id):
    name = request.form.get("name")
    data_actions.buy_product(product_id, name)
    return redirect(url_for("index"))



if __name__ == "__main__":
    app.run(debug=True, port=5000)