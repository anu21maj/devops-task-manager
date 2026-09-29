from flask import Flask, render_template #Import the Flask class from the Flask package.

app = Flask(__name__) #creares our Flask application object, which is an instance of the Flask class. The __name__ variable is a special Python variable that represents the name of the current module. It is used to determine the root path of the application.

@app.route('/') #The @app.route() decorator is used to define a route for the application. In this case, it defines the root route ("/") of the application.
def home(): 
    #return "DevOps Task Manager is running!" #This function is called when a user visits the root route. It returns a simple string message indicating that the application is running.
    return render_template("index.html") #This function is called when a user visits the root route. It returns a simple string message indicating that the application is running.

@app.route('/health') #This route is used to check the health of the application. It returns a JSON response indicating that the application is healthy.
def health(): 
    return {"status" : "healthy"} #This function is called when a user visits the "/health" route. It returns a JSON response with a "status" key and a value of "healthy".

if __name__ == '__main__': #This line checks if the script is being run directly (as opposed to being imported as a module). If it is, the application will be started.
    app.run(host = "0.0.0.0" ,port = 5000) #This line starts the Flask development server, which listens for incoming requests on all available network interfaces (host = "
    
