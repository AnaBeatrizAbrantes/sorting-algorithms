# 1
def selection_sort(lista):
    n = len(lista)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if lista[j] < lista[min_idx]:
                min_idx = j
        lista[i], lista[min_idx] = lista[min_idx], lista[i]
    return lista

# 2
def insertion_sort(lista):
    for i in range(1, len(lista)):
        chave = lista[i]
        j = i - 1
        while j >= 0 and lista[j] > chave:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = chave
    return lista

# 3
def merge_sort(lista):
    if len(lista) > 1:
        meio = len(lista) // 2
        esquerda = lista[:meio]
        direita = lista[meio:]

        merge_sort(esquerda)
        merge_sort(direita)

        i = j = k = 0
        while i < len(esquerda) and j < len(direita):
            if esquerda[i] < direita[j]:
                lista[k] = esquerda[i]
                i += 1
            else:
                lista[k] = direita[j]
                j += 1
            k += 1

        while i < len(esquerda):
            lista[k] = esquerda[i]
            i += 1
            k += 1

        while j < len(direita):
            lista[k] = direita[j]
            j += 1
            k += 1
    return lista

# 4
def quick_sort(lista):
    if len(lista) <= 1:
        return lista
    pivo = lista[len(lista) // 2]
    menores = [x for x in lista if x < pivo]
    iguais = [x for x in lista if x == pivo]
    maiores = [x for x in lista if x > pivo]
    return quick_sort(menores) + iguais + quick_sort(maiores)

# 5
def heapify(lista, n, i):
    maior = i
    esquerda = 2 * i + 1
    direita = 2 * i + 2

    if esquerda < n and lista[esquerda] > lista[maior]:
        maior = esquerda
    if direita < n and lista[direita] > lista[maior]:
        maior = direita
    if maior != i:
        lista[i], lista[maior] = lista[maior], lista[i]
        heapify(lista, n, maior)

def heap_sort(lista):
    n = len(lista)
    for i in range(n // 2 - 1, -1, -1):
        heapify(lista, n, i)
    for i in range(n - 1, 0, -1):
        lista[i], lista[0] = lista[0], lista[i]
        heapify(lista, i, 0)
    return lista

# 6
def counting_sort(lista):
    if not lista:
        return lista
    max_val = max(lista)
    contagem = [0] * (max_val + 1)
    for num in lista:
        contagem[num] += 1
    idx = 0
    for i, qtd in enumerate(contagem):
        for _ in range(qtd):
            lista[idx] = i
            idx += 1
    return lista

# 7
def counting_sort_radix(lista, exp):
    n = len(lista)
    saida = [0] * n
    contagem = [0] * 10

    for i in range(n):
        indice = (lista[i] // exp) % 10
        contagem[indice] += 1

    for i in range(1, 10):
        contagem[i] += contagem[i - 1]

    i = n - 1
    while i >= 0:
        indice = (lista[i] // exp) % 10
        saida[contagem[indice] - 1] = lista[i]
        contagem[indice] -= 1
        i -= 1

    for i in range(n):
        lista[i] = saida[i]

def radix_sort(lista):
    if not lista:
        return lista
    max_val = max(lista)
    exp = 1
    while max_val // exp > 0:
        counting_sort_radix(lista, exp)
        exp *= 10
    return lista

# 8
def bucket_sort(lista):
    if len(lista) == 0:
        return lista
    max_val, min_val = max(lista), min(lista)
    bucket_count = len(lista)
    buckets = [[] for _ in range(bucket_count)]

    for num in lista:
        idx = int(((num - min_val) / (max_val - min_val + 1e-9)) * (bucket_count - 1))
        buckets[idx].append(num)

    lista.clear()
    for bucket in buckets:
        insertion_sort(bucket)
        lista.extend(bucket)
    return lista

# 9
def bubble_sort(lista):
    n = len(lista)
    for i in range(n):
        trocou = False
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                trocou = True
        if not trocou:
            break
    return lista

lista_exemplo = [5, 2, 9, 1, 5, 6]

print("selection sort:", selection_sort(lista_exemplo.copy()))
print("insertion sort:", insertion_sort(lista_exemplo.copy()))
print("merge sort:", merge_sort(lista_exemplo.copy()))
print("quick sort:", quick_sort(lista_exemplo.copy()))
print("heap sort:", heap_sort(lista_exemplo.copy()))
print("counting sort:", counting_sort(lista_exemplo.copy()))
print("radix sort:", radix_sort(lista_exemplo.copy()))
print("bucket sort:", bucket_sort(lista_exemplo.copy()))
print("bubble sort:", bubble_sort(lista_exemplo.copy()))
