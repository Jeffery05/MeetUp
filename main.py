from website import app
from website import db

if __name__ == '__main__':
    app.run(debug=True) #re-run whenever we make a change in python

@app.before_first_request
def create_tables():
    db.create_all()