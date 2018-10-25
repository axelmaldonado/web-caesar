from flask import Flask, request
from caesar import rotate_string


app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!DOCTYPE html>

<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>
        <form action="/" method="POST">
            Rotate by: 
            <input type="text" id="rot" name="rot" value="0"/>
                <textarea id="textarea" name="textarea">{0}</textarea>
        <input type="submit" value="Submit"/>
    </form>
    </body>
</html>
"""

@app.route("/")
def index():
    return form.format("")

@app.route("/", methods=['POST'])
def encrypt():
    web_rot = int(request.form['rot'])
    web_text = request.form['textarea']

    return form.format(rotate_string(web_text, web_rot))
    #return "<h1>" + rotate_string(web_text, web_rot) +  "</h1>"



app.run()