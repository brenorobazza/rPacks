from Correios.CorreiosAPI import CorreiosAPI as correios

print(correios.getData("Avenida Paulista, São Paulo")["dados"][0]["cep"])