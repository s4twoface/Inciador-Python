# ========================================
# VERSÃO 2: INTERFACE GRÁFICA COM TKINTER
# ========================================
# Agora com JANELA e BOTÕES de verdade!
# Tkinter já vem instalado com Python

import tkinter as tk  # Biblioteca de interface gráfica
from tkinter import messagebox  # Para mostrar mensagens popup
import webbrowser
import time
import threading  # Para não travar a janela enquanto abre links

# ===== CLASSE PRINCIPAL DO APP =====
class LauncherApp:
    """
    CLASSE = molde para criar objetos
    Aqui dentro tem todas as funções e variáveis do nosso app
    """
    
    def __init__(self, root):
        """
        __init__ = construtor (roda quando você cria o app)
        root = janela principal
        self = referência ao próprio objeto (tipo "eu mesmo")
        """
        self.root = root
        self.root.title("Launcher de Rotinas v2.0")  # Título da janela
        self.root.geometry("500x400")  # Tamanho: largura x altura
        self.root.configure(bg="#2b2b2b")  # Cor de fundo (cinza escuro)
        
        # Impede que janela seja redimensionada
        self.root.resizable(False, False)
        
        # Chama função que cria todos os elementos visuais
        self.criar_interface()
    
    
    def criar_interface(self):
        """
        Cria todos os elementos da janela (título, botões, etc)
        """
        
        # ===== TÍTULO =====
        titulo = tk.Label(
            self.root,  # Onde vai ficar (na janela principal)
            text="🚀 LAUNCHER DE ROTINAS",
            font=("Arial", 20, "bold"),  # Fonte, tamanho, estilo
            bg="#2b2b2b",  # Cor de fundo
            fg="white"  # Cor do texto
        )
        titulo.pack(pady=20)  # pack() coloca na tela, pady=espaço vertical
        
        
        # ===== SUBTÍTULO =====
        subtitulo = tk.Label(
            self.root,
            text="Escolha sua rotina de trabalho",
            font=("Arial", 11),
            bg="#2b2b2b",
            fg="#cccccc"
        )
        subtitulo.pack(pady=5)
        
        
        # ===== FRAME DE BOTÕES =====
        # Frame = container para organizar elementos
        frame_botoes = tk.Frame(self.root, bg="#2b2b2b")
        frame_botoes.pack(pady=20)
        
        
        # ===== BOTÃO 1: ROTINA COMPLETA =====
        btn_completa = tk.Button(
            frame_botoes,
            text="🎯 Rotina Completa",
            command=self.rotina_completa,  # Função que roda ao clicar
            width=20,
            height=2,
            font=("Arial", 11, "bold"),
            bg="#4CAF50",  # Verde
            fg="white",
            cursor="hand2",  # Muda cursor quando passa o mouse
            relief="raised"  # Estilo do botão (raised = elevado)
        )
        btn_completa.pack(pady=8)
        
        
        # ===== BOTÃO 2: COMUNICAÇÃO =====
        btn_comunicacao = tk.Button(
            frame_botoes,
            text="📧 Apenas Comunicação",
            command=self.rotina_comunicacao,
            width=20,
            height=2,
            font=("Arial", 11, "bold"),
            bg="#2196F3",  # Azul
            fg="white",
            cursor="hand2"
        )
        btn_comunicacao.pack(pady=8)
        
        
        # ===== BOTÃO 3: SISTEMAS =====
        btn_sistemas = tk.Button(
            frame_botoes,
            text="⚙️ Apenas Sistemas",
            command=self.rotina_sistemas,
            width=20,
            height=2,
            font=("Arial", 11, "bold"),
            bg="#FF9800",  # Laranja
            fg="white",
            cursor="hand2"
        )
        btn_sistemas.pack(pady=8)
        
        
        # ===== BOTÃO 4: SAIR =====
        btn_sair = tk.Button(
            frame_botoes,
            text="❌ Sair",
            command=self.sair,
            width=20,
            height=1,
            font=("Arial", 10),
            bg="#f44336",  # Vermelho
            fg="white",
            cursor="hand2"
        )
        btn_sair.pack(pady=15)
        
        
        # ===== LABEL DE STATUS =====
        # Esta label vai mostrar o que tá acontecendo
        self.label_status = tk.Label(
            self.root,
            text="Pronto para iniciar!",
            font=("Arial", 9),
            bg="#2b2b2b",
            fg="#4CAF50"
        )
        self.label_status.pack(pady=10)
    
    
    def abrir_links(self, links, nome_rotina):
        """
        Função genérica que abre uma lista de links
        
        Parâmetros:
        - links: lista com URLs
        - nome_rotina: nome pra mostrar no status
        """
        
        # Atualiza o texto de status
        self.label_status.config(
            text=f"Abrindo {nome_rotina}...",
            fg="#FF9800"  # Laranja = processando
        )
        
        # Loop pelos links
        for i, link in enumerate(links, start=1):
            webbrowser.open(link)
            time.sleep(0.5)  # Pequena pausa
        
        # Atualiza status quando terminar
        self.label_status.config(
            text=f"✅ {nome_rotina} aberta com sucesso!",
            fg="#4CAF50"  # Verde = sucesso
        )
        
        # Mostra popup de confirmação
        messagebox.showinfo(
            "Sucesso!",
            f"{nome_rotina} foi aberta!\n\n"
            f"Total de abas: {len(links)}"
        )
    
    
    def rotina_completa(self):
        """
        Abre rotina completa em uma thread separada
        Thread = execução paralela (não trava a janela)
        """
        links = [
            "https://teams.microsoft.com",
            "https://outlook.office.com/mail/",
            "https://clinica.sgusuite.com.br/agendas",
            "https://portalrh3.unimedjf.coop.br/portalrh/WPortalRH.dll/$/",
            "https://unimedjf-my.sharepoint.com/",
            "https://gemini.google.com/app"
        ]
        
        # threading.Thread cria uma execução paralela
        thread = threading.Thread(
            target=self.abrir_links,  # Função que vai rodar
            args=(links, "Rotina Completa")  # Argumentos da função
        )
        thread.start()  # Inicia a thread
    
    
    def rotina_comunicacao(self):
        """Abre apenas comunicação"""
        links = [
            "https://teams.microsoft.com",
            "https://outlook.office.com/mail/"
        ]
        
        thread = threading.Thread(
            target=self.abrir_links,
            args=(links, "Comunicação")
        )
        thread.start()
    
    
    def rotina_sistemas(self):
        """Abre apenas sistemas administrativos"""
        links = [
            "https://clinica.sgusuite.com.br/agendas",
            "https://portalrh3.unimedjf.coop.br/portalrh/WPortalRH.dll/$/"
        ]
        
        thread = threading.Thread(
            target=self.abrir_links,
            args=(links, "Sistemas Administrativos")
        )
        thread.start()
    
    
    def sair(self):
        """
        Fecha o aplicativo
        Pergunta antes se user tem certeza
        """
        resposta = messagebox.askyesno(
            "Confirmar",
            "Tem certeza que deseja sair?"
        )
        
        if resposta:  # Se clicou "Sim"
            self.root.quit()  # Fecha a janela


# ===== EXECUÇÃO DO PROGRAMA =====
if __name__ == "__main__":
    root = tk.Tk()  # Cria a janela principal
    app = LauncherApp(root)  # Cria o app dentro da janela
    root.mainloop()  # Loop principal (mantém janela aberta)


# ========================================
# NOVOS CONCEITOS DESTA VERSÃO:
# ========================================
# 1. CLASSES: class Nome:
# 2. MÉTODOS: funções dentro de classes
# 3. self: referência ao próprio objeto
# 4. __init__: construtor da classe
# 5. TKINTER: biblioteca de interface gráfica
#    - Label: texto
#    - Button: botão
#    - Frame: container
#    - pack(): posicionar elementos
# 6. THREADING: executar código em paralelo
# 7. MESSAGEBOX: janelas popup
# 8. LAMBDA: funções anônimas (não usamos aqui mas é importante)
# ========================================
