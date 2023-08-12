import requests


sentences = [
    "Durante la Revolución Industrial en el siglo XIX, la fábrica textil de Manchester, conocida por su producción de algodón, se convirtió en un símbolo de la transformación económica y social de la época.",
    "Jane Goodall es una renombrada primatóloga que dedicó su vida al estudio de los chimpancés en su hábitat natural, lo que contribuyó enormemente a nuestra comprensión de la vida animal y la conservación.",
    "En el siglo XX, la obra maestra literaria 'Cien años de soledad', escrita por Gabriel García Márquez, capturó la imaginación de lectores de todo el mundo con su estilo único y su narrativa mágica.",
    "La Gran Muralla China, una estructura defensiva construida a lo largo de siglos para proteger las fronteras del imperio chino, es uno de los logros arquitectónicos más impresionantes y una atracción turística icónica en la actualidad."
]

data = {'sentences': sentences}
response = requests.post('http://127.0.0.1:5000/api/ner', json=data)
print(response.json())