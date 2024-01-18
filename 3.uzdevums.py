def tresa_rinda (teksts):
    try:
      with open('fails', "r", encoding='utf-8')as f:
        rindas=f.readlines()
      if len(rindas) >=3:
        rinda=rindas[2].strip()
        print("Trešās rindas saturs!")
        print(rinda)
      else:
        print("Nav pieteikami daudz rindu!")
    except FileNotFoundError:
        print(f"Fails {teksts}nav atrasts!")