def fatorial(n):
    if not isinstance(n, int) or n < 0:
        raise ValueError("Valor deve ser um número maior ou igual a zero.")
    if n == 0:
        return 1
    else:
        return n * fatorial(n - 1)
