import sys
import os
import subprocess
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("YouTube Transcriber")

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
YTMP3_SCRIPT = os.path.join(BASE_DIR, "ytmp3.py")


def run_cli_command(args: list[str]) -> str:
    """Executa o ytmp3.py e captura a saída."""
    cmd = [sys.executable, YTMP3_SCRIPT] + args
    result = subprocess.run(cmd, capture_output=True, text=True, cwd=BASE_DIR, encoding="utf-8")
    if result.returncode != 0:
        return f"Erro ao executar comando:\n{result.stderr}\n{result.stdout}"
    return f"Sucesso:\n{result.stdout}"


@mcp.tool()
def download_youtube_audio(url: str, output: str = None) -> str:
    """Baixa um vídeo do YouTube em MP3 com capa e metadados ID3."""
    args = ["download", url]
    if output:
        args.extend(["-o", output])
    return run_cli_command(args)


@mcp.tool()
def download_youtube_playlist(url: str, out_dir: str = None, no_archive: bool = False) -> str:
    """Baixa todas as faixas de uma playlist do YouTube em MP3 com histórico incremental."""
    args = ["playlist", url]
    if out_dir:
        args.extend(["-d", out_dir])
    if no_archive:
        args.append("--no-archive")
    return run_cli_command(args)


@mcp.tool()
def transcribe_audio(
    source: str,
    model: str = "small",
    language: str = "pt",
    timestamps: bool = False,
    force_whisper: bool = False,
) -> str:
    """Transcreve vídeo do YouTube (Legenda Nativa instantânea -> Faster-Whisper) ou MP3 local."""
    args = ["transcribe", source, "-m", model, "-l", language]
    if timestamps:
        args.append("--timestamps")
    if force_whisper:
        args.append("--force-whisper")
    return run_cli_command(args)


@mcp.tool()
def cut_audio(input_file: str, start: str, end: str, output: str = None) -> str:
    """Corta um trecho do MP3 entre start e end."""
    args = ["cut", input_file, start, end]
    if output:
        args.extend(["-o", output])
    return run_cli_command(args)


@mcp.tool()
def auto_youtube_workflow(url: str, segments: list[str], output: str = None) -> str:
    """Baixa do YouTube, aplica múltiplos cortes e junta em um único MP3."""
    args = ["auto", url] + segments
    if output:
        args.extend(["-o", output])
    return run_cli_command(args)


if __name__ == "__main__":
    mcp.run(transport="stdio")
