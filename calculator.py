from flask import Flask, request, render_template_string

app = Flask(__name__)

# Define your functions
def add(x, y): return x + y
def subtract(x, y): return x - y
def multiply(x, y): return x * y
def divide(x, y): return "Error! Division by zero." if y == 0 else x / y

# HTML form
form_html = '''
    <h2>Simple Web Calculator</h2>
    <form method="post">
        Number 1: <input type="text" name="num1"><br>
        Number 2: <input type="text" name="num2"><br>
        Operation:
        <select name="operation">
            <option value="add">Add</option>
            <option value="subtract">Subtract</option>
            <option value="multiply">Multiply</option>
            <option value="divide">Divide</option>
        </select><br>
        <input type="submit" value="Calculate">
    </form>
    {% if result is not none %}
        <h3>Result: {{ result }}</h3>
    {% endif %}
'''

@app.route("/", methods=["GET", "POST"])
def calculator():
    result = None
    if request.method == "POST":
        try:
            x = float(request.form["num1"])
            y = float(request.form["num2"])
            op = request.form["operation"]

            if op == "add": result = add(x, y)
            elif op == "subtract": result = subtract(x, y)
            elif op == "multiply": result = multiply(x, y)
            elif op == "divide": result = divide(x, y)
        except:
            result = "Invalid input"
    return render_template_string(form_html, result=result)

