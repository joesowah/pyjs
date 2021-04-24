import datetime as dt
# import pandas as pd
import flask
from flask import request

# data = pd.read_csv('data/monarchs.csv', names=['startyear', 'endyear', 'monarch']).set_index('monarch')

# create a panda series starting from first year from dataset to current year
# series = pd.Series(index=range(data.startyear.min(), dt.now().year))

# for m in data.index:
#    series.loc[data.loc[m].startyear:data.loc[m].endyear] = m

app = flask.Flask(__name__)


@app.route('/', methods=['GET'])
def whoreigned():
    # return "<h1>Dummy Chieftain Orm</h1>"
    try:
        year = int(request.args['year'])
        print(f'Year entered is : {year}')
        return getmonarch(year)  # series.loc[year]
    except ValueError:
        return f'Invalid year input - range should be 802 - 925'


def getmonarch(year):
    chieftain = 'None'
    if year == 802:
        chieftain = 'HRH Egbert'
    elif year == 839:
        chieftain = 'HRH Aethelwulf'
    elif year == 856:
        chieftain = 'HRH Aethelbald'
    elif year == 860:
        chieftain = 'HRH Aethelbert'
    elif year == 866:
        chieftain = 'HRH Aethelred I'
    elif year == 871:
        chieftain = 'HRHX Alfred the Great'
    elif year == 899:
        chieftain = 'HRH Edward the Elder'
    elif year == 925:
        chieftain = 'HRH Athelstan'
    else:
        chieftain = 'None Available'

    return chieftain



@app.route('/test', methods=['GET'])
def test():
    return "<h1>Dummy Chieftain Orm</h1>"
    
    
if __name__ == '__main__':
    app.run(host='0.0.0.0')


    
