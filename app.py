from flask import Flask, render_template, redirect, url_for


app = Flask('__name__')

#this is an index route
@app.route('/')
def index():
    return render_template ('public/templates/index.html')

#this is an introduction route
@app.route('/home_intro')
def home_intro():
    return render_template ('intro/templates/home_intro.html')


@app.route('/family_head')
def family_head():
    return render_template ('public/templates/family_head.html')

@app.route('/children')
def children():
    return render_template ('public/templates/children.html')

#this is an over
@app.route('/grand_children')
def grand_children():
    return render_template ('public/templates/grand_children.html')









if __name__ == '__main__':
    app.run(debug=True)
