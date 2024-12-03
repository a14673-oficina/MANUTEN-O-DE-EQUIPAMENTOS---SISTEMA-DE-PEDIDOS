#Função para registar um pedido
def registar_pedido(pedidos):
  id_pedido = len(pedidos) + 1
  descricao = input("Descrição do problema: ")
  estado = "Pendente"
  pedidos[id_pedido] = {"descricao": descricao, "estado": estado}
  print(f"Pedido #{id_pedido} registado com sucesso!")

#Função para eliminar um pedido
def eliminar_pedido(pedidos):
    id_pedido = int(input("ID do pedido a eliminar: "))
    if id_pedido in pedidos:
        pedidos.pop(id_pedido)
        print(f"Pedido #{id_pedido} eliminado com sucesso!")
    else:
        print("Não foi possivel eliminar o pedido")
#Função para consultar um pedido
def consultar_pedido(pedidos):
  id_pedido = int(input("ID do pedido a consultar: "))
  if id_pedido in pedidos:
      pedido = pedidos[id_pedido]
      print(f"Pedido #{id_pedido} - Descrição: {pedido['descricao']}, Estado: {pedido['estado']}")
  else:
      print("Pedido não encontrado.")

#Função para atualizar um estado
def atualizar_estado(pedidos):
  id_pedido = int(input("ID do pedido a atualizar: "))
  if id_pedido in pedidos:
      novo_estado = input("Novo estado (Pendente/Em Andamento/Concluído): ")
      if novo_estado in ["Pendente", "Em Andamento", "Concluído"]:
          pedidos[id_pedido]["estado"] = novo_estado
          print(f"Estado do pedido #{id_pedido} atualizado para '{novo_estado}'.")
      else:
          print("Estado inválido.")
  else:
      print("Pedido não encontrado.")

#Função para exibir um pedido
def exibir_pedidos(pedidos):
  print("\nLista de Pedidos:")
  print("ID\tDescrição\t\tEstado")
  print("-" * 40)
  for id_pedido, info in pedidos.items():
      print(f"{id_pedido}\t{info['descricao'][:15]}\t\t{info['estado']}")
#Função para exibir o menu
def main():
  pedidos = {}
  while True:
      print("\nSistema de Gestão de Pedidos - Manutenção")
      print("1. Registar Pedido")
      print("2. Eliminar Pedido")
      print("3. Consultar Pedido")
      print("4. Atualizar Estado")
      print("5. Exibir Todos os Pedidos")
      print("6. Sair")
      opcao = input("Escolha uma opção: ")

      if opcao == "1":
          registar_pedido(pedidos)
      elif opcao == "2":
          eliminar_pedido(pedidos)
      elif opcao == "3":
          consultar_pedido(pedidos)
      elif opcao == "4":
          atualizar_estado(pedidos)
      elif opcao == "5":
          exibir_pedidos(pedidos)
      elif opcao == "6":
          print("Encerrando o sistema...")
          break
      else:
          print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
  main()
