import requests
from flask import Flask

app = Flask(__name__)

def get_newborn_names(url):
    result = requests.get(url)
    return result.json()

@app.route("/")
def index():
    return "Hi!"


@app.route("/names")
def newborn_names():
    names_list = get_newborn_names('http://api.data.mos.ru/v1/datasets/2009/rows')
    output_table = '<table><tr>'
    for key in names_list[0]['Cells'].keys():
        output_table += '<th>   {}    </th>'.format(key)
    output_table += '</tr>'
    for num in names_list:
        #newborn_name = num['Cells']['Name']
        #newborn_year = num['Cells']['Year']
        #newborn_month = num['Cells']['Month']
        #newborn_count = num['Cells']['NumberOfPersons']
        #print('Имя: {}, Год: {}, Месяц: {}, Кол-во новорожденных: {}'.format(newborn_name, newborn_year, newborn_month, newborn_count))
        name_dict = num['Cells']
        value_html = ''
        for value in name_dict.values():
            value_html += '<td>{}   </td>'.format(value)
            #print('{}: {}'.format(key, value))
        output_table += '<tr><center>   {}  </center></tr>'.format(value_html)
    output_table += '</table>'
    return output_table








   # for num in names_list:
        #newborn_name = num['Cells']['Name']
        #newborn_year = num['Cells']['Year']
        #newborn_month = num['Cells']['Month']
        #newborn_count = num['Cells']['NumberOfPersons']
        #print('Имя: {}, Год: {}, Месяц: {}, Кол-во новорожденных: {}'.format(newborn_name, newborn_year, newborn_month, newborn_count))
    #    for key, value in num[]        

    #return names_list





if __name__ == "__main__":
    #get_newborn_names('http://api.data.mos.ru/v1/datasets/2009/rows')
    app.run()

    
