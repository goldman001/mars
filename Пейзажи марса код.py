from flask import Flask, url_for

app = Flask(__name__)

@app.route('/bootstrap_sample')
def bootstrap():
    return f'''<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet" 
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                    crossorigin="anonymous">
                    <title>Жди нас, Марс!</title>
                  </head>
                  <body>
                    <h1>Пейзажи Марса:</h1>
                      <img src="{url_for('static', filename='img/1.jpeg')}">
                    <div>
                      <img src="{url_for('static', filename='img/2.jpeg')}">
                    </div>
                      <img src="{url_for('static', filename='img/3.jpeg')}">
                    </div>
                      <img src="{url_for('static', filename='img/4.jpeg')}">
                    </div>
                      <img src="{url_for('static', filename='img/5.jpeg')}">
                    </div>
                      <img src="{url_for('static', filename='img/6.jpeg')}">           
                      </body>
                </html>'''

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')