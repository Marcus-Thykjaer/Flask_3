from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
     return """
    <h1>Home</h1>
    <p>Velkommen min nettside</p>
    <ul>
        <li><a href="/aboutme">About Me</a></li>
        <li><a href="/Fisker">Fisker</a></li>
        <li><a href="/Dyr">Dyr</a></li>
    </ul>
    """

if __name__ == '__main__':
    app.run(debug=True)