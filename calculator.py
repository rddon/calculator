from flask import Flask, request, render_template_string

app = Flask(__name__)

form = '''
<h2>Calculator</h2>
<form method="post">
  Number 1: <input type="text" name="x"><br>
  Number 2: <input type="text" name="y"><br>
  Operation:
  <select name="op">
    <option value="add">Add</option>
    <option value="sub">Subtract</option>
    <option value="mul">Multiply</option>
    <option value="div">Divide</option>
  </select><br>
  <input type="submit" value="Calculate">
</form>
{% if result is not none %}
<h3>Result: {{ result }}</h3>
{% endif %}
'''

@app.route("/", methods=["GET", "POST"])
def calc():
    result = None
    if request.method == "POST":
        try:
            x = float(request.form["x"])
            y = float(request.form["y"])
            op = request.form["op"]
            if op == "add":
                result = x + y
            elif op == "sub":
                result = x - y
            elif op == "mul":
                result = x * y
            elif op == "div":
                result = "Error" if y == 0 else x / y
        except:
            result = "Invalid input!"
    return render_template_string(form, result=result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
