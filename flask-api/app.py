import os
from flask import Flask, jsonify
import requests
import bs4
from flask import Flask

noticia_ruin = [
    'morte',
    'assassinato',
    'lavagem de dinheiro',
    'estupro',
    'pedofilia',
    'corrupto',
    'roubo'
]
limit = 5
app = Flask(__name__)

nome_delinquente = ('osama') 
               
@app.route('/', methods=['GET'])
def crawler():
    res = requests.get("https://g1.globo.com/busca/?q=" + nome_delinquente)
    res.text
    soup = bs4.BeautifulSoup(res.text, 'lxml')
    for link in soup.find_all('a', href=True, stop=3):
        print(link['href'])
    return jsonify(link['href'])
        
if __name__ == '__main__':
    app.run(debug=True)







        

