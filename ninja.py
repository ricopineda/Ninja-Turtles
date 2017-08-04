from flask import Flask, render_template, url_for                                      

app = Flask(__name__)                     
                                          
@app.route('/')

def index():
  return render_template("index.html") 

@app.route('/ninja')

def ninja():
	source =  url_for('static', filename='img/tmnt.png') 
	return render_template("ninja.html", image_source = source) 

@app.route('/ninja/<ninja_color>')

def ninja_type(ninja_color):

	if ninja_color == "blue":
		source = url_for('static', filename='img/leonardo.jpg')
	elif ninja_color == "orange":
		source = url_for('static', filename='img/michelangelo.jpg')
	elif ninja_color == "purple":
		source = url_for('static', filename='img/raphael.jpg')
	elif ninja_color == "red":
		source = url_for('static', filename='img/raphael.jpg')
	else:
		source = url_for('static', filename='img/notapril.jpg')	



	
	
	return render_template("ninja.html", image_source = source)



app.run(debug=True)