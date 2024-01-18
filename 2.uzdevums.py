import csv

def lasitotrokolonu(csv_failins):
    try:
        with open(csv_failins, 'r', newline='', encoding='utf-8') as sodiena:
            lasii = csv.reader(sodiena)
            
            # Izdrukā otrās kolonnas datus
            for rinda in lasii:
                if len(rinda) >= 2:  
                    otra_kolonna = rinda[1]
                    print(otra_kolonna)
    except FileNotFoundError:
        print(f"CSV fails ar nosaukumu '{csv_failins}' netika atrasts.")
    except Exception as e:
        print(f"Radās kļūda: {e}")

# Mainīgais ar CSV faila nosaukumu, piemēram, 'mans_csv_fails.csv'
anitas_csv_fails = 'aste.csv'

# Izsauc funkciju ar norādīto CSV faila nosaukumu
lasitotrokolonu(anitas_csv_fails)