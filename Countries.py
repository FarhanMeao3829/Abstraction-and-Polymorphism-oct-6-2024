class India:
    def capital(self):
        print("New Delhi is the capital of India.")
        
    def language(self):
        print("Hindi is the most widely spoken language of India")
        
    def type(self):
        print("India is a developing country")
        
class Bangladesh:
    def capital(self):
        print("Dhaka is the capital of Bangladesh")
        
    def language(self):
        print("Bengali is the primary language of Bangladesh")
        
    def type(self):
        print("Bangladesh is a developing country")
        
objInd = India()
objBd = Bangladesh()

for country in (objInd, objBd):
    country.capital()
    country.language()
    country.type()

    