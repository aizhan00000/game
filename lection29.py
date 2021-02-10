import requests
from bs4 import BeautifulSoup


class ParseData:
    def __init__(self):
        self.url = 'https://www.computermarket.ru/main/catalog/catid/105197.aspx'
        self.session = requests.Session()

    def get_request(self):
        response = self.session.get(self.url)
        page = response.text
        return page

    def write_site_data_to_file(self):
        file = open('page.txt', 'w')
        file.write(self.get_request())
        file.close()
        file = open('page.txt', 'r')
        file_data = file.read()
        file.close()
        return file_data

    def parse_data(self):
        file = self.write_site_data_to_file()
        soup = BeautifulSoup(file, 'html.parser')

        cpu_title_list = []
        for i in soup.find_all("a", {"class": "title-ineer-cont"}):
            cpu_title_list.append(str(i.get_text()).strip())

        counter = 0
        for i in range(len(cpu_title_list)):
            if i % 2 == 0:
                item = cpu_title_list[counter]
                cpu_title_list.remove(item)
                counter += 1

        cpu_price_list = []
        for i in soup.find_all("div", {"class": "price-c"}):
            cpu_price_list.append(str(i.get_text()).strip())

        finally_list = []
        for i in range(len(cpu_title_list)):
            finally_list.append([cpu_title_list[i], cpu_price_list[i]])

        for i in finally_list:
            print(i)


def main():
    parse = ParseData()

    def run():
        user_choice = int(input(
            "1) Send request and create file with data\n"
            "2) Get data\n"
            "3) Close program\n"
            "Make choice: "
        ))
        if user_choice == 1:
            parse.get_request()
            parse.write_site_data_to_file()
            return run()
        elif user_choice == 2:
            parse.parse_data()
            return run()
        else:
            return True
    run()

main()