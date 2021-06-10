from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://my_user:my_password@172.17.0.2/szczepienia'
db = SQLAlchemy(app)

class Pacjent(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    imie = db.Column(db.String(200), nullable=False)
    nazwisko = db.Column(db.String(200), nullable=False)
    pesel = db.Column(db.String(200), nullable=False)
    data = db.Column(db.String(200), nullable=False)
    godzina = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return '<Pacjent %r>' % self.id


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        pacjent_imie = request.form['imie']
        pacjent_nazwisko = request.form['nazwisko']
        pacjent_pesel = request.form['pesel']
        pacjent_data = request.form['data']
        pacjent_godzina = request.form['godzina']

        new_pacjent = Pacjent(imie=pacjent_imie,nazwisko=pacjent_nazwisko,pesel=pacjent_pesel,data=pacjent_data,godzina=pacjent_godzina)
        
        #tutaj dodanie do bazy danych
        try:
            db.session.add(new_pacjent)
            db.session.commit()
            return redirect('/')
        except:
            return 'Wystąpił problem z dodaniem terminu!'

    else:
        termin_szczepienia = Pacjent.query.order_by(Pacjent.id).all()
        return render_template('index.html', termin_szczepienia=termin_szczepienia)


@app.route('/delete/<int:id>')
def delete(id):
    pacjent_to_delete = Pacjent.query.get_or_404(id)

    try:
        db.session.delete(pacjent_to_delete)
        db.session.commit()
        return redirect('/')
    except:
        return 'Wystąpił problem z usunięciem terminu!'



if __name__ == "__main__":
    app.run(debug=True)