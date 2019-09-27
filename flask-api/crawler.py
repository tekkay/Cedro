from pyquery import PyQuery

seeds = [
    'https://g1.globo.com/busca/?q=osama'
   
]

noticia_ruin = [
    'morte',
    'assassinato',
    'lavagem de dinheiro',
    'estupro',
    'pedofilia',
    'corrupto',
    'roubo'
]

crawl_frontiers = []

def start_crawler():
    crawl_frontiers = crawler_seeds()

    print(crawl_frontiers)

def crawler_seeds():
    frontiers = []
    for index, seed in enumerate(seeds):
        frontier = {index: read_links(seed)}
        frontiers.append(frontier)

    return frontiers

def read_links(seed):
    crawler = PyQuery(seed)
    rule = define_rule(seed)

    links = []

    tags_a = crawler('a').filter(lambda i: PyQuery(this).attr('href') and rule(PyQuery(this).attr('href')))
    links = [crawler(tag_a).attr('href') for tag_a in tags_a]

    return links

def define_rule(seed):
    if 'g1' in seed:
        return google_rule

def google_rule(link):
    return noticia_ruin in link

def cade_rule(link):
    return noticia_ruin in link

def bing_rule(link):
    return noticia_ruin in link

start_crawler()