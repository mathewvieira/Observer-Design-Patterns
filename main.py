class Observer:
  listners = []
  
  def adicionarListener(self, listener):
    self.listners.append(listener)
    print("Listner adicionado: " + listener);
    print()

  def notificarListeners(self):
    print("- Notificando todos os Listeners -")
    for listener in self.listners:
      print("Notificação do Observer: " + listener)
    print()

  def notificarListener(self, listnerSrc, listnerDest):
    if listnerSrc in self.listners:
      if listnerDest in self.listners:
        print(listnerSrc + " notificou " + listnerDest)
      else:
        print("ListnerDest não encontrado")
    else:
      print("ListnerSrc não encontrado")
    print()
      
class Observable(Observer):
  name = ""
  
  def __init__(self, name):
    self.name = name
    super().adicionarListener(name)

  def notificarListener(self, listnerDest):
    super().notificarListener(self.name, listnerDest)

class Compras(Observable):
  def __init__(self, name):
    super().__init__(name)

  def apresentetion(self):
    print("Olá me chamo "+ self.name + "e sou responsável pelas Compras")
    print()
    
class MKT(Observable):
  def __init__(self, name):
    super().__init__(name)

  def apresentetion(self):
    print("Olá me chamo "+ self.name + "e sou responsável pelo Marketing")
    print()

class SAC(Observable):
  def __init__(self, name):
    super().__init__(name)

  def apresentetion(self):
    print("Olá me chamo "+ self.name + "e sou responsável pelo SAC")
    print()

class Estoque(Observable):
  def __init__(self, name):
    super().__init__(name)

  def apresentetion(self):
    print("Olá me chamo "+ self.name + "e sou responsável pelo Estoque")
    print()

if __name__ == '__main__':
  ob = Observer()
  
  compras = Compras("Compras_OB")
  mkt = MKT("MKT_OB")
  sac = SAC("SAC_OB")
  estoque = SAC("Estoque_OB")
  
  ob.notificarListeners()
  
  compras.notificarListener(mkt.name)
  
  sac2 = SAC("SAC2_OB")
  
  sac.notificarListener(sac2.name)
  
  ob.notificarListeners()
  
  estoque.notificarListener(compras.name)