class Cliente():
    def __init__(self, nome, idade, documento):
        self.__nome = nome
        self.__idade = idade,
        self.__documento = documento

    def get_nome(self):
        return self.__nome
    
    def get_idade(self):
        return self.__idade
    
    def get_documento(self):
        return self.__documento