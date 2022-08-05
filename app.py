from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///appointment.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# Schema for database
class Appointment(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    doctor = db.Column(db.String, nullable=False)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50),nullable=False)
    phoneno = db.Column(db.Integer, nullable=False)
    symptom = db.Column(db.String(500), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self) -> str:
        return f"{self.sno} - {self.name} "



@app.route("/", methods=["GET", "POST"])
def hello_world():
    if request.method == 'POST':
        
        doctor= request.form['doctor']
        name = request.form['name']
        email = request.form['email']
        phoneno = request.form['phoneno']
        symptom= request.form['symptom']
        appointment = Appointment(name=name, email = email, phoneno= phoneno, symptom=symptom, doctor=doctor)
        db.session.add(appointment)
        db.session.commit()
    allAppointments = Appointment.query.all()
    return render_template('index.html')

@app.route('/delete/doctor1/<int:phoneno>')
def delete(phoneno):
    appointment = Appointment.query.filter_by(phoneno=phoneno).first()
    db.session.delete(appointment)
    db.session.commit()
    return redirect("/doctor")

@app.route('/delete/doctor2/<int:phoneno>')
def delete2(phoneno):
    appointment = Appointment.query.filter_by(phoneno=phoneno).first()
    db.session.delete(appointment)
    db.session.commit()
    return redirect("/doctor2")

@app.route("/patient")
def fb3():
    return render_template('patient.html')

@app.route("/fitness-blog.html")
def fb():
    return render_template('fitness-blog.html')

@app.route("/meditation-blog.html")
def mb():
    return render_template('meditation-blog.html')

@app.route("/motivation-blog.html")
def mb1():
    return render_template('motivation-blog.html')

@app.route("/study-blog.html")
def sb():
    return render_template('study-blog.html')

@app.route("/login-doctor")
def ld():
    return render_template('login-doctor.html')

@app.route("/login-patient")
def ld1():
    return render_template('login-patient.html')

@app.route("/register-patient")
def ld2():
    return render_template('register-patient.html')

@app.route("/forgot-pass")
def fp():
    return render_template('forgot-pass.html')

@app.route("/doctor",methods=['GET', 'POST'])
def d1():
    
    allAppointments = Appointment.query.all()
    return render_template('doctor.html', allAppointments=allAppointments)
@app.route("/doctor2",methods=['GET', 'POST'])
def d2():
    
    allAppointments = Appointment.query.all()
    return render_template('doctor2.html', allAppointments=allAppointments)



if __name__ == "__main__":
    app.run(debug=True)
    