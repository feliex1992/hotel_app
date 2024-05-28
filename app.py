from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///hotel.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Room(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    room_number = db.Column(db.Integer, unique=True, nullable=False)
    room_type = db.Column(db.String(50), nullable=False)
    is_booked = db.Column(db.Boolean, default=False)

class Booking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_name = db.Column(db.String(100), nullable=False)
    room_id = db.Column(db.Integer, db.ForeignKey('room.id'), nullable=False)
    check_in_date = db.Column(db.Date, nullable=False)
    check_out_date = db.Column(db.Date, nullable=False)
    room = db.relationship('Room', backref=db.backref('bookings', lazy=True))

@app.route('/')
def home():
    rooms = Room.query.all()
    return render_template('home.html', rooms=rooms)

@app.route('/book', methods=['GET', 'POST'])
def book():
    if request.method == 'POST':
        room_number = int(request.form['room_number'])
        customer_name = request.form['customer_name']
        check_in_date = datetime.strptime(request.form['check_in_date'], '%Y-%m-%d').date()
        check_out_date = datetime.strptime(request.form['check_out_date'], '%Y-%m-%d').date()

        room = Room.query.filter_by(room_number=room_number).first()
        if room and not room.is_booked:
            booking = Booking(customer_name=customer_name, room=room, check_in_date=check_in_date, check_out_date=check_out_date)
            room.is_booked = True
            db.session.add(booking)
            db.session.commit()
            return redirect(url_for('home'))
        else:
            return "Room not available", 400
    rooms = Room.query.filter_by(is_booked=False).all()
    return render_template('book.html', rooms=rooms)

@app.route('/bookings')
def view_bookings():
    bookings = Booking.query.all()
    return render_template('bookings.html', bookings=bookings)

@app.route('/delete_booking/<int:booking_id>', methods=['POST'])
def delete_booking(booking_id):
    booking = Booking.query.get_or_404(booking_id)
    room = booking.room
    room.is_booked = False
    db.session.delete(booking)
    db.session.commit()
    return redirect(url_for('view_bookings'))


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
