
import requests
    

def get_newborn_names(url):
    result = requests.get(url)
    result = result.json()
    output_table = '<table><tr>'
    for key in result[0]['Cells'].keys():
        output_table += '<th>{}</th>'.format(key)
    output_table += '</tr><tr>'
    for num in result:
        #newborn_name = num['Cells']['Name']
        #newborn_year = num['Cells']['Year']
        #newborn_month = num['Cells']['Month']
        #newborn_count = num['Cells']['NumberOfPersons']
        #print('Имя: {}, Год: {}, Месяц: {}, Кол-во новорожденных: {}'.format(newborn_name, newborn_year, newborn_month, newborn_count))
        name_dict = num['Cells']
        for value in name_dict.values():
            output_table += '<td>{}</td>'.format(value)

            #print('{}: {}'.format(key, value))
    output_table += '</tr></table>'
    print(output_table)
            

if __name__ == "__main__":
    get_newborn_names('http://api.data.mos.ru/v1/datasets/2009/rows')

    
