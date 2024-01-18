def ieraksti_vardinu_faila():
    try:
    
        tavsvardins = input("Ieraksti savu vārdiņu:) : ")
        zuzes_fails = "pekstini.txt"

        with open(zuzes_fails, 'w', encoding='utf-8') as zuze:
            zuze.write(tavsvardins)

        print(f"Vārds '{tavsvardins}' veiksmīgi ierakstīts failā '{zuzes_fails}'.:)")
    except Exception as iunu:
        print(f"Radās kļūda: {iunu}")

ieraksti_vardinu_faila()