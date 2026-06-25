from flask import Flask, render_template
app = Flask(__name__)

JOBS = [
    {
        'id': 1,
        'title': 'Data Analyst',
        'location': 'New York, NY',
        'salary': '$70,000 - $90,000'
    },
    {
        'id': 2,
        'title': 'Software Engineer',
        'location': 'San Francisco, CA',
        'salary': '$100,000 - $130,000'
    },
    {
        'id': 3,
        'title': 'Product Manager',
        'location': 'Austin, TX',
        'salary': '$90,000 - $120,000'
    }
]

@app.route('/')
def hello_world():
    return render_template('main.html', jobs=JOBS, company_name="BuddyWorks")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)






























