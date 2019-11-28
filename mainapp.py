# Steps through a range of IP addresses, performs a
# reverse DNS lookup on the address, and sends an HTTP header
# request to the website and logs return headers to a file for
# later analysis.

# Resources used:
#
# 1. Code from professor on March 1, 2019
# 2. https://www.tutorialspoint.com/python/python_http_headers.htm
# 3. https://stackoverflow.com/questions/2792650/import-error-no-module-name-urllib2
# 4. https://stackoverflow.com/questions/5823572/valueerror-unknown-url-type-in-urllib2-though-the-url-is-fine-if-opened-in-a-b
# 5. https://www.blog.pythonlibrary.org/2016/06/28/python-101-an-intro-to-urllib/
# 6. https://stackoverflow.com/questions/7832264/difficulty-using-pythons-socket-gethostbyaddr


from scanner import Scanner
import time



def main():
    scanner = Scanner()
    ip_addresses = scanner.get_addresses_for_class(172)
    domains = scanner.analyze_ips(ip_addresses)
    returned_headers = scanner.spider_domains(domains)
    scanner.save_to_file(returned_headers, "headers.txt")


if __name__ == "__main__":
    main()