from PyQt6.QtWidgets import QFrame, QVBoxLayout, QHBoxLayout, QLabel, QTextEdit, QPushButton
from PyQt6.QtCore import Qt
from cryos.styles import POLARIS_STYLES

CRYSTAL_ASCII_ART = r"""
       /\           
      /  \          
     /    \  ____   
    /  /\  \/    \  
   /  /  \          
  (  (    \        
   \  \    \  /\   
    \__\    \/  \  
"""

class CryTerminal(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("TerminalWindow")
        self.setStyleSheet(POLARIS_STYLES)
        self.resize(520, 320)
        
        self.init_ui()
        
    def init_ui(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(12, 10, 12, 12)
        
        # Title bar
        tb_layout = QHBoxLayout()
        tb_layout.setSpacing(6)
        
        btn_close = QPushButton()
        btn_close.setObjectName("BtnClose")
        btn_close.setFixedSize(12, 12)
        
        btn_min = QPushButton()
        btn_min.setObjectName("BtnMin")
        btn_min.setFixedSize(12, 12)
        
        btn_max = QPushButton()
        btn_max.setObjectName("BtnMax")
        btn_max.setFixedSize(12, 12)
        
        tb_layout.addWidget(btn_close)
        tb_layout.addWidget(btn_min)
        tb_layout.addWidget(btn_max)
        
        title = QLabel("cryos@polaris ~")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setStyleSheet("font-size: 12px; font-weight: bold; color: #94A3B8;")
        tb_layout.addWidget(title)
        
        add_btn = QLabel("+")
        add_btn.setStyleSheet("color: #64748B; font-weight: bold;")
        tb_layout.addWidget(add_btn)
        
        layout.addLayout(tb_layout)
        
        # Terminal Text
        term_text = QTextEdit()
        term_text.setObjectName("TerminalBody")
        term_text.setReadOnly(True)
        
        neofetch_output = """<span style="color: #38BDF8;">cryos@polaris ~ %</span> neofetch

<table border="0" cellspacing="0" cellpadding="0">
<tr>
<td style="color: #38BDF8; font-family: monospace; font-size: 11px; padding-right: 15px; vertical-align: top;">
   /\\ <br/>
  /  \\  /\\ <br/>
 /    \\/  \\ <br/>
/  /\\  \\   \\ <br/>
\\  \\/  /   / <br/>
 \\    /\\  / <br/>
  \\  /  \\/ <br/>
   \\/ 
</td>
<td style="color: #E2E8F0; font-family: monospace; font-size: 12px; line-height: 1.4;">
<b style="color: #38BDF8;">cryos@polaris</b><br/>
---------------------<br/>
<b>OS:</b> CryOS 1.0.0 Polaris x86_64<br/>
<b>Host:</b> CryOS Device<br/>
<b>Kernel:</b> 6.6.14-cryos<br/>
<b>Uptime:</b> 2 hours, 35 mins<br/>
<b>Packages:</b> 1542 (cryopkg)<br/>
<b>Shell:</b> zsh 5.9<br/>
<b>Resolution:</b> 1792x1824<br/>
<b>DE:</b> CryOS Shell<br/>
<b>WM:</b> CryOS Quartz<br/>
<b>Theme:</b> CryBlue (Light)<br/>
<b>Icons:</b> CryOS Icons<br/>
<b>Terminal:</b> cryoterm<br/>
<b>CPU:</b> Intel i7-12700H (20) @ 4.70GHz<br/>
<b>GPU:</b> Intel Iris Xe Graphics<br/>
<b>Memory:</b> 6.23GiB / 15.42GiB
</td>
</tr>
</table>

<br/>
<span style="color: #38BDF8;">cryos@polaris ~ %</span> <span style="color: #27C93F;">█</span>
"""
        term_text.setHtml(neofetch_output)
        layout.addWidget(term_text)
