def lasit_un_drukaz(teksta_fails):
    try:
        with open(teksta_fails, 'r', encoding='utf-8') as fails:
            saturs = fails.read()
            print("Faila saturs:")
            print(saturs)
    except FileNotFoundError:
        print(f"Fails ar nosaukumu '{teksta_fails}' netika atrasts.")
    except Exception as e:
        print(f"Radās kļūda: {e}")

# Mainīgais ar faila nosaukumu, piemēram, 'mans_fails.txt'
mans_fails = 'teksts.txt'

# Izsauc funkciju ar norādīto faila nosaukumu
lasit_un_drukaz(mans_fails)