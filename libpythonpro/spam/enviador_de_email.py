class Enviador:
    def enviar(self, remetente: object, destinatario: object, assunto: object, corpo: object) -> object:
        if "@" not in remetente:
            raise EmailInvalido(f"Email de remetente invalido{remetente}")
        return remetente


class EmailInvalido(Exception):
    pass
