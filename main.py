import json


class Country:
    def __init__(self):
        self.dictionary = {"Slovensko":"Bratislava","Cesko":"Praha"}
    def finding_data(self,country):
        return self.dictionary.get(country)
    def adding_data(self,country,mesto):
        self.dictionary[country] = mesto
    def delete_data(self,country):
        return self.dictionary.pop(country)
    def editing_data(self, country, mesto):
        if country in self.dictionary:
            self.dictionary[country] = mesto
        else:
            print("Krajina nenajdena, nieje mozne editovat")

    @staticmethod
    def to_json(data):
        return json.dumps(data)

    def packing(self, nazov):
        with open(nazov, "w") as file:
            file.write(json.dumps(self.dictionary))
        return nazov

    def unpacking(self, nazov):
        with open(nazov, "r") as file:
            loaded_file = json.load(file)
            self.dictionary = loaded_file
            return self

country = Country()

print(country.finding_data("Slovensko"))
country.adding_data("France", "Paris")
print(country.dictionary)
country.delete_data("Cesko")
print(country.dictionary)
country.editing_data("Slovensko", "Kosice")
print(country.dictionary)

print(Country.to_json(country.dictionary))
country.packing("country_data.json")
country.unpacking("country_data.json")
print(country.dictionary)

