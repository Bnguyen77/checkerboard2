from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def helloWorld():
    return "welcome World"

@app.route('/<x>/<y>')
def context(x,y):
    x=int(x)
    y=int(y)
    return render_template("index.html",x=x, y=y)





if __name__=="__main__":
    app.run(debug=True)
