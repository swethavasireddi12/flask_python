from Employee import app
import os

#Checks if the run.py file has executed directly and not imported
# docker run -p 5001:5000 -e DEBUG=1 flask_app_dev
if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000,debug=os.environ.get('DEBUG')=='1')