# Morse Code decoder

Este desafio implementa um decodificador para o código morse em python.
Sendo capaz de traduzir sequências de código Morse em texto legível para humanos. 
A entrada é feita pela linha de comando, e o programa suporta tanto letras quanto números e espaços entre palavras.

## 1. Descrição técnica da solução implementada

O programa `decode_morse.py` recebe uma string de código Morse como argumento da linha de comando e a converte em texto legível para humanos. A separação entre letras é feita por um espaço (` `), enquanto a separação entre palavras é representada por **três ou mais espaços consecutivos** (`   `). Espaços extras antes ou depois do código não têm significado e são ignorados.

## 2. Instruções para rodar o programa
### 2.1 Pré-requistos
    Python 3.x

### 2.2 Tornar o programa executável:
```
$ chmod +x decode_morse.py
```

### 2.3 Como executar o programa

No terminal, ir para o diretório onde o programa está localizado 
e executar conforme abaixo.  
opção 1:
```
$ python decode_morse.py '<morse code>'
````
opção 2:
```
$./decode_morse.py '<morse code>'
```
Exemplo:
```
$ ./decode_morse.py ".... . -.-- .--- ..- -.. ."
HEY JUDE
```
## 3. Testes de verificação do programa

Os seguintes testes foram implementados para verificação da
correta execução do programa:

* Decodificacao de uma única palavra
* Decodificacao de múltiplas palavras
* Decodificacao de números
* Decodificacao de letras e números juntos
* Decodificacao de codigo morse inválido
* Decodificacao com espaços extras

### 3.1 Instruções para rodar os testes

Para executar todos os testes,  executar o comando abaixo no diretório onde o programa foi instalado.
Para executar todos os testes:
```
$ python -m unittest test_decode_morse.py 
......
----------------------------------------------------------------------
Ran 6 tests in 0.000s

OK
```

Para executar todos os testes no modo `verbose`"
```
$ python -m unittest -v test_decode_morse
test_extra_spaces (test_decode_morse.TestMorseCodeToText)
Teste decodificacao com espacos extras. ... ok
test_invalid_morse_code (test_decode_morse.TestMorseCodeToText)
Teste decodificacao de codigo morse invalido. ... ok
test_letters_and_numbers (test_decode_morse.TestMorseCodeToText)
Teste decodificacao de letras e numeros juntos. ... ok
test_multiple_words (test_decode_morse.TestMorseCodeToText)
" ... ok
test_numbers (test_decode_morse.TestMorseCodeToText)
Teste decodificacao de numeros. ... ok
test_single_word (test_decode_morse.TestMorseCodeToText)
Teste decodificacao de uma unica palavra. ... ok

----------------------------------------------------------------------
Ran 6 tests in 0.000s

OK
```
Para executar um teste específico, utilizar o caminho completo, exemplo abaixo.
```
$ python -m unittest -v test_decode_morse.TestMorseCodeToText.test_single_word
test_single_word (test_decode_morse.TestMorseCodeToText)
Teste decodificacao de uma unica palavra. ... ok

----------------------------------------------------------------------
Ran 1 test in 0.000s

OK
```

## Código Morse

Segue abaixo, o código Morse para letras e números que
foi utilizado no desafio:  
A .-   
B -...   
C -.-.   
D -..   
E .   
F ..-.   
G --.   
H ....   
I ..   
J .---   
K -.-   
L .-..   
M --   
N -.   
O ---  
P .--.   
Q --.-   
R .-.  
S ...  
T -  
U ..-   
V ...-   
W .--   
X -..-  
Y -.--  
Z --..  
0 -----  
1 .----  
2 ..---  
3 ...--  
4 ....-  
5 .....  
6 -....  
7 --...  
8 ---..  
9 ----.  
