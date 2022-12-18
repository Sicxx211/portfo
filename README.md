# A simple web application made with Python and Flask.


# Why I made this web application 

I believe that making a website is the best way to show off your skills and portfolio. I made it to make my work easier in seeking new jobs or meeting people that are interested in the same fields as I am. <br> 
<br>
I made this simple web application using Python and Flask for the back-end part of it, and of course HTML,CSS and JS for the front-end part.
<br>
I took the time and added a personal note to the web application by making the images by myself.
<br>
This is only the start of the journey.



# How I wrote the code :


import csv  <br>
from flask import Flask , render_template, url_for, request, redirect <br>
app = Flask(_name_) <br>

@app.route('/') <br>
def my_home(): <br>
 return render_template('index.html') <br>
<br>
#We used this to not repeat code and make this more dinamically, instead of copy and pasting the app.route code for each page we can use this syntax instead
<br>
@app.route('/') <br>
def html_page(page_name): <br>
 return render_template(page_name) <br>
<br>
#This functions basically appends the data from the form that someone submits into the database.txt file, again this works because they are in the same directory eitherwise we should've specify the full path <br>
<br>
def write_to_file(data): <br>
 with open('database.txt', mode='a') as database: <br>
  email = data['email'] <br>
  subject = data['subject'] <br>
  message = data['message'] <br>
  file = database.write(f'\n1:{email}\n2:{subject}\n3:{message}') <br>
<br>
#This functions basically appends the data from the form to a csv file, to use csv files we will need to first import it's module, then we can use the next lines to write what's in the form into a csv file <br> 
<br>
def write_to_csv(data): <br>
 with open('database.csv', mode='a') as database2: <br>
  email = data['email'] <br>
  subject = data['subject'] <br>
  message = data['message'] <br>
  csv_writer = csv.writer(database2, delimiter=',', quotechar='*', quoting=csv.QUOTE_MINIMAL) <br>
  csv_writer.writerow([email,subject,message]) #This is enough for csv writer because it knows that these are the things that we want <br>
 <br>
@app.route('/submit_form', methods=['POST', 'GET']) <br>
def submit_form(): <br>
 if request.method == 'POST': <br>
  try: <br> 
   data = request.form.to_dict() #This basically turn the form data into a dictionary <br>
   write_to_csv(data) <br>
   return redirect('/thankyou.html') #Basically this will redirect you after you submit a form to the page thankyou.html <br>
  except: <br>
   return 'Did not save to database' <br>
 else: <br>
  return 'something went wrong.Try again!' <br>
