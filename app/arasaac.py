from eve import Eve
import os

SETTINGS_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'settings.py')

app = Eve(settings=SETTINGS_PATH)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
