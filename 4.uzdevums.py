def lasam_kopa():
    try:
        tava_faila_nosaukums = input("Uzraksti šeit kā sauc tavu failu: ")

        faila_paplasinajumins = input("Ievadiet faila paplašinājumu, tādu, kuru zini:) : ")

        tavs_pilnais_failins = f"{tava_faila_nosaukums}.{faila_paplasinajumins}"

        with open(tavs_pilnais_failins, 'r', encoding='utf-8') as fails:
            saturs = fails.read()
            print(f"Faila '{tavs_pilnais_failins}' saturs ir:")
            print(saturs)
    except FileNotFoundError:
        print(f"Fails ar nosaukumu '{tavs_pilnais_failins}' nav ticis atrasts. :(")
    except Exception as e:
        print(f"Radās kļūdiņa:( ): {e}")

lasam_kopa()