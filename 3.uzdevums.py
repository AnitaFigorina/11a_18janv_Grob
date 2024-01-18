def tikai_treso_rindu(texta_fails):
    try:
        with open(texta_fails, 'r', encoding='utf-8') as abece:
            rindas = abece.readlines()
            if len(rindas) >= 3:
                tresa_rinda = rindas[2]
                print("Trešajā rindā ir teikts: ")
                print(tresa_rinda)
            else:
                print("Failā nav TIK daudz rindu.")
    except FileNotFoundError:
        print(f"Fails ar nosaukumu '{texta_fails}' nav ticis atrasts.")
    except Exception as i:
        print(f"Radās kļūda: {i}")


abeces_fails = 'teksts.txt'


tikai_treso_rindu(abeces_fails)