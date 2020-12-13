from flask import Flask,jsonify,request
from flask_uploads import UploadSet, IMAGES, configure_uploads

app = Flask(__name__)

app.config['SECRET_KEY'] = 'development'
app.config['UPLOADED_DEF_DEST'] = r'./'
app.config['UPLOADED_DEF_URL'] = r'./'
app.config["DEBUG"] = True
#Define config mode
app.config['JSON_AS_ASCII'] = False
#show 繁體中文

abc = UploadSet(name='def',extensions=IMAGES)
configure_uploads(app,abc)

#test HTML
html = '''
<!DOCTYPE html>
<html lang="en">
<h1>測試上傳</h1>
<form method=post enctype=multipart/form-data>
<input type=file name=uploadfile>
<input type=submit value=Upload>
</form>
</html>
'''

# test data
tpe = {
    "id": 0,
    "city_name": "臺北",
    "country_name": "台灣",
    "is_capital": True,
    "location": {
        "longitude": 121.569649,
        "latitude": 25.036786
    }
}
nyc = {
    "id": 1,
    "city_name": "紐約",
    "country_name": "美國",
    "is_capital": False,
    "location": {
        "longitude": -74.004364,
        "latitude": 40.710405
    }
}
ldn = {
    "id": 2,
    "city_name": "倫敦",
    "country_name": "英國",
    "is_capital": True,
    "location": {
        "longitude": -0.114089,
        "latitude": 51.507497
    }
}
cities = [tpe, nyc, ldn]

@app.route('/',methods=['GET'])
@app.route('/index')
def index():
    data = "<h1>Hello Flask api</h1>"
    return data

@app.route('/cities/all',methods=['GET'])
def cities_all():
    return jsonify(cities)

@app.route('/cities',methods=['GET'])
def city_name():
    if 'city_name' in request.args:
        city_name = request.args['city_name']
    else:
        return "Error: No city_name provided. Please specify a city_name."
    results = []

    for city in cities:
        if city['city_name'] == city_name:
            results.append(city)

    return jsonify(results)

@app.route('/uploads/',methods=['GET','POST'])
def uploads():
    if request.method == 'POST' and 'uploadfile' in request.files:
        filename = abc.save(request.files['uploadfile'])
        print(filename)
        file_url = abc.url(filename)
        print(file_url)
    return html




if __name__ == '__main__':
    app.run()
