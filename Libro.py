class Libro:
    codigo = ''
    titulo = ''
    autor = ''
    precio = 0
    pais = ''
    categoria = ''
    fpub = ''

    #valores minimo
    def __int__(self):
        self.codigo = 'AAC-123'
        self.titulo = 'S/T'
        self.autor = 'S/A'
        self.precio = 10000
        self.pais = 'S/P'
        self.categoria = 'S/C'
        self.fpub = '1780' #entre 1780 y 2023

    #reglas de negocio

    def setprecio(self, precio):
        if precio >= 10000 and precio <= 150000:
            self.precio = precio
            return True
        else:
            precio("El precio del libro debe estar entre 10000 y 150000")
            return False

    def setcodigo(self, codigo):
        if codigo[0:3].isalpha() and codigo[3:4] == '-' and codigo[4:7].isdigit():
            self.codigo = codigo
            return True
        else:
            print("El formato del codigo debe ser: AAA-000")
            return False

    def setfpub(self, fpub):
        if fpub >= 1780 and fpub <= 2023:
            self.fpub = fpub
            return True
        else:
            print("El año de publicacion debe estar en 1780 y 2023")
            return False
