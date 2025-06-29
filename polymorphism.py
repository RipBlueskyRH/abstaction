class China():
    def capital(self):
        print("The capital of China is Beijing.")
    def language(self):
        print("The main languages of China are Mandarin and Cantenese.")


class Kuwait():
    def capital(self):
        print("The capital of Kuwait is Kuwait City.")
    def language(self):
        print("The main language of Kuwait is Arabic.")

obj1=China()
obj2=Kuwait()

for country in (obj1,obj2):
    country.capital()
    country.language()