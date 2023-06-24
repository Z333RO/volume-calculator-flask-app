from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home_get():
    print("GET request string")
    return render_template('index.html') #flask is designed to look into /templates folder automatically. No need to specify the path ie templates/index.html - self note, this app will receive GET requests. No need for me to specify.

@app.route('/', methods = ['POST']) # adding the ability for the app to receive POST requests
def home_post():
    # print(request.form)
    dim1 = request.form['first_dim']
    dim2 = request.form['second_dim']
    dim3 = request.form['third_dim']
    volume = float(dim1) * float(dim2) * float(dim3) 
    print(volume)

    print("POST request string")
    return render_template('index.html', output=volume, dim_1=dim1, dim_2=dim2, dim_3=dim3)

# app.run(host='127.0.0.1', port='3000')
app.run(host='0.0.0.0', port='3000')