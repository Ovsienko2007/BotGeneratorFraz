import requests
from random import randint
from categories import categories

# список видов цитат
c=categories.cat()

#___________________________________________цитата__________________________________________________________
def quotes(category):
    # автовыбор категории
    if category=='любое':
        category = c[randint(0, 66)]

    # получение ключа из файла
    x = open('API_kluchi.txt', 'r')
    API_KEY = x.readline()[9:-1]

    #получение цитаты
    api_url_q = 'https://api.api-ninjas.com/v1/quotes?category={}'.format(category)
    query = requests.get(api_url_q, headers={'X-Api-Key': API_KEY})
    l=query.text[1:-2]

    n = [i for i in l.split()]
    i = n[n.index('{"quote":') + 1:n.index('"author":')]
    e = ''
    for q in i:
        e += q
        e += ' '
    e = e[1:-3]

    # получение автора
    a=''
    w = n[n.index('"author":')+1:-2]
    for q in w:
        a += q
        a += ' '
    a=a[1:-3]
    m=e+'\n'+' '*100+a

    return m

#___________________________________________анекдот__________________________________________________________

def anekdot():
    response = requests.get("http://rzhunemogu.ru/RandJSON.aspx?CType=1") # АПИ
    c=str(response.text)[12:-2] # получение анекдота
    k=''

    # превод его в приемлемый вид из-за бага в апи
    for i in c:
        if i==chr(13):
            pass
        else:
            k+=i
    return k

if __name__ == '__main__':
    print(anekdot())
    print('__________________________________________________________')
    print(quotes('любое'))
