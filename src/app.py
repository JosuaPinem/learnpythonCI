from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
	return "Hello, world!"

@app.route("/perulangan")
def perulangan():
	return [i for i in range(1,11)]

if __name__ == "__main__":
	app.run()
