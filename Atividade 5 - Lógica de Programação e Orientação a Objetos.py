import time
import os
def sistema():
  print("Terrestre, Aéreo ou Aquático?");
  print("");
  rspt = input();
  txt = rspt.lower();
  if txt == "terrestre":
    print("""
Cabe apenas uma pessoa?
Sim ou Não?
  """);
    rspt = input();
    txt = rspt.lower();
    if txt == "sim":
      print("""
É pesado?
""");
      rspt = input();
      txt = rspt.lower();
      if txt == "sim":
        print("");
        print("É trator");
      else:
        print("""
Tem pendal?
""");
        rspt = input();
        txt = rspt.lower();
        if txt == "sim":
          print("");
          print("É bicicleta");
        else:
          print("");
          print("Me desculpe, não sei qual é o meio de transporte!")
  
  
    else:
      print ("""
Usa capacete?
""");
      rspt = input();
      txt = rspt.lower();
      if txt == "sim":
        print("");
        print("É moto!");
      else:
        print("""
Tem passageiro?
""");
        rspt = input();
        txt = rspt.lower();
        if txt == "sim":
          print("""
Usa trilho?
""");
          rspt = input();
          txt = rspt.lower();
          if txt == "sim":
            print("");
            print("É trem!")
          else:
            print("""
Anda na pista?
""");
            rspt = input();
            txt = rspt.lower();
            if txt == "sim":
              print("""
É alto?
""");
              rspt = input();
              txt = rspt.lower();
              if txt == "sim":
                print("""
Usa carroceria?
""");
                rspt = input();
                txt = rspt.lower();
                if txt == "sim":
                  print("");
                  print("É caminhão!");
                else:
                  print("""
Pode ter cobrador?
""");
                  rspt = input();
                  txt = rspt.lower();
                  if txt == "sim":
                    print("");
                    print("É ônibus!")
                  else:
                    print("")
                    print("Me desculpe, não sei qual é o meio de transporte!")
                    
              else:
                print("""
É veículo leve?
""")
                rspt = input();
                txt = rspt.lower();
                if txt == "sim":
                  print("");
                  print("É carro!")
                else:
                  print("")
                  print("Me desculpe, não sei qual é o meio de transporte!")
            else:
              print("")
              print("Me desculpe, não sei qual é o meio de transporte!")
        else:
          print("")
          print("Me desculpe, não sei qual é o meio de transporte!")
  elif txt == "aereo":
    print("""
Precisa pular?
Sim ou Não?
""");
    rspt = input();
    txt = rspt.lower();
    if txt == "sim":
      print("");
      print("É asa delta!");
    else:
      print("""
Viaja dentro?
""");
      rspt = input();
      txt = rspt.lower();
      if txt == "sim":
        print("""
É devagar?
""");
        rspt = input();
        txt = rspt.lower();
        if txt == "sim":
          print("");
          print("É balão");
        else:
          print("""
Tem piloto?
""");
          rspt = input();
          txt = rspt.lower();
          if txt == "sim":
            print("""
Tem asas fixas?
""");
            rspt = input();
            txt = rspt.lower();
            if txt == "sim":
              print("");
              print("É avião");
            else:
              print("""
Faz vôo vertical?
""");
              rspt = input();
              txt = rspt.lower();
              if txt == "sim":
                print("");
                print("É helicóptero");
              else:
                print("");
                print("Me desculpe, não sei qual é o meio de transporte!");
          else:
            print("");
            print("Me desculpe, não sei qual é o meio de transporte!")
      else:
        print("");
        print("Me desculpe, não sei qual é o meio de transporte!")
  elif txt == "aquatico":
    print("""
É coberto d'água??
Sim ou Não?
""");
    rspt = input();
    txt = rspt.lower();
    if txt == "sim":
      print("");
      print("É submarino!");
    else:
      print("""
Navega na água?
""");
      rspt = input();
      txt = rspt.lower();
      if txt == "sim":
        print("""
Possui vela?
""");
        rspt = input();
        txt = rspt.lower();
        if txt == "sim":
          print("");
          print("É barco!");
        else:
          print("""
Tem motor?
""");
          rspt = input();
          txt = rspt.lower();
          if txt == "sim":
            print("""
É alto?
""");
            rspt = input();
            txt = rspt.lower();
            if txt == "sim":
              print("");
              print("É navio!");
            else:
              print("""
Pode ser descoberto?
""");
              rspt = input();
              txt = rspt.lower();
              if txt == "sim":
                print("");
                print("É lancha!");
              else:
                print("");
                print("Me desculpe, não sei qual é o meio de transporte!");
  
          else:
                print("");
                print("Me desculpe, não sei qual é o meio de transporte!");
      else:
                print("");
                print("Me desculpe, não sei qual é o meio de transporte!");
  else:
    print("");
    print("Desculpe não compreendi, tente novamente!");
    time.sleep(2);
    os.system('clear')
    sistema()
sistema()
