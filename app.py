from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)


menu = {
    "Pizza": 180,
    "Pasta": 160,
    "Burger": 120,
    "Salad": 140,
    "Coffee": 100,
    "Milkshake": 150,
    "Juice": 90,
    "Chinese": 170,
    "Pav Bhaji": 130
}


cart = {}


@app.route('/', methods=['GET', 'POST'])
def home():
    global cart

    if request.method == "POST":

        
        if request.form.get("order"):
            return redirect(url_for('summary'))

        
        item = request.form.get("item")

        if item:
            qty = int(request.form.get(f"qty_{item}", 1))

            if item in cart:
                cart[item] += qty
            else:
                cart[item] = qty

    return render_template("index.html", menu=menu)



@app.route('/summary')
def summary():
    global cart

    total = 0
    for item, qty in cart.items():
        total += menu[item] * qty

    temp_cart = cart.copy()   
    cart.clear()              

    return render_template("result.html", cart=temp_cart, menu=menu, total=total)



@app.route('/clear')
def clear_cart():
    global cart
    cart.clear()
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)

