class LogisticaException(Exception):
    """Exceção base do sistema."""
    pass


class TransicaoStatusInvalida(LogisticaException):
    """Status não pode ser alterado para o valor solicitado."""
    pass


class PedidoJaAvaliado(LogisticaException):
    """Pedido já possui avaliação."""
    pass


class PermissaoNegada(LogisticaException):
    """Usuário não tem permissão para esta ação."""
    pass


class DoacaoIndisponivel(LogisticaException):
    """Doação não está mais disponível."""
    pass


class UsuarioJaCadastrado(LogisticaException):
    """Email ou CPF já cadastrado."""
    pass
