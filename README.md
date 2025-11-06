# Algoritmos de Ordenação em Python  

Este projeto implementa diversos **algoritmos de ordenação** para a disciplina de **Algoritmos**, com o objetivo de compreender como diferentes métodos organizam listas de dados.  
Os algoritmos foram implementados em **Python** de forma simples e didática.  

## Descrição dos Algoritmos  

### Selection Sort  
Percorre a lista procurando o menor elemento e o coloca na posição correta a cada iteração.  
**Vantagens:** Simples de entender e implementar.  
**Desvantagens:** Ineficiente para listas grandes (complexidade O(n²)).  

### Insertion Sort  
Insere cada elemento na posição correta em relação aos anteriores, como se estivesse ordenando cartas na mão.  
**Vantagens:** Rápido para listas pequenas ou quase ordenadas.  
**Desvantagens:** Lento para listas grandes (O(n²)).  

### Merge Sort  
Divide a lista em duas partes, ordena cada uma e depois as intercala.  
**Vantagens:** Muito eficiente (O(n log n)) e estável.  
**Desvantagens:** Usa memória extra por causa das listas auxiliares.  

### Quick Sort  
Escolhe um pivô e separa os elementos menores e maiores, ordenando recursivamente.  
**Vantagens:** Um dos mais rápidos na prática (O(n log n) em média).  
**Desvantagens:** Pode ter pior caso O(n²) se o pivô for mal escolhido.  

### Heap Sort  
Transforma a lista em uma estrutura de heap e vai extraindo o maior elemento até ordenar tudo.  
**Vantagens:** Tempo garantido de O(n log n) e sem necessidade de memória extra.  
**Desvantagens:** Implementação mais complexa e não é estável.  

### Counting Sort  
Conta quantas vezes cada número aparece e reconstrói a lista em ordem.  
**Vantagens:** Muito rápido para inteiros pequenos (O(n + k)).  
**Desvantagens:** Só funciona com inteiros positivos em um intervalo pequeno.  

### Radix Sort  
Ordena os números dígito por dígito usando o Counting Sort como base.  
**Vantagens:** Excelente para números inteiros grandes.  
**Desvantagens:** Limitado a dados numéricos e consome mais memória.  

### Bucket Sort  
Distribui os elementos em "baldes" (buckets), ordena cada um e depois junta tudo.  
**Vantagens:** Muito eficiente para números uniformemente distribuídos.  
**Desvantagens:** Ineficiente se os dados estiverem concentrados em poucos intervalos.  

### Bubble Sort  
Compara pares de elementos vizinhos e troca de posição até que tudo esteja ordenado.  
**Vantagens:** Fácil de entender e implementar.  
**Desvantagens:** Extremamente ineficiente (O(n²)), usado apenas para fins didáticos.  

---

### Autores  
**Ana Beatriz Abrantes da Silva; Beatriz Barbosa M. L. da Silva; Hudson N. P. Vieira; Rafael dos S. Paulo**  
Estudantes de **Engenharia de Software**  
Disciplina: **Algoritmos**  

---

### Execução  

Basta rodar o código principal para testar os algoritmos:  

```bash
python nome_do_arquivo.py
