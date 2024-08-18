import request

target_url = input('[*] Enter target URL: ')
file_name = input('[*] Enter The Name Of The File Containing Directoaries: ')

#In this Function we check we get the '200OK' response of our request or not.
def req(url):

    try:
        return request.get("http://" + url) #In this line of code use "GET method" of HTML to get the result of the request of website.

    except request.exceptions.ConnectionError:
        pass


file = open(file_name, 'r')
for line in file:

    directory = line.strip()
    full_url = target_url + '/' + directory
    response = req(full_url)

    if response:
        print('[*] Discoverd Directory At This Path: ' + full_url)