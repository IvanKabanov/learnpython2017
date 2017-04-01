import requests
from flask import Flask, abort, request

app = Flask(__name__)

def get_newborn_names(url):
    result = requests.get(url)
    return result.json()

@app.route("/")
def index():
    return "Hi!"


@app.route("/names")
def newborn_names():
    years = [2015, 2016, 2017]
    try:
        newborn_year = int(request.args.get('year')) if int(request.args.get('year')) in years else 'all'
    except:
        newborn_year = 'all'
    names_list = get_newborn_names('http://api.data.mos.ru/v1/datasets/2009/rows')
    output_table = '<table><tr>'
    for key in names_list[0]['Cells']:
        output_table += '<th><h3>{}</h3></th>'.format(key)
    output_table += '</tr>'
    for num in names_list:
        name_dict = num['Cells']
        value_html = ''
        if name_dict['Year'] == newborn_year or newborn_year == 'all':
            for value in name_dict.values():
                value_html += '<td align="justify">{}</td>'.format(value)
            output_table += '<tr align="justify">{}</tr>'.format(value_html)
    output_table += '</table>'
    return output_table


if __name__ == "__main__":
    app.run()

    
