from urllib import request


def download_file(csv_url):
    response = request.urlopen(csv_url)
    csv = response.read()
    csv_str = str(csv)
    lines = csv_str.split("\\n")
    dest_url = r'google.csv'
    fx = open(dest_url, 'w')
    for line in lines:
        fx.write(line + "\\n")
    fx.close()


if __name__ == '__main__':
    url = 'http://samplecsvs.s3.amazonaws.com/SacramentocrimeJanuary2006.csv'
    download_file(url)
