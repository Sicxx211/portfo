#Building a portfolio

import csv
from flask import Flask , render_template, url_for, request, redirect
app = Flask(__name__) 


@app.route('/')
def my_home():
	return render_template('index.html')


#We used this to not repeat code and make this more dinamically, instead of copy and pasting the app.route code for each page we can use this syntax instead 
@app.route('/<string:page_name>')
def html_page(page_name):
	return render_template(page_name)

#This functions basically appends the data from the form that someone submits into the database.txt file, again this works because they are in the same directory eitherwise we should've specify the full path 
#Mode a stands for append 
def write_to_file(data):
	with open('database.txt', mode='a') as database:
		email = data['email']
		subject = data['subject']
		message =  data['message']
		file = database.write(f'\n1:{email}\n2:{subject}\n3:{message}')



#This functions basically appends the data from the form to a csv file, to use csv files we will need to first import it's module, then we can use the next lines to write what's in the form into a csv file
def write_to_csv(data):
	with open('database.csv', mode='a') as database2:
		email = data['email']
		subject = data['subject']
		message =  data['message']
		csv_writer = csv.writer(database2, delimiter=',', quotechar='*', quoting=csv.QUOTE_MINIMAL)
		csv_writer.writerow([email,subject,message]) #This is enough for csv writer because it knows that these are the things that we want

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
	if request.method == 'POST':
		try:
			data = request.form.to_dict() #This basically turn the form data into a dictionary
			write_to_csv(data)
			return redirect('/thankyou.html') #Basically this will redirect you after you submit a form to the page thankyou.html
		except:
			return 'Did not save to database'	
	else:
		return 'something went wrong.Try again!'