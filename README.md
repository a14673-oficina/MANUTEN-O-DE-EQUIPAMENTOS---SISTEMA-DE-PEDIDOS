# Sistema de Gestão de Pedidos de Manutenção

## Português (Portugal)

### Descrição Geral
Este é um programa que permite gerir pedidos de manutenção de forma simples e eficiente. O utilizador pode criar, consultar, atualizar e eliminar pedidos, bem como visualizar todos os pedidos registados.

---

### Funcionalidades Principais
1. **Registar Pedido**: Cria um novo pedido com uma descrição e estado inicial definido como *Pendente*.
2. **Eliminar Pedido**: Permite eliminar um pedido com base no ID.
3. **Consultar Pedido**: Exibe os detalhes de um pedido específico.
4. **Atualizar Estado**: Altera o estado de um pedido para *Pendente*, *Em Andamento* ou *Concluído*.
5. **Exibir Todos os Pedidos**: Lista todos os pedidos em formato tabular.

---

### Estrutura do Código
- **Funções Modulares**: Cada funcionalidade é implementada numa função separada para maior clareza e manutenção.
  - `registar_pedido`: Regista um novo pedido.
  - `eliminar_pedido`: Elimina um pedido específico.
  - `consultar_pedido`: Mostra detalhes de um pedido.
  - `atualizar_estado`: Altera o estado de um pedido.
  - `exibir_pedidos`: Lista todos os pedidos.
- **Controlos de Fluxo**: Utiliza condições `if-elif-else` para gerir escolhas do utilizador.
- **Gestão de Dados**: Os dados dos pedidos são armazenados num dicionário Python, onde o ID do pedido é a chave.

---

### Desafios e Soluções
1. **Validação de Entradas**: Para evitar erros, adicionaram-se verificações para garantir que IDs e estados introduzidos são válidos.
2. **Expansão Modular**: A estrutura modular permite adicionar novas funcionalidades facilmente no futuro.

---

### Como Usar
1. Execute o programa.
2. Siga as instruções no menu para criar, consultar, atualizar ou eliminar pedidos.
3. Escolha a opção **6** para sair do sistema.

---

## English

### Overview
This is a program that allows you to manage maintenance requests simply and efficiently. Users can create, view, update, and delete requests, as well as display all registered requests.

---

### Main Features
1. **Register Request**: Creates a new request with a description and an initial status set as *Pending*.
2. **Delete Request**: Deletes a request based on its ID.
3. **View Request**: Displays the details of a specific request.
4. **Update Status**: Changes the status of a request to *Pending*, *In Progress*, or *Completed*.
5. **Display All Requests**: Lists all requests in a tabular format.

---

### Code Structure
- **Modular Functions**: Each functionality is implemented in a separate function for clarity and maintainability:
  - `register_request`: Registers a new request.
  - `delete_request`: Deletes a specific request.
  - `view_request`: Displays details of a request.
  - `update_status`: Changes the status of a request.
  - `display_requests`: Lists all requests.
- **Flow Control**: Uses `if-elif-else` conditions to manage user choices.
- **Data Management**: Request data is stored in a Python dictionary, where the request ID is the key.

---

### Challenges and Solutions
1. **Input Validation**: Added checks to ensure entered IDs and statuses are valid, avoiding errors.
2. **Modular Expansion**: The modular structure makes it easy to add new features in the future.

---

### How to Use
1. Run the program.
2. Follow the menu instructions to create, view, update, or delete requests.
3. Select option **6** to exit the system.
