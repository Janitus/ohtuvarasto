from varasto import Varasto

def main():
    mehua = Varasto(100.0)
    olutta = Varasto(100.0, 20.2)

    print("Luonnin jälkeen:")
    print(f"Mehuvarasto: {mehua}")
    print(f"Olutvarasto: {olutta}")

    olut_getterit(olutta)
    mehu_setterit(mehua)
    virhe_tilanteita()

    lisaa_varastoon(olutta, 1000.0, "Olutvarasto")
    lisaa_varastoon(mehua, -666.0, "Mehuvarasto")

    ota_varastosta(olutta, 1000.0, "Olutvarasto")
    ota_varastosta(mehua, -32.9, "Mehuvarasto")

def lisaa_varastoon(varasto: Varasto, maara, nimi):
    print(f"{nimi} ennen lisäystä: {varasto}")
    print(f"{nimi}.lisaa_varastoon({maara})")
    varasto.lisaa_varastoon(maara)
    print(f"{nimi} lisäyksen jälkeen: {varasto}")

def ota_varastosta(varasto: Varasto, maara, nimi):
    print(f"{nimi} ennen ottamista: {varasto}")
    print(f"{nimi}.ota_varastosta({maara})")
    saatiin = varasto.ota_varastosta(maara)
    print(f"Saatiin {saatiin} yksikköä varastosta")
    print(f"{nimi} ottamisen jälkeen: {varasto}")

def olut_getterit(varasto: Varasto):
    print("Olut getterit:")
    print(f"saldo = {varasto.saldo}")
    print(f"tilavuus = {varasto.tilavuus}")
    print(f"paljonko_mahtuu = {varasto.paljonko_mahtuu()}")

def mehu_setterit(varasto: Varasto):
    print("Mehu setterit:")
    print("Lisätään 50.7")
    varasto.lisaa_varastoon(50.7)
    print(f"Mehuvarasto: {varasto}")
    print("Otetaan 3.14")
    varasto.ota_varastosta(3.14)
    print(f"Mehuvarasto: {varasto}")

def virhe_tilanteita():
    print("Virhetilanteita:")
    print("Varasto(-100.0);")
    huono = Varasto(-100.0)
    print(huono)

    print("Varasto(100.0, -50.7)")
    huono = Varasto(100.0, -50.7)
    print(huono)

if __name__ == "__main__":
    main()
