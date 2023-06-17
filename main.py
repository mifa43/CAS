from bs4 import BeautifulSoup


html_path = '/home/mifa43/Desktop/CAS/htmlStructure/jubilej-14.html'
new_file_name = 'index.html'

def modify_HTML(source_html, new_html_name):
    mapped_html = {
        "target_tag": "div",
        "target_class": "t m0 x1 h7 y14 ff1 fs2 fc0 sc0 ls4 ws3",

    }
    with open(source_html, 'r') as file:
        fcontent = file.read()

    soup = BeautifulSoup(fcontent, 'html.parser')

    target_div = soup.find('div', class_='t m0 x1 h7 y14 ff1 fs2 fc0 sc0 ls4 ws3')
    target_div.string.replace_with('g. Milos Zlatkovic')

    with open(new_html_name, 'w') as file:
        file.write(str(soup))

modify_HTML(html_path, new_file_name)