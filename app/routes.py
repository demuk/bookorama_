from flask import render_template,redirect,url_for,request
from app import app


@app.route('/contact')
def contact():
    return render_template('contact.html')



if __name__ == '__main__': 
    app.run(debug=True) 