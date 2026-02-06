

import customtkinter as ctk  # Tkinter moderno
from tkinter import messagebox
import webbrowser
import time
import threading
import json  # Para salvar configurações em arquivo
import os

# Configuração de aparência do CustomTkinter
ctk.set_appearance_mode("green")  # Modo escuro
ctk.set_default_color_theme("green")  # Tema de cor


# ===== CLASSE PRINCIPAL =====
class LauncherModerno:
    """
    Versão TOP do launcher com interface moderna
    """
    
    def __init__(self, root):
        self.root = root
        self.root.title("Sistemas Unimed")
        self.root.geometry("600x550")
        try:
            self.root.iconbitmap("ss.ico")
        except:
            pass
        
        # Centraliza a janela na tela
        self.centralizar_janela()
        
        # Dicionário com todas as rotinas (mais fácil de gerenciar)
        self.rotinas = {
            "completa": {
                "nome": "Rotina",
                "descricao": "todos os sistemas",
                "programas": [
                    "msteams.exe",
                ],
                "links": [
                "https://clinica.sgusuite.com.br/agendas",
                "https://portalrh3.unimedjf.coop.br/portalrh/WPortalRH.dll/$/",
                "http://10.0.38.100/crm/index.php?codmodulo=146",
                "https://unimedjf-my.sharepoint.com/",
                "https://unimedjuizdefora.syngoo-talk.app/user/agent",
                "https://outlook.office.com/mail/",
                "https://ujf.healthmap.com.br/cusuario",
                "https://sgucardprod.unimedjf.coop.br/autsc2",
                "https://gemini.google.com/app",
                "https://sgucardprod.unimedjf.coop.br/cmagnet/Login.do?type=notLogged&dynaHash=cb160654283d6507671d555692566b7b%22",
                "https://cloud-fedmg.unimedmg.coop.br/nextcloud/apps/onlyoffice/s/PYGD9gM5ELLnsWg?fileId=358621",
                "https://sgucardprod.unimedjf.coop.br/autsc2/Login.do?timeOut=1"
                ],
                "cor": "#00995d"  # Verde
            }
        }
        
        
        # Cria a interface
        self.criar_interface()
    
    
    def centralizar_janela(self):
        """
        Centraliza a janela no meio da tela
        """
        self.root.update_idletasks()  # Atualiza info da janela
        
        # Pega tamanho da tela
        largura_tela = self.root.winfo_screenwidth()
        altura_tela = self.root.winfo_screenheight()
        
        # Pega tamanho da janela
        largura_janela = self.root.winfo_width()
        altura_janela = self.root.winfo_height()
        
        # Calcula posição central
        x = (largura_tela - largura_janela) // 4
        y = (altura_tela - altura_janela) // 4
        
        # Define posição
        self.root.geometry(f"+{x}+{y}")
    
    
    def criar_interface(self):
        """
        Cria todos os elementos da interface moderna
        """
        
        # ===== FRAME PRINCIPAL =====
        main_frame = ctk.CTkFrame(self.root)
        main_frame.pack(fill="both", expand=True, padx=20, pady=20)
        
        
        # ===== CABEÇALHO =====
        header_frame = ctk.CTkFrame(main_frame, fg_color="transparent")
        header_frame.pack(pady=(0, 20), fill="x")
        
        titulo = ctk.CTkLabel(
            header_frame,
            text="Sistemas Unimed",
            font=ctk.CTkFont(size=28, weight="bold")
        )
        titulo.pack()
        
        subtitulo = ctk.CTkLabel(
            header_frame,
            text="Abra suas rotinas de trabalho com um clique",
            font=ctk.CTkFont(size=13),
            text_color="white"
        )
        subtitulo.pack()
        
        # ===== FRAME DE CARDS (BOTÕES) =====
        cards_frame = ctk.CTkFrame(main_frame, fg_color="transparent")
        cards_frame.pack(fill="both", expand=True, pady=10)
        
        # Grid com 2 colunas
        cards_frame.columnconfigure(0, weight=1)
        
        
        # ===== CRIA UM CARD PRA CADA ROTINA =====
        row = 0
        col = 0
        
        for chave, rotina in self.rotinas.items():
            self.criar_card(
                cards_frame, 
                rotina["nome"],
                rotina["descricao"],
                lambda r=rotina: self.executar_rotina(r),
                row, 
                col
            )
            
            # Alterna coluna (0, 1, 0, 1...)
            col += 1
            if col > 1:
                col = 0
                row += 1
        
        
        # ===== BARRA DE STATUS =====
        self.status_label = ctk.CTkLabel(
            main_frame,
            text="✓ Pronto para iniciar",
            font=ctk.CTkFont(size=12),
            text_color="#00995d"
        )
        self.status_label.pack(pady=15)
        
        
        # ===== BARRA DE PROGRESSO =====
        self.progress_bar = ctk.CTkProgressBar(main_frame)
        self.progress_bar.pack(fill="x", pady=(0, 15))
        self.progress_bar.set(0)  # Começa em 0%
        
        
        # ===== BOTÕES INFERIORES =====
        bottom_frame = ctk.CTkFrame(main_frame, fg_color="transparent")
        bottom_frame.pack(fill="x")
    
        
        btn_sair = ctk.CTkButton(
            bottom_frame,
            text="❌ Sair",
            command=self.sair,
            width=140,
            height=35,
            fg_color="#f44336",
            hover_color="#d32f2f"
        )
        btn_sair.pack(side="bottom", padx=5)

        marca_dagua = ctk.CTkLabel(
            main_frame,
            text="© 2026 - Desenvolvido por slm",
            font=ctk.CTkFont(size=10, slant="italic"),
            text_color="gray"
        )
        marca_dagua.pack(side="bottom", pady=5)
    
    
    def criar_card(self, parent, titulo, descricao, comando, row, col):
        """
        Cria um card (botão estilizado) para uma rotina
        
        Parâmetros:
        - parent: onde vai ficar
        - titulo: texto principal
        - descricao: texto secundário
        - comando: função ao clicar
        - row, col: posição no grid
        """
        
        # Frame do card
        card = ctk.CTkFrame(
            parent,
            corner_radius=10,
            fg_color="gray25"
        )
        card.grid(row=row, column=col, padx=10, pady=10, sticky="nsew")
        
        # Título do card
        titulo_label = ctk.CTkLabel(
            card,
            text=titulo,
            font=ctk.CTkFont(size=16, weight="bold")
        )
        titulo_label.pack(pady=(15, 5))
        
        # Descrição
        desc_label = ctk.CTkLabel(
            card,
            text=descricao,
            font=ctk.CTkFont(size=11),
            text_color="gray"
        )
        desc_label.pack(pady=(0, 10))
        
        # Botão de ação
        btn = ctk.CTkButton(
            card,
            text="Iniciar",
            command=comando,
            width=120,
            height=30,
            corner_radius=6
        )
        btn.pack(pady=(0, 15))
    
    
    def executar_rotina(self, rotina):
        """
        Executa uma rotina (abre os links)
        """
        thread = threading.Thread(
            target=self.abrir_links_com_progresso,
            args=(rotina["links"], rotina["nome"])
        )
        thread.start()
    
    
    def abrir_links_com_progresso(self, links, nome):
        """
        Abre links e atualiza barra de progresso
        """
        total = len(links)
        
        # Atualiza status
        self.status_label.configure(
            text=f"Abrindo {nome}...",
            text_color="#FF9800"
        )
        
        # Abre cada link
        for i, link in enumerate(links):
            webbrowser.open(link)
            
            # Atualiza progresso
            progresso = (i + 1) / total
            self.progress_bar.set(progresso)
            
            time.sleep(1.0)
        
        # Finaliza
        self.status_label.configure(
            text=f"✓ {nome} aberta! ({total} abas)",
            text_color="#4CAF50"
        )
        
        # Reseta progresso após 2 segundos
        time.sleep(2)
        self.progress_bar.set(0)
    
    
    def sair(self):
        """
        Fecha o aplicativo
        """
        if messagebox.askyesno("Sair", "Deseja realmente sair?"):
            self.salvar_config()  # Salva antes de fechar
            self.root.quit()


# ===== EXECUÇÃO =====
if __name__ == "__main__":
    root = ctk.CTk()  # Janela CustomTkinter
    app = LauncherModerno(root)
    root.mainloop()


