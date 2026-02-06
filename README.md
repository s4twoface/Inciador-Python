# 🚀 LAUNCHER DE ROTINAS - GUIA COMPLETO

## 📚 COMO ESTUDAR ESTE PROJETO

Este projeto tem **3 versões** que vão da mais simples até a mais avançada.
Estude nesta ordem:

### 1️⃣ VERSÃO 1 - Terminal (versao1_terminal.py)
**O QUE VOCÊ VAI APRENDER:**
- ✅ Variáveis
- ✅ Funções (def)
- ✅ Listas
- ✅ Loops (for, while)
- ✅ Condicionais (if, elif, else)
- ✅ Input do usuário
- ✅ Bibliotecas básicas (webbrowser, time, os)

**COMO RODAR:**
```bash
python versao1_terminal.py
```

**EXERCÍCIOS:**
1. Adicione um novo link na lista
2. Crie uma nova rotina (exemplo: "Rotina de Estudos")
3. Mude as cores do terminal
4. Adicione um contador de quantas vezes cada rotina foi usada


### 2️⃣ VERSÃO 2 - Interface Gráfica (versao2_tkinter.py)
**O QUE VOCÊ VAI APRENDER:**
- ✅ Classes e Objetos (POO - Programação Orientada a Objetos)
- ✅ Tkinter (interface gráfica)
- ✅ Widgets (Label, Button, Frame)
- ✅ Threading (não travar a interface)
- ✅ Messagebox (janelas popup)
- ✅ self (referência ao objeto)

**COMO RODAR:**
```bash
python versao2_tkinter.py
```

**EXERCÍCIOS:**
1. Mude as cores dos botões
2. Adicione um novo botão com uma rotina sua
3. Aumente o tamanho da janela
4. Adicione um ícone na janela (pesquise "tkinter iconbitmap")


### 3️⃣ VERSÃO 3 - Interface Moderna (versao3_customtkinter.py)
**O QUE VOCÊ VAI APRENDER:**
- ✅ CustomTkinter (Tkinter moderno)
- ✅ Dicionários aninhados
- ✅ JSON (salvar/carregar dados)
- ✅ Lambda functions
- ✅ Grid layout
- ✅ Progress bar
- ✅ Janelas secundárias (Toplevel)
- ✅ Try/Except (tratamento de erros)

**ANTES DE RODAR, INSTALE O CUSTOMTKINTER:**
```bash
pip install customtkinter
```

**COMO RODAR:**
```bash
python versao3_customtkinter.py
```

**EXERCÍCIOS:**
1. Adicione uma nova rotina no dicionário self.rotinas
2. Mude o tema de "dark" para "light"
3. Mude a cor do tema de "blue" para "green"
4. Implemente a função de salvar configurações de verdade


---

## 🎯 ROADMAP DE ESTUDO

### SEMANA 1 - Versão 1 (Terminal)
**Dia 1-2:** Leia o código inteiro, linha por linha
- Entenda o que cada função faz
- Rode o programa e teste tudo
- Leia os comentários com atenção

**Dia 3-4:** Modifique o código
- Adicione seus próprios links
- Crie uma nova rotina
- Mude as mensagens

**Dia 5-7:** Recrie do zero
- Abra um arquivo novo
- Tente fazer sem olhar o código original
- Consulte só quando travar


### SEMANA 2 - Versão 2 (Tkinter)
**Dia 1-3:** Estude POO (Classes)
- Entenda o que é uma classe
- O que é self
- O que é __init__
- Diferença entre função e método

**Dia 4-5:** Estude Tkinter
- Como funciona Label, Button, Frame
- O que é pack()
- Como funciona command=

**Dia 6-7:** Modifique e teste
- Mude cores, tamanhos
- Adicione novos botões
- Teste diferentes layouts


### SEMANA 3 - Versão 3 (Avançado)
**Dia 1-2:** Instale e rode
- pip install customtkinter
- Rode o programa
- Veja como ficou bonito!

**Dia 3-5:** Estude o código
- Entenda dicionários aninhados
- Veja como funciona o grid
- Estude as lambda functions

**Dia 6-7:** Customize
- Crie suas próprias rotinas
- Mude cores e design
- Adicione funcionalidades


---

## 🔧 CONCEITOS IMPORTANTES EXPLICADOS

### 1. VARIÁVEIS
```python
nome = "Andrew"  # String (texto)
idade = 20       # Integer (número inteiro)
altura = 1.75    # Float (número decimal)
ativo = True     # Boolean (verdadeiro/falso)
```

### 2. LISTAS
```python
links = ["google.com", "youtube.com", "github.com"]

# Acessar primeiro item (índice 0)
print(links[0])  # google.com

# Adicionar item
links.append("twitter.com")

# Remover item
links.remove("youtube.com")

# Loop pela lista
for link in links:
    print(link)
```

### 3. FUNÇÕES
```python
# Definir função
def somar(a, b):
    resultado = a + b
    return resultado

# Usar função
total = somar(5, 3)  # total = 8
```

### 4. CONDICIONAIS
```python
idade = 18

if idade < 18:
    print("Menor de idade")
elif idade == 18:
    print("Tem 18 anos")
else:
    print("Maior de idade")
```

### 5. LOOPS
```python
# While (enquanto)
contador = 0
while contador < 5:
    print(contador)
    contador += 1  # Adiciona 1

# For (para cada)
numeros = [1, 2, 3, 4, 5]
for num in numeros:
    print(num)
```

### 6. CLASSES (POO)
```python
class Cachorro:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def latir(self):
        print(f"{self.nome} fez: Au au!")

# Criar objeto
meu_cachorro = Cachorro("Rex", 3)
meu_cachorro.latir()  # Rex fez: Au au!
```

### 7. DICIONÁRIOS
```python
pessoa = {
    "nome": "Andrew",
    "idade": 20,
    "cidade": "Juiz de Fora"
}

# Acessar valor
print(pessoa["nome"])  # Andrew

# Adicionar/modificar
pessoa["profissao"] = "Desenvolvedor"
```


---

## 🐛 ERROS COMUNS E SOLUÇÕES

### Erro: "ModuleNotFoundError: No module named 'customtkinter'"
**Solução:** Instale com `pip install customtkinter`

### Erro: "IndentationError"
**Solução:** Python usa indentação (espaços). Confira se está tudo alinhado

### Erro: "NameError: name 'x' is not defined"
**Solução:** Você usou uma variável que não foi criada. Defina ela antes

### Programa não abre links
**Solução:** Confira se tem navegador instalado. Teste com: `webbrowser.open("google.com")`

### Janela abre e fecha rapidamente
**Solução:** Provavelmente tem erro no código. Rode pelo terminal pra ver o erro


---

## 💡 IDEIAS PARA MELHORAR O PROJETO

1. **Sistema de Login**
   - Cada usuário tem suas rotinas
   - Senha para acessar

2. **Atalhos de Teclado**
   - Ctrl+1 = Rotina 1
   - Ctrl+2 = Rotina 2

3. **Estatísticas**
   - Quantas vezes usou cada rotina
   - Gráfico de uso

4. **Temas Customizáveis**
   - Claro/Escuro
   - Cores personalizadas

5. **Minimizar para Bandeja**
   - Fica no ícone da barra
   - Abre com clique

6. **Notificações**
   - "Rotina aberta com sucesso!"
   - Notificações do Windows

7. **Banco de Dados**
   - SQLite para salvar dados
   - Histórico de uso

8. **Auto-Update**
   - Verifica se tem versão nova
   - Baixa automático


---

## 📖 RECURSOS PARA ESTUDAR MAIS

### Python Básico
- [Curso em Vídeo - Python](https://www.cursoemvideo.com/curso/python-3-mundo-1/)
- [W3Schools Python](https://www.w3schools.com/python/)
- [Python.org Tutorial](https://docs.python.org/pt-br/3/tutorial/)

### Tkinter
- [Real Python - Tkinter](https://realpython.com/python-gui-tkinter/)
- [TutorialsPoint Tkinter](https://www.tutorialspoint.com/python/python_gui_programming.htm)

### CustomTkinter
- [Documentação Oficial](https://customtkinter.tomschimansky.com/)
- [GitHub CustomTkinter](https://github.com/TomSchimansky/CustomTkinter)

### POO (Classes)
- [Programação Orientada a Objetos](https://www.youtube.com/watch?v=Gp2m8ZuXoPg)


---

## 🎓 DESAFIO FINAL

Depois de estudar as 3 versões, tente criar seu próprio launcher do ZERO com:

✅ Interface bonita (CustomTkinter)
✅ Sistema de login simples
✅ Pelo menos 5 rotinas diferentes
✅ Salvar configurações em JSON
✅ Atalhos de teclado
✅ Ícone personalizado

**BOA SORTE E BOM ESTUDO! 🚀**

Se tiver dúvidas, leia os comentários no código. Tá tudo explicado lá!
