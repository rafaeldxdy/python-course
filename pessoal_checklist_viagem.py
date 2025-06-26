import mysql.connector

# Configurações da conexão com o banco de dados
DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': 'root',
    'database': 'lista_viagem'
}

def conectar_db():
    """Conecta ao banco de dados MySQL."""
    try:
        mydb = mysql.connector.connect(**DB_CONFIG)
        return mydb, mydb.cursor()
    except mysql.connector.Error as err:
        print(f"Erro ao conectar ao MySQL: {err}")
        return None, None

def desconectar_db(mydb, cursor):
    """Desconecta do banco de dados MySQL."""
    if cursor:
        cursor.close()
    if mydb and mydb.is_connected():
        mydb.close()

def adicionar_item(descricao):
    """Adiciona um novo item ao banco de dados."""
    mydb, cursor = conectar_db()
    if mydb:
        try:
            sql = "INSERT INTO lista_itens (descricao) VALUES (%s)"
            cursor.execute(sql, (descricao,))
            mydb.commit()
            print(f'Item "{descricao}" adicionado com sucesso!')
        except mysql.connector.Error as err:
            print(f"Erro ao adicionar item: {err}")
            mydb.rollback()
        finally:
            desconectar_db(mydb, cursor)

def listar_itens():
    """Lista todos os itens do banco de dados."""
    mydb, cursor = conectar_db()
    if mydb:
        try:
            sql = "SELECT * FROM lista_itens"
            cursor.execute(sql)
            itens = cursor.fetchall()
            if not itens:
                print('Sua lista está vazia.')
            else:
                print('Lista de itens:')
                for item in itens:
                    print(f'{item[0]} - {item[1]}')
            return [item[0] for item in itens] # Retorna os IDs para a função ticar
        except mysql.connector.Error as err:
            print(f"Erro ao listar itens: {err}")
        finally:
            desconectar_db(mydb, cursor)
            return []

def ticar_item(item_id):
    """Marca um item como "ticado" (removido) no banco de dados."""
    mydb, cursor = conectar_db()
    if mydb:
        try:
            sql = "DELETE FROM lista_itens WHERE id = %s"
            cursor.execute(sql, (item_id,))
            mydb.commit()
            if cursor.rowcount > 0:
                print(f'Item com ID "{item_id}" ticado com sucesso!')
            else:
                print(f'Item com ID "{item_id}" não encontrado na lista!')
        except mysql.connector.Error as err:
            print(f"Erro ao ticar item: {err}")
            mydb.rollback()
        finally:
            desconectar_db(mydb, cursor)

while True:
    opcao = input('O que gostaria de fazer? \n1 - Adicionar item'
                  '\n2 - Listar itens'
                  '\n3 - Ticar item'
                  '\n4 - Sair\n')

    if opcao == '1':
        item = input('O que deseja adicionar? ')
        adicionar_item(item)
    elif opcao == '2':
        listar_itens()
    elif opcao == '3':
        ids_disponiveis = listar_itens() # Primeiro listamos para o usuário ver os IDs
        item_id = input('Qual o número do item que deseja ticar? ')

        if item_id in ids_disponiveis:
            try:
                item_id = input('Qual o número do item que deseja ticar? ')
                if item_id in ids_disponiveis:
                    ticar_item(item_id)
                else:
                    print(f'Número "{item_id}" não encontrado na lista.')
            except ValueError:
                print('Por favor, insira um número válido.')
        else:
            print('Sua lista está vazia.')
    elif opcao == '4':
        break
    else:
        print('Opção inválida! Tente novamente.')

print('Programa encerrado.')