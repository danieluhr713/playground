from flask import Flask, render_template  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return render_template('index.html')  # Return the string 'Hello World!' as a response

@app.route('/play')
def blue_box():
    return render_template('index.html', times = 3, color="lightblue")

@app.route('/play/<int:times>')
def first(times):
    return render_template('index.html', times=times, color="lightblue")

@app.route('/play/<int:times>/<string:color>')
def second(times, color):
    return render_template('index.html', times=times, color=color)

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.