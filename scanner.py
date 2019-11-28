import socket
import requests

class Scanner():

    def analyze_ips(self, ip_addresses):
        domains = []
        for address in ip_addresses:
            try:
                n = socket.gethostbyaddr(address)
                domains.append(n[0])
            except Exception as e:
                print(e)
        return domains

    def get_addresses_for_class(self, address):
        for m in range(address, 173):
            for n in range(100, 102):
                for o in range(90, 92):
                    for p in range(100, 101):
                        yield '%s.%s.%s.%s' % (m, n, o, p)

    def spider_domains(self, domains):
        list_of_headers = []
        for each_domain in domains:
            domain = "http://" + each_domain.strip()
            header_string = "Headers for {}: ".format(domain)
            try:
                request = requests.get(domain)
                header_string += request.headers.as_string()
            except Exception as e:
                header_string += str(e)
            list_of_headers.append(header_string)
        return list_of_headers

    def save_to_file(self, list_of_strings, filename):
        try:
            list_file = open(filename, "w")
            for indiv_string in list_of_strings:
                list_file.write(indiv_string + "\n")
            list_file.close()
        except:
            print("Had a problem writing to the file.")