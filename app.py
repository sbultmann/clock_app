from flask import Flask, render_template, redirect
from forms import ColorForm
import os
import serial
import time

from text_render import render_text_columns

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(16)


@app.route('/', methods=['GET', 'POST'])
def hello():
    form = ColorForm()
    if form.validate_on_submit():
        HEADER = "X" if len(form.msg.data) < 1 else 'M'
        R = str(form.R.data)
        G = str(form.G.data)
        B = str(form.B.data)
        RGB = HEADER + R + "." + G + "." + B

        if len(form.msg.data) > 0:
            le_columns = render_text_columns(str(form.msg.data))
            RGB += ',' + ','.join(map(str, le_columns));

        ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)
        RGB=bytes(RGB, encoding='utf-8')
        time.sleep(5)
        ser.write(RGB)
        return redirect('/')
    return render_template('submitColor.html', title='Sign In', form=form)
if __name__ == "__main__":
	app.run(host= '0.0.0.0')