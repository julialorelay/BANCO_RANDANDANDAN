class Utils:
    @staticmethod
    def pegar_primeira_palavra(texto):
        palavras = texto.split()
        return palavras[0]