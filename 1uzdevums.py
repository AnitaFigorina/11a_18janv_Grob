def lasit_un_drukaz(teksta_fails):
    try:
        with open(teksta_fails, 'r', encoding='utf-8') as fails:
            saturs = fails.read()
            print("Faila saturs:")
            print(saturs)
    except FileNotFoundError:
        print(f"Fails ar nosaukumu '{teksta_fails}' NAV ticis atrasts.")
    except Exception as e:
        print(f"Radās kļūda: {e}")

mans_fails = 'teksts.txt'
lasit_un_drukaz(mans_fails)