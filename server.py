from flask import Flask, render_template
from random import randint
from datetime import datetime
import requests

new_server = Flask(__name__)


@new_server.route('/')
def home():
    random_num = randint(1, 10)
    return render_template('index.html', num=random_num, curr_date=datetime.now().year)


@new_server.route('/guess/<name>')
def guess(name):
    r1 = requests.get(url=f'https://api.genderize.io/?name={name}')
    r2 = requests.get(url=f'https://api.agify.io?name={name}')
    r3 = requests.get(url=f'https://api.nationalize.io?name={name}')
    r1.raise_for_status()
    r2.raise_for_status()
    r3.raise_for_status()
    return render_template('sample.html', the_name=name,
                           gender=r1.json()['gender'],
                           age=r2.json()['age'],
                           nation=r3.json()['country'][0]['country_id'])


@new_server.route('/blog/cosmos/')
def cosmos():
    r = requests.get('https://api.npoint.io/2490efd005505d66c3d1')
    r.raise_for_status()
    return render_template('blog.html', posts=r.json())


@new_server.route('/blogs')
def blog():
    r = requests.get('https://api.npoint.io/2490efd005505d66c3d1')
    r.raise_for_status()
    year = datetime.now().year
    return render_template('blog_index.html', date=year, data=r.json())


@new_server.route('/blogs/<int:value>')
def blog_post(value):
    r = requests.get('https://api.npoint.io/2490efd005505d66c3d1')
    r.raise_for_status()
    year = datetime.now().year
    return render_template('blog_post.html', curr_date=year, data=r.json(),val=value)


if __name__ == "__main__":
    new_server.run(debug=True)
