import mysql.connector


conexao = mysql.connector.connect(
    host = "localhost",
    user = "root",

    password = "",

    database = "nave"
)

vnome = 'Conchinha'

vlogin = 'calvo'

vsenha = "123"


cursor = conexao.cursor()


#comando = "select * from tb_login"

#comando = f'insert into tb_login(nome,login,senha) values("{vnome}","{vlogin}","{vsenha}")
comando = "delete from tb_login where id = 2"
cursor.execute(comando)


#resultado = cursor.fetchall()
jls_extract_var = conexao
jls_extract_var.commit()

print("cadastrado")

