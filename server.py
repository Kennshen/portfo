from flask import Flask, render_template, request, redirect
import csv

# setting the Flask app as the main function to be running
app = Flask(__name__)


@app.route('/')
def home_page():
    return render_template('index.html')


# do not need to call function for all the different htmls
@app.route('/<string:page_name>')
def call_page(page_name):
    return render_template(page_name)


def write_to_file(data):
    with open('data.txt', mode='a') as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        file = database.write(f'\n{email},{subject},{message}')


def write_to_csv(data):
    with open('database.csv', newline='', mode='a') as database2:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(database2, delimiter=',',
                                quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])

# function to receive information from website


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    try:
        if request.method == "POST":
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('/thankyou.html')
    except:
        return 'did not save to database'
    else:
        return "something went wrong"
