from wsgiref.simple_server import make_server


def app(environ, start_response):
    specific = {
        "Cyberman": "John Lumic",
        "Dalek": "Davros",
        "Judoon": "Shadow Proclamation Convention 15 Enforcer",
        "Human": "Leonardo da Vinci",
        "Ood": "Klineman Halpen",
        "Silence": "Tasha Lem",
        "Slitheen": "Coca-Cola salesman",
        "Sontaran": "General Staal",
        "Time Lord": "Rassilon",
        "Weeping Angel": "The Division Representative",
        "Zygon": "Broton"
    }
    species: str = get_species(environ['QUERY_STRING'])
    credentials = specific.get(species)
    status = '200 OK'
    response_body = f'{{"credentials": "{credentials}"}}'.encode()
    if not credentials:
        status = '404 not found'
        response_body = b'{"credentials": "Unknown"}'
    response_headers = [
        ('Content-Type', 'application/json'),
        ('Content-Length', str(len(response_body)))
    ]
    start_response(status, response_headers)
    return [response_body]


def get_species(s: str) -> str:
    l: list = s.split('=')
    if l.count('species') > 0:
        species = l[l.index('species') + 1]
        species = species.replace('%20', ' ')
    else:
        species = 'Unknown'
    return species


with make_server('localhost', 8888, app) as httpd:
    print("Serving on port 8888...")
    httpd.serve_forever()
