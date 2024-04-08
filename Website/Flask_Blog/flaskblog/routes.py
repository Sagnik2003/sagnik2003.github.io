from flask import Flask, render_template, url_for, flash, redirect
from flaskblog.forms import RegistrationForm, LoginForm
from flaskblog.models import User,Post
from flaskblog import app,db,bcrypt
posts =[
    {
        'author' : 'Sagnik Kayal',
        'title'  :  'Blog Post 1',
        'content' : """First blog postLorem ipsum dolor sit amet consectetur, adipisicing elit. Molestiae quibusdam omnis eos provident doloribus,
                    pariatur ducimus quod fuga perferendis maxime enim ut recusandae obcaecati est vel. Nam aliquam dolorum corporis.
                    Lorem ipsum dolor sit amet consectetur, adipisicing elit. Molestiae quibusdam omnis eos provident doloribus,.""",
        'date_posted': 'May 3 ,2023'
    },
    
    {
        'author' : 'Sagnik Kayal',
        'title'  :  'Blog Post 2',
        'content' : """Second blog post,Lorem ipsum dolor sit amet consectetur, adipisicing elit. Molestiae quibusdam omnis eos provident doloribus,
                    pariatur ducimus quod fuga perferendis maxime enim ut recusandae obcaecati est vel. Nam aliquam dolorum corporis.
                    Lorem ipsum dolor sit amet consectetur, adipisicing elit. Rem beatae optio quidem velit iusto mollitia deleniti,Lorem ipsum dolor sit amet consectetur, adipisicing elit. Molestiae quibusdam omnis eos provident doloribus,
        pariatur ducimus quod fuga perferendis maxime enim ut recusandae obcaecati est vel. Nam aliquam dolorum corporis..
                    """,
        'date_posted': 'Jun 6 ,2023'
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('blog.html',posts = posts)


@app.route("/blog")
def blog():
    return render_template('blog.html',posts = posts)

@app.route("/about")
def abcd():
    return render_template('index.html',title = 'About')

@app.route("/register",methods = ['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username = form.username.data , email = form.email.data,password = hashed_password)
        #db.session.add(user)
        #db.session.commit()
        flash('Your account has been created! You can now log in','success')
        return redirect(url_for('home'))   #can use the ('/home') also
    return render_template('register.html',title = 'Register',form =form)


@app.route("/login",methods = ['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)
