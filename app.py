from modelos.restaurante import Restaurante

restaurante1 = Restaurante("Outback Steakhouse", "Carnes")
restaurante2 = Restaurante("Taverna Medieval", "Hamburgueria")

restaurante1.receber_avaliacao("Felipe", 4.5)
restaurante1.receber_avaliacao("Erika", 4.7)
restaurante1.receber_avaliacao("Priscila", 5)

def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()
