from flask import Flask, render_template, url_for

# from flask_wtf import FlaskForm, LoginForm

app = Flask(__name__)


@app.route("/index/<title>")
def index(title):
    return render_template("base.html", title=title)


@app.route("/training/<prof>")
def train(prof):
    return render_template("fly.html", prof=prof)


@app.route("/list_prof/<ss>")
def listt(ss):
    ls = ["Инженер-исследователь", "Инженер-строитель", "Пилот", "Метеоролог", "Инженер по жизнеобеспечению",
          "Инженер по радиационной защите", "Врач", "Экзобиолог"]
    return render_template("list.html", ss=ss, ls=ls)


@app.route("/answer")
@app.route("/auto_answer")
def answer():
    data = {
        "title": "Анкета",
        "surname": "Watny",
        "name": "Mark",
        "education": "выше среднего",
        "profession": "штурман марсохода",
        "sex": "male",
        "motivation": "Всегда мечтал застрять на Марсе!",
        "ready": "True"
    }
    return render_template("auto_answer.html", **data)


# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     form = LoginForm()
#     if form.validate_on_submit():
#         return redirect('/success')
#     return render_template('login.html', title='Авторизация', form=form)


@app.route("/distribution")
def distribution():
    ls = ["Ридли Скотт", "Энди Уир", "Марк Уотни", "Венката Капур", "Тедди Сандерс", "Шон Бин"]
    return render_template("distribution.html", ls=ls)


@app.route("/table/<sex>/<int:age>")
def table(sex, age):
    return render_template("table.html", sex=sex, age=age)


@app.route('/carousel')
def carousel():
    return f'''<!doctype html>
                <html lang="ru">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                   <link rel="stylesheet"
                   href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                   integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                   crossorigin="anonymous">
                   <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/js/bootstrap.bundle.min.js" integrity="sha384-FKyoEForCGlyvwx9Hj09JcYn3nv7wiPVlz7YYwJrWVcXK/BmnVDxM+D2scQbITxI" crossorigin="anonymous"></script>
                    <title>Варианты выбора</title>
                  </head>
                  <body>
                    <div id="carouselExampleRide" class="carousel slide" data-bs-ride="true">
  <div class="carousel-inner">
    <div class="carousel-item active">
      <img src="{url_for('static', filename='img/igor.jpg')}" class="d-block w-100" alt="igor1">
    </div>
    <div class="carousel-item">
      <img src="{url_for('static', filename='img/igor1.jpg')}" class="d-block w-100" alt="igor2">
    </div>
    <div class="carousel-item">
      <img src="{url_for('static', filename='img/igor2.jpg')}" class="d-block w-100" alt="igor3">
    </div>
    <div class="carousel-item">
      <img src="{url_for('static', filename='img/igor3.jpg')}" class="d-block w-100" alt="igor4">
    </div>
    <div class="carousel-item">
      <img src="{url_for('static', filename='img/igor4.jpg')}" class="d-block w-100" alt="igor5">
    </div>
  </div>
  <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleRide" data-bs-slide="prev">
    <span class="carousel-control-prev-icon" aria-hidden="true"></span>
    <span class="visually-hidden">Previous</span>
  </button>
  <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleRide" data-bs-slide="next">
    <span class="carousel-control-next-icon" aria-hidden="true"></span>
    <span class="visually-hidden">Next</span>
  </button>
</div>
                  </body>
                </html>'''


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=7990, debug=True)
