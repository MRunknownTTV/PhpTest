from flask import Flask

app = Flask(__name__)

@app.route("/hello")
def hello():
    return "Hello from Python!"

app.run(debug=True, port=8000)

print("hello world")
if (1 < 2):
    print("1 is less than 2")
    
    first_name = "Sven"
    
    print(f"Hello {first_name}")

    