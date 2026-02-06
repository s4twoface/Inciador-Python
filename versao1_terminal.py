# -*- coding: utf-8 -*-
# ========================================
# VERSAO 1: LAUNCHER NO TERMINAL
# ========================================
# Este e o mais basico - so terminal, sem interface grafica
# Aqui voce vai entender a LOGICA do programa

import webbrowser  # Biblioteca pra abrir sites no navegador
import time        # Biblioteca pra fazer pausas (esperar)
import os          # Biblioteca pra interagir com sistema operacional

# ===== FUNCAO: LIMPAR TELA =====
def limpar_tela():
    """
    Limpa a tela do terminal
    'cls' funciona no Windows
    'clear' funciona no Linux/Mac
    """
    os.system('cls' if os.name == 'nt' else 'clear')


# ===== FUNCAO: MOSTRAR MENU =====
def mostrar_menu():
    """
    Mostra o menu principal pro usuario
    Triple quotes permitem texto em varias linhas
    """
    limpar_tela()
    print("=" * 60)
    print("           LAUNCHER DE ROTINAS - VERSAO TERMINAL")
    print("=" * 60)
    print()
    print("  [1] Rotina de Trabalho Completa")
    print("  [2] Apenas Comunicacao (Teams, Email)")
    print("  [3] Apenas Sistemas Administrativos")
    print("  [4] Configuracoes")
    print("  [5] Sair")
    print()
    print("=" * 60)


# ===== FUNCAO: ABRIR ROTINA COMPLETA =====
def rotina_completa():
    """
    Abre TODOS os links da rotina de trabalho
    """
    print("\n🚀 Iniciando Rotina Completa...")
    print("-" * 60)
    
    # Lista com todos os links (voce pode adicionar/remover aqui)
    links = [
        "https://teams.microsoft.com",
        "https://outlook.office.com/mail/",
        "https://clinica.sgusuite.com.br/agendas",
        "https://portalrh3.unimedjf.coop.br/portalrh/WPortalRH.dll/$/",
        "https://unimedjf-my.sharepoint.com/",
        "https://gemini.google.com/app"
    ]
    
    # Loop = repeticao
    # Para cada link na lista, faz algo
    for i, link in enumerate(links, start=1):
        # enumerate() da o numero da posicao (i) e o valor (link)
        print(f"({i}/{len(links)}) Abrindo: {link}")
        webbrowser.open(link)  # Abre o link no navegador padrao
        time.sleep(1)  # Espera 1 segundo antes de abrir o proximo
    
    print("\n✅ Todas as abas foram abertas!")
    input("\nPressione ENTER para voltar ao menu...")


# ===== FUNCAO: ABRIR APENAS COMUNICACAO =====
def rotina_comunicacao():
    """
    Abre apenas ferramentas de comunicacao
    """
    print("\n📧 Abrindo ferramentas de comunicacao...")
    print("-" * 60)
    
    links_comunicacao = [
        "https://teams.microsoft.com",
        "https://outlook.office.com/mail/"
    ]
    
    for i, link in enumerate(links_comunicacao, start=1):
        print(f"({i}/{len(links_comunicacao)}) Abrindo: {link}")
        webbrowser.open(link)
        time.sleep(1)
    
    print("\n✅ Comunicacao pronta!")
    input("\nPressione ENTER para voltar ao menu...")


# ===== FUNCAO: ABRIR SISTEMAS ADMINISTRATIVOS =====
def rotina_sistemas():
    """
    Abre apenas sistemas administrativos
    """
    print("\n⚙️ Abrindo sistemas administrativos...")
    print("-" * 60)
    
    links_sistemas = [
        "https://clinica.sgusuite.com.br/agendas",
        "https://portalrh3.unimedjf.coop.br/portalrh/WPortalRH.dll/$/"
    ]
    
    for i, link in enumerate(links_sistemas, start=1):
        print(f"({i}/{len(links_sistemas)}) Abrindo: {link}")
        webbrowser.open(link)
        time.sleep(1)
    
    print("\n✅ Sistemas prontos!")
    input("\nPressione ENTER para voltar ao menu...")


# ===== FUNCAO: CONFIGURACOES =====
def configuracoes():
    """
    Menu de configuracoes (aqui voce pode adicionar coisas depois)
    """
    limpar_tela()
    print("=" * 60)
    print("                    CONFIGURACOES")
    print("=" * 60)
    print("\n[Em desenvolvimento] Aqui voce podera:")
    print("  - Adicionar novos links")
    print("  - Remover links")
    print("  - Criar novas rotinas personalizadas")
    print()
    input("Pressione ENTER para voltar...")


# ===== FUNCAO PRINCIPAL (MAIN) =====
def main():
    """
    Funcao principal - e daqui que tudo comeca!
    Loop infinito que so para quando user escolhe sair
    """
    while True:  # Loop infinito (while True = enquanto verdadeiro)
        mostrar_menu()
        
        # input() captura o que o usuario digitar
        escolha = input("Digite sua escolha: ")
        
        # if/elif/else = SE/SENAO SE/SENAO
        if escolha == "1":
            rotina_completa()
        elif escolha == "2":
            rotina_comunicacao()
        elif escolha == "3":
            rotina_sistemas()
        elif escolha == "4":
            configuracoes()
        elif escolha == "5":
            print("\n👋 Ate logo!")
            break  # break sai do loop (encerra o programa)
        else:
            print("\n❌ Opcao invalida! Escolha entre 1 e 5.")
            time.sleep(2)  # Espera 2 segundos pra user ver a mensagem


# ===== EXECUCAO DO PROGRAMA =====
# Esta parte garante que o codigo so roda se voce executar ESTE arquivo
# (nao roda se voce importar ele em outro arquivo)
if __name__ == "__main__":
    main()  # Chama a funcao principal


# ========================================
# CONCEITOS QUE VOCE APRENDEU AQUI:
# ========================================
# 1. VARIAVEIS: escolha, links, i
# 2. FUNCOES: def nome_funcao():
# 3. LISTAS: links = [item1, item2, item3]
# 4. LOOPS: for, while
# 5. CONDICIONAIS: if, elif, else
# 6. BIBLIOTECAS: import
# 7. STRINGS: "texto", f"texto {variavel}"
# 8. COMENTARIOS: # para explicar codigo
# ========================================