from flask import Flask, request, render_template
from GOOGLE_API import g_api_call
from OWN_API import own_api_call


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def func():
    weather = own_api_call(g_api_call('toronto'))

    if request.method == 'POST':

        city = request.form['city']
        weather = own_api_call(g_api_call(city))


    return render_template("weather_temp.html", weather=weather)



if __name__ == "__main__":
    app.run(debug=True)