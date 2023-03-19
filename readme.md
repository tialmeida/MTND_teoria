# Máquina de Turing Não Determinística (MTND)

Este projeto é um trabalho entragável da disciplina de Teoria de Computação. 
Nele é possível encontrar um algorimo capaz de processar qualquer MTND.

> :technologist: Aluno: Tiago Almeida Santos - 2022134470

## Como utilizar
1. Instale o [PyCharm](https://www.jetbrains.com/pt-br/pycharm/download/#section=windows);
2. Execute o arquivo [main.py](main.py);
3. Dê as seguintes entradas:
   1. Estados;
   2. Alfabeto de entrada;
   3. Alfabeto da fita;
   4. Símbolo de limitação da fita a esquerda;
   5. Símbolo branco da fita;
   6. Número total de transições;
   7. Quintuplas contendo:
      1. Estado de origem;
      2. Caractere a ser lido;
      3. Estado de destino;
      4. Caractere a ser escrito;
      5. Direção de movimentação da fita;
   8. Estado inicial;
   9. Estados finais;
   10. Palavras de teste a serem reconhecidas;
4. Agora o programa devolve as saídas S ou N para indicação aceitação ou rejeição das palavras na mesma ordem de entrada.

> Estados, símbolos do alfabeto, itens das triplas, estados finais e palavras de testes devem ser separados por um espaço.
> <br>Estado inicial deve ser único. E o número total de transições deve ser um número inteiro.


## Maquina de Turing

O Algoritmo da Máquina de Turing tem poder computacional maior que uma AFD e de um ADP. Podendo reconhecer qualquer 
linguagem recursivamente enumerável. O que engloba linguagens: regulares, livres de contexto, sensíveis ao contexto e recursivas.
A Máquina de Turing possui memória e pode ir e voltar na fita fazendo alterações na palavra original, o que confere grande
versatilidade para projetar.

<br>O algoritmo foi projetado pensando nos requisitos:
- Qualquer MT deve ser capaz de ser processada;
- A quantidade de entradas pode variar entra zero e um número finito;
- Não deve ser impresso nada além do resultado final;
- Padrão de entrada e saída definidos pelo professor;
- Não deve ser utilizado mais de um arquivo.

A estrutura de dados utilizada para gerenciamento e processamento foi grafos. Não houve uma metodologia de software específica adotada,
foi utilizada orientações a objetos e programação imperativa. O não determinista foi gerenciado por meio de um array com fitas 
a serem processadas de forma síncrona e sequencial.
<br>Os testes foram manuais, ou seja, escritos casos de testes no blocos de notas e inputados via terminal e o controle de versões foi realizado via Github.