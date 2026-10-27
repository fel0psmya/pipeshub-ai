import os
import subprocess
import sys
from pathlib import Path

# Configuração, ajuste apenas se necessário.

# Diretório raiz do projeto clonado, os testes vai começar a execução a petir dele. 
PROJETO = "."

# Diretório dos testes detectado automaticamente, mas pode forçar manualmente
# Exemplos: TESTES = "./tests"  ou  TESTES = "./test"
TESTES = "./tests/unit/modules"

# Pasta onde os relatórios serão salvos (não altere)
PASTA = "metrics-before-pytest"

# Detecção automática do diretório de testes
CANDIDATOS = ["tests", "test", "src/tests", "src/test"]

if TESTES is None:
    for candidato in CANDIDATOS:
        if Path(candidato).exists():
            TESTES = candidato
            break

if TESTES is None:
    print("Erro: diretório de testes não encontrado.")
    print(f"Procurado em: {CANDIDATOS}")
    print("Defina manualmente a variável TESTES no script.")
    sys.exit(1)

# Execução
os.makedirs(PASTA, exist_ok=True)

print(f"Projeto : {os.path.abspath(PROJETO)}")
print(f"Testes  : {TESTES}")
print(f"Relatórios em: {PASTA}/")
print()

resultado = subprocess.run(
    [
        sys.executable, "-m", "pytest", TESTES,
        "-v",
        f"--junit-xml={os.path.join(PASTA, 'pytest_antes.xml')}",
        f"--html={os.path.join(PASTA, 'pytest_antes.html')}",
        "--self-contained-html",
        f"--cov={PROJETO}",
        "--cov-branch", 
        f"--cov-report=xml:{os.path.join(PASTA, 'coverage_antes.xml')}",
        f"--cov-report=json:{os.path.join(PASTA, 'coverage_antes.json')}",
        f"--cov-report=html:{os.path.join(PASTA, 'coverage_antes_html')}",
        "--cov-report=term-missing",
    ],
    cwd=PROJETO, 
                 
    text=True,
    encoding="utf-8",
)

print(f"\nExit code: {resultado.returncode}")
print(f"\nArquivos gerados em '{PASTA}':")
print(f"  pytest_antes.xml      → resultados dos testes em XML")
print(f"  pytest_antes.html     → relatório visual dos testes")
print(f"  coverage_antes.xml    → cobertura de código em XML")
print(f"  coverage_antes.json   → cobertura de código em JSON")
print(f"  coverage_antes_html/  → relatório visual de cobertura")
print("\nConcluído.")