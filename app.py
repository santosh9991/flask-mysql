from flask import Flask,request
from models import CPUModel as c, LocationModel as l
from models import db_session
app = Flask(__name__)
app.debug = True
@app.route('/cpu')
def cpus_list():

    a =   c.query.all()
    print("cpu list: ", a)
    print('a.location',a[1].locs.city)
    # for i in a[1]:
    #     print(i)
    return "cpu"
@app.route('/loc')
def loc_list():

    a =   l.query.all()
    print("cpu list: ", a)

    # for i in a[1]:
    #     print(i)
    return "cpu"
@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8000)
