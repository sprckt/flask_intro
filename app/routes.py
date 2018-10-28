from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():

    user = {'username': 'et'}

    posts = [
        {
            'author': {'username': 'J-Dub'},
            'body': 'Great sunday spent programming',
            'tags': ['coding', 'flask']
        },
        {
            'author': {'username': 'X-box'}, 
            'body': 'Is car sickness genetically inherited',
            'tags': ['life', 'worries']
        }
    ]
    
    return render_template('index.html', 
                            title='Flask Mega', 
                            user=user, 
                            posts=posts)
