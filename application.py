import flask

application = flask.Flask(__name__)

# Set application.debug = True to enable tracebacks on beanstalk log output.
# TODO: remove this before deploying to production
application.debug = True

@application.route('/')
def hello_world():
	return "Hello World!"

if __name__ == "__main__":
	application.run(host='0.0.0.0', debug=True)