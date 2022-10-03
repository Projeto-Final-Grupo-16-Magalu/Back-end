db_usuarios =[]


def persistencia_usuario_cadastrar(novo_usuario):
    id_novo_usuario =len(db_usuarios)+1
    novo_usuario["id"]= id_novo_usuario
    db_usuarios.append(novo_usuario)
    return novo_usuario
