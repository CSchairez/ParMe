from flask import Flask, render_template, url_for, request, redirect
from flask_restful import Api, Resource
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
db = SQLAlchemy(app)




class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    golfer_name = db.Column(db.String(25), nullable=False)
    course_name = db.Column(db.String(50), nullable=False)
    round_score = db.Column(db.String(3), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    #-- Will need to create new DB model for comments, this is incorrect  --#
    round_comments = db.Column(db.String(45), nullable=True)
    

    def __repr__(self):
        return '<Round %r>' % self.id



class Round(Resource):
    def post(self):

        #-- Hardcoding round data for testing --#
        golfer_name = "Mike"
        course = "SJ Muni"
        score = 92
        new_golfer = Todo(golfer_name=golfer_name, course_name=course, round_score=score)

        round = {"golfer_name":golfer_name, "course": course, "score": str(score)}
        try:
            #-- Add golfer to the db. --#
            db.session.add(new_golfer)
            db.session.commit()
        except:
            return 'There was an issue adding your round.'

        rounds = Todo.query.order_by(Todo.date_created).all()
        return {"Rounds": round}

api.add_resource(Round, "/")

"""

@app.route('/', methods=['POST','GET'])
def index():


    if request.method == 'POST':
        #-- Get content from ids --#
        golfer_name = request.form['name']
        course = request.form['course']
        score = request.form['score']
        #-- Create new golfer and their round info to db model instance. --#
        new_golfer = Todo(golfer_name=golfer_name, course_name=course, round_score=score)

        try:
            #-- Add golfer to the db. --#
            db.session.add(new_golfer)
            db.session.commit()
            return redirect('/')
        except:
            return 'There was an issue adding your round.'

    else:
        rounds = Todo.query.order_by(Todo.date_created).all()
        return render_template('index.html', rounds=rounds)


@app.route('/delete/<int:id>')
def delete(id):
    round_to_delete = Todo.query.get_or_404(id)
    try:
        db.session.delete(round_to_delete)
        db.session.commit()
        return redirect('/')
    except:
        return 'There was a problem deleting that round.'


#-- Under Construction, will most likely get rid of this. --#
@app.route('/comment/<int:id>')
def comment(id):
    round_to_comment = Todo.query.get_or_404(id)


"""
if __name__ == "__main__":
    app.run(debug=True)
    
