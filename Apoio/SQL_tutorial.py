# Conexão com Banco de Dados
import sqlite3
conexao = sqlite3.connect('WoMakersAulaSincrona') # O arquivo do VSCode deve estar na mesma pasta que o arquivo do SQL
cursor = conexao.cursor()


#__________________________________
# 1. CREATE: Iniciar a criação do Banco de Dados
#cursor.execute('CREATE TABLE usuarios(id INT, nome VARCHAR(100), endereco VARCHAR(150), email VARCHAR(100))')
#cursor.execute('CREATE TABLE gerente(id INT, nome VARCHAR(100), endereco VARCHAR(150), email VARCHAR(100))')

#__________________________________
# 2. ALTER: Alteração do Banco de Dados
#cursor.execute('ALTER TABLE usuarios RENAME TO usuario')
#cursor.execute('ALTER TABLE usuario ADD COLUMN telefoni INT')


#__________________________________
# 3. ALTER: Alterar erros
#cursor.execute('ALTER TABLE usuario RENAME COLUMN telefoni TO telefone')


#__________________________________
# 4. DROP: Excluir tabela inteira - não tem como recuperar(!)
#cursor.execute('CREATE TABLE produtos(id INT, nome VARCHAR(100), endereco VARCHAR(150), email VARCHAR(100))')
#cursor.execute('DROP TABLE produtos')


#__________________________________
# 5. INSERT: Inserindo informação
#cursor.execute('INSERT INTO usuario(id, nome, endereco,email, telefone)VALUES(1, "Isadora","Cagnin", "isa@gmail.com", 16998580142)')
#cursor.execute('INSERT INTO usuario(id, nome, endereco,email, telefone)VALUES(2, "Raimunda","Profunda", "rai@gmail.com", 16998598562)')
#cursor.execute('INSERT INTO usuario(id, nome, endereco,email, telefone)VALUES(3, "Elvira","Bruxist", "elvira@gmail.com", 16998527349)')
#cursor.execute('INSERT INTO usuario(id, nome, endereco,email, telefone)VALUES(4, "Magenta","Ciano", "mag@gmail.com", 16998587549)')
#cursor.execute('INSERT INTO usuario(id, nome, endereco,email, telefone)VALUES(5, "Willow","Kyoto", "will@gmail.com", 16921327549)')
#cursor.execute('INSERT INTO usuario(id, nome, endereco,email, telefone)VALUES(6, "Willow","Tokyo", "wllw@gmail.com", 16234587549)')


#__________________________________
# 6. DELETE: Exclusão de dados pontuais (selecionados)
#cursor.execute('DELETE FROM usuario where id=1')


#__________________________________
# 7. SELECT: Ver as informações que estão no Banco de Dados
#dados = cursor.execute('SELECT * FROM usuario') 

#for usuario in dados:
#    print(usuario)

"""o asterisco seleciona tudo da tabela. 
Se quiser selecionar um dado em específico, trocar o asterisco pelo nome da variável
Exemplo:  

dados = cursor.execute('SELECT nome,telefone FROM usuario WHERE id >2')

Aqui adicionamento também uma condicional: aonde o id for maior que 2 """

#__________________________________
# 8. UPDATE: queremos mudar os dados
#cursor.execute('UPDATE usuario SET endereco="Minas Gerais" WHERE id=3')
#cursor.execute('UPDATE usuario SET endereco="São Paulo" WHERE nome="Raimunda"')
#cursor.execute('UPDATE usuario SET endereco="California" WHERE id=4')


#__________________________________
# 9. ORDER BY e DESC: Ordenando dados e ordem decrescente
#dados = cursor.execute('SELECT * FROM usuario ORDER BY nome,id DESC')  # É possível usar mais de uma variavel,variavel.... DESC = decrescente (reverso)
#for usuario in dados:
#    print(usuario)


#__________________________________
# 10. LIMIT E DISTINCT: 
# LIMIT - usado para
# DISTINCT - usado para retornar apenas valores distintos. Se houver valores duplicados ele não lerá nenhum.

# dados = cursor.execute('SELECT * FROM usuario LIMIT 2') # Retorna apenas os n de limite iniciais da Base de Dados
# dados = cursor.execute('SELECT DISTINCT * FROM usuario')
#for usuario in dados:
#    print(usuario)


#__________________________________
# GROUP BY e HAVING:
# GROUP BY - Agrupa com mais de uma condição específica e permite somas, médias etc
# HAVING - 

#dados = cursor.execute('SELECT nome, id FROM usuario GROUP BY nome')
#for usuario in dados:
#    print(usuario)

#print()

#dados = cursor.execute('SELECT nome, id FROM usuario GROUP BY nome HAVING id>3')
#for usuario in dados:
#    print(usuario)

# Cláusulas JOIN (Right, Left, Full, Inner)
# Join é uma cláusula para combinar informações de duas ou mais tabelas em condições específicas que desejamos aplicar

#cursor.execute('INSERT INTO gerente(id, nome, endereco,email)VALUES(6, "Willow","Tokyo", "wllw@gmail.com")')
#cursor.execute('INSERT INTO gerente(id, nome, endereco,email)VALUES(2, "Gulherme","Tokyo", "gui@gmail.com")')
#cursor.execute('INSERT INTO gerente(id, nome, endereco,email)VALUES(5, "Ichigo","Tokyo", "ichigo@gmail.com")')
#cursor.execute('INSERT INTO gerente(id, nome, endereco,email)VALUES(4, "Yakimeshi","Hong Kong", "yaki@gmail.com")')
#cursor.execute('INSERT INTO gerente(id, nome, endereco,email)VALUES(3, "Go Haw","Seul", "gh@gmail.com")')
#cursor.execute('INSERT INTO gerente(id, nome, endereco,email)VALUES(1, "Kira","Tokyo", "deathnote@gmail.com")')

"""dados_gerente = cursor.execute('SELECT * FROM gerente')
for gerente in dados_gerente:
    print(gerente)"""

# JOIN - INNER JOIN
# Seleciona as informações das tabelas onde há equivalência de valores em ambas tabelas
"""dados = cursor.execute('SELECT * FROM usuario INNER JOIN gerente ON usuario.id=gerente.id')
for usuario in dados:
    print(usuario)"""

# JOIN - LEFT JOIN
# Coloca todas as informações da tabela a esquerda e trás as informações da tabela da direita se houver equivalência com a da esquerda
"""dados = cursor.execute('SELECT * FROM usuario LEFT JOIN gerente ON usuario.nome=gerente.nome')
for usuario in dados:
    print(usuario)
print()"""

# JOIN - RIGHT JOIN
# Coloca todas as informações da tabela a direita e trás as informações da tabela da esquerda se houver equivalência com a da direita
"""dados = cursor.execute('SELECT * FROM usuario RIGHT JOIN gerente ON usuario.nome=gerente.nome')
for usuario in dados:
    print(usuario)
print()"""
    

# JOIN - FULL JOIN
# Compara nas duas tabelas
"""dados = cursor.execute('SELECT * FROM usuario FULL JOIN gerente ON usuario.nome=gerente.nome')
for usuario in dados:
    print(usuario)
print()"""
        

# SUB CONSULTAS
# As Sub consultas são consultas SQL que são arqueadas dentro da consulta principal. Ela permite que utilizemos a subconsulta como parte de uma consulta.

# dados = cursor.execute('SELECT * FROM usuario WHERE nome IN (SELECT nome FROM gerente)')
# for usuario in dados:
#     print(usuario)

#__________________________________
# Final de comandos Base para a Conexão com Banco de Dados
conexao.commit()
conexao.close