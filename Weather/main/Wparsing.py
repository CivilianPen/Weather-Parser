'''import requests
from bs4 import BeautifulSoup as BS

def Weather(city):
    Week_Weather = ()
    prognoz = 'dDb8'
    r2 = requests.get('https://weather.rambler.ru/' + city + '/')
    html2 = BS(r2.text, 'html.parser')
    t2 = html2.find("div", class_=prognoz).find_all('span')
    db = []
    for result in t2:
        db.append(result.text)
    db[0] = 'Дата'
    db = ['День недели'] + db
    dels = [[] for i in range(len(db[5:]) // 6)]
    for i in range(1, len(dels)):
        for j in range(0, 6):
            dels[i].append(db[i * 6 + j - 1])
    dels[0] = [db[:5]]
    for i in range(1, len(dels)):
        value = dict()
        for key in db[:5]:
            value[key] = ''
        value['День недели'] = dels[i][0]
        value['Дата'] = dels[i][1]
        value['Температура'] = dict({'Днем': dels[i][2], 'Ночью': dels[i][3]})
        value['Осадки'] = dels[i][4]
        value['Ветер'] = dels[i][5]
        Week_Weather += (value,)

    ###############################################################

    cities_RU = []
    url = 'https://weather.rambler.ru/' + city + '/now/'
    url2 = 'https://weather.rambler.ru/' + city + '/'
    r = requests.get(url)
    html = BS(r.text, 'html.parser')
    classes = ['_2RLq', 'O6uR', 'HhSR GyfK', 'hjtR pressure HbwD aT_0', 'hjtR wind HbwD aT_0','hjtR precipitationProbability HbwD aT_0', 'UAaG']
    V_citi = html.find(class_='RkHg')
    cities_RU.append(V_citi.text[:V_citi.text.rfind(' ')])

    value = [V_citi.text]
    for j in range(len(classes)):
        t = html.find(class_=classes[j])
        if j == 0:
            pass
            #s = t.text
            #tire = s.find('—')
            #value.append(s[:tire])
        elif j == 1:
            value.append(t.text)
        elif j == 2:
            value.append(t.text)
        elif j == len(classes) - 1:
            os = t.text
            comma = os.find(',')
            value.append(os[comma + 2:])
        else:
            if classes[j] != 'hjtR precipitationProbability HbwD aT_0':
                so = t.text
                space = so.find(' ')
                value.append(so[space:])
            else:
                try:
                    so = t.text
                    space = so.rfind(' ')
                    value.append(so[space:])
                except:
                    value.append('0%')
    Today_Weather = {
        'inf': value[0],
        'date': value[1],
        'temp': value[2],
        'press': value[3],
        'wind': value[4],
        'prob': value[5],
        'falls': value[6],
    }
    return Week_Weather, Today_Weather'''