class Botswana:
    def capital(self):
        return "The capital of Botswana is Gaborone."

    def language(self):
        return "The official language of Botswana is English."

    def type_of_country(self):
        return "Botswana is a landlocked country."

class Japan:
    def capital(self):
        return "The capital of Japan is Tokyo."

    def language(self):
        return "The official language of Japan is Japanese."

    def type_of_country(self):
        return "Japan is an island nation."

def display_country_info(country):
    print(country.capital())
    print(country.language())
    print(country.type_of_country())

botswana = Botswana()
japan = Japan()

display_country_info(botswana)
display_country_info(japan)