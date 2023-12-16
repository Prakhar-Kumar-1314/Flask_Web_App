from flask import Flask, render_template, request

app = Flask(__name__)


def convert_length(value, from_unit, to_unit):
    conversion_factors = {
        'Centimeter': {'Meter': 0.01, 'Inch': 0.393701},
        'Meter': {'Centimeter': 100, 'Inch': 39.3701},
        'Inch': {'Centimeter': 2.54, 'Meter': 0.0254},
    }

    if from_unit == to_unit:
        return value
    else:
        factor = conversion_factors[from_unit][to_unit]
        return value * factor


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/convert_temperature', methods=['POST'])
def convert_temperature():
    try:
        temperature = float(request.form['temperature'])
        from_unit = request.form['from_unit']

        if from_unit == 'Celsius':
            converted = {
                'celsius': temperature,
                'fahrenheit': temperature * 9 / 5 + 32,
                'kelvin': temperature + 273.15,
            }
        elif from_unit == 'Fahrenheit':
            converted = {
                'celsius': (temperature - 32) * 5 / 9,
                'fahrenheit': temperature,
                'kelvin': (temperature - 32) * 5 / 9 + 273.15,
            }
        else:
            converted = {
                'celsius': temperature - 273.15,
                'fahrenheit': (temperature - 273.15) * 9 / 5 + 32,
                'kelvin': temperature,
            }

        return render_template('index.html', converted=converted)

    except ValueError:
        error_message = 'Please enter a valid temperature.'
        return render_template('index.html', error_message=error_message)


@app.route('/convert_currency', methods=['POST'])
def convert_currency():
    try:
        amount = float(request.form['amount'])
        from_currency = request.form['from_currency']
        to_currency = request.form['to_currency']

        conversion_factors = {
            'USD': 1.0,
            'EUR': 0.85,
            'GBP': 0.73,
            'JPY': 114.39,
            'CAD': 1.26,
            'AUD': 1.35,
            'INR': 74.28,
        }

        rate = conversion_factors.get(to_currency, 1.0) / conversion_factors.get(from_currency, 1.0)
        converted_amount = amount * rate

        conversion_result = {
            'amount': amount,
            'from_currency': from_currency,
            'converted_amount': converted_amount,
            'to_currency': to_currency,
        }

        return render_template('index.html', conversion_result=conversion_result)

    except ValueError:
        error_message = 'Please enter a valid amount.'
        return render_template('index.html', error_message=error_message)

        return render_template('index.html', conversion_result=conversion_result)

    except ValueError:
        error_message = 'Please enter a valid amount.'
        return render_template('index.html', error_message=error_message)


@app.route('/convert_length', methods=['POST'])
def convert_length_route():
    try:
        value = float(request.form['value'])
        from_unit = request.form['from_unit']
        to_unit = request.form['to_unit']

        converted_value = convert_length(value, from_unit, to_unit)

        length_result = {
            'value': value,
            'from_unit': from_unit,
            'converted_value': converted_value,
            'to_unit': to_unit,
        }

        return render_template('index.html', length_result=length_result)

    except ValueError:
        error_message = 'Please enter a valid value.'
        return render_template('index.html', error_message=error_message)


if __name__ == '__main__':
    app.run(debug=True)
