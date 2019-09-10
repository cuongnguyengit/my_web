from flask import Flask, render_template, template_rendered
import datetime

app = Flask(__name__)


@app.template_filter()
def datetimefilter(value, format='%Y/%m/%d %H:%M'):
    """convert a datetime to a different format."""
    return value.strftime(format)


app.jinja_env.filters['datetimefilter'] = datetimefilter


@app.route('/')
def get():
    """
    :return:
    """
    # return render_template('base.html', content='Đây là app')
    return render_template('test.html', current_time=datetime.datetime.now())


@app.route('/lol', methods=['GET'])
def get_lol():
    """
    :return:
    """
    # return render_template('base.html', content='Đây là app')
    return render_template('content_lol.html', current_time=datetime.datetime.now())


@app.route('/view_table_lol', methods=['POST'])
def get_view_table_lol():
    """
    :return:
    """
    # return render_template('base.html', content='Đây là app')
    return ''


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8088, debug=True)
