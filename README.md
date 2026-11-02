# 🎵 YouTube MP3 Downloader, Playlist Manager & Hybrid AI Transcriber (MCP + Agent Skill)

Uma **Agent Skill** e servidor **MCP (Model Context Protocol)** de alta performance para assistentes de IA (**Google Antigravity**, **Claude Code**, **Claude Desktop**, **Cursor**) e uso via linha de comando (**CLI**).

Permite baixar áudios e playlists completas do YouTube em MP3 (com capa e metadados ID3), recortar/juntar faixas e realizar **transcrição híbrida ultrarrápida** (extraindo legendas nativas em ~1s ou usando **Faster-Whisper `int8`** localmente).

> **Créditos e Projeto Original:** Este projeto é uma evolução baseada na skill original criada por [**José Robson (`joserobson/mcp-youtube-transcriber`)**](https://github.com/joserobson/mcp-youtube-transcriber), expandida com arquitetura híbrida de transcrição, suporte a playlists incrementais, metadados ID3 automáticos e otimização de tokens para agentes.

---

## ✨ Diferenciais e Melhorias Técnicas

- ⚡ **Transcrição Híbrida Inteligente (Fast Path → Whisper):** Verifica e extrai legendas nativas/automáticas do YouTube em menos de 2 segundos sem uso de CPU. Caso o vídeo não possua legendas (ou com `--force-whisper`), aciona automaticamente o motor local **Faster-Whisper (`int8`)**, até 4x mais rápido e leve que o Whisper tradicional.
- 📂 **Suporte Nativo a Playlists com Histórico Incremental:** Comando `playlist` dedicado que baixa todas as faixas numeradas (`01 - Título.mp3`), ignora vídeos privados/indisponíveis (`--ignore-errors`) e registra um histórico (`.playlist_archive.txt`) para pular músicas já baixadas em execuções futuras.
- 🎨 **Metadados ID3 e Capa Embutida:** Todos os MP3s são gerados com `--embed-thumbnail` e `--add-metadata`.
- 🛠️ **Zero-Config FFmpeg & Compatibilidade Python 3.13 / 3.14:** Detecta automaticamente o binário embutido via `imageio-ffmpeg` (sem exigir configuração manual no `PATH` do sistema) e inclui suporte a `audioop-lts` para `pydub`.
- 🧠 **Otimizado para Economia de Tokens (Progressive Disclosure):** `SKILL.md` enxuto projetado para consumir o mínimo de tokens no contexto do agente.

---

## 📦 Instalação

```bash
pip install -r requirements.txt
```

> **Dica:** Se você tiver o `Node.js` instalado na máquina, o script o detecta automaticamente para contornar limites de *throttling* (HTTP 429) do YouTube.

---

## 🚀 Como Usar via Linha de Comando (CLI)

### 1. Transcrever Vídeo ou Áudio (Modo Híbrido)
```bash
# Extrai legenda nativa instantaneamente ou usa Faster-Whisper se não houver legenda
python ytmp3.py transcribe "https://youtube.com/watch?v=XYZ" --timestamps -m small -l pt

# Forçar transcrição por IA com Faster-Whisper mesmo se houver legenda
python ytmp3.py transcribe "https://youtube.com/watch?v=XYZ" --force-whisper -m small -l pt
```

### 2. Baixar Vídeo Único em MP3 (com Capa e ID3)
```bash
python ytmp3.py download "https://youtube.com/watch?v=XYZ" -o "minha_musica.mp3"
```

### 3. Baixar Playlist Completa
```bash
python ytmp3.py playlist "https://youtube.com/playlist?list=..." -d "D:/Músicas/MinhaPlaylist"
```

### 4. Cortar ou Juntar Trechos de MP3
```bash
# Cortar trecho específico
python ytmp3.py cut "output/musica.mp3" 0:30 2:45 -o "corte.mp3"

# Baixar + cortar múltiplos trechos + juntar automaticamente
python ytmp3.py auto "https://youtube.com/watch?v=XYZ" 0:00-1:30 4:00-end -o "editado.mp3"
```

---

## 🤖 Como Usar em Agentes de IA

### Como Skill no Google Antigravity / Claude Code
Copie a pasta para o diretório de skills:
- **Antigravity (Global):** `~/.gemini/config/skills/youtube-transcriber`
- **Claude Code (Global):** `~/.claude/skills/youtube-transcriber`

### Como Servidor MCP (Claude Desktop / Cursor / Antigravity)
Adicione ao seu arquivo `mcp_config.json` ou `claude_desktop_config.json`:
```json
{
  "mcpServers": {
    "youtube-transcriber": {
      "command": "python",
      "args": ["/caminho/absoluto/para/youtube-transcriber/mcp_server.py"]
    }
  }
}
```
Ferramentas expostas via MCP:
- `download_youtube_audio`
- `download_youtube_playlist`
- `transcribe_audio`
- `cut_audio`
- `auto_youtube_workflow`

---

## 📄 Licença
MIT License — Livre para usar, modificar e distribuir.
