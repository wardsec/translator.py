from translate import Translator

# Configurando tradução
s = Translator(from_lang="english", to_lang="pt-br")

#Traduzindo texto
res = s.translate(input("Digite o texto a ser traduzido: "))
#Imprimindo texto
print(res)