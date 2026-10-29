# Relatório Final — Refatoração de Test Smells (PipesHub AI)

**Disciplina:** Qualidade de Software (2026.2 - T01) — UFC Quixadá  
**Equipe:**
- Felipe da Silva Maia (514914)
- Guilherme Sousa Barbosa (565684)

> Este repositório é o fork utilizado para o trabalho prático de detecção e refatoração de *test smells* na suíte de testes em Python do projeto open-source **[PipesHub AI](https://github.com/pipeshub-ai/pipeshub-ai)**.  
> *(Para consultar a documentação original do projeto PipesHub, acesse [`README_PIPESHUB.md`](./README_PIPESHUB.md)).*

---

## 🔗 Links Principais da Entrega

| Entregável | Link no Repositório (PDF / Pasta) | Link Externo (Docs / GitHub / Vídeo) |
| :--- | :--- | :--- |
| 📄 **Relatório Final** | [`entrega-qs/Relatorio_Final_QS.pdf`](./entrega-qs/Relatorio_Final_QS.pdf) | [Abrir no Google Docs](https://docs.google.com/document/d/1DbzdGAiFFZWVzYhjxlMnPt0LglWSVOri3F1ksLzAAUU/edit?usp=sharing) |
| 📓 **Diário de Bordo** | [`entrega-qs/Diario_de_Bordo_QS.pdf`](./entrega-qs/Diario_de_Bordo_QS.pdf) | [Abrir no Google Docs](https://docs.google.com/document/d/1wFAyl15ANM5Pgw3hReOcklHiZMC9iuM2SUWGBMmAkcg/edit?usp=sharing) |
| 🎥 **Vídeo de Apresentação** | *(Link externo)* | **[Assistir à Apresentação ](COLE_AQUI_O_LINK_DO_YOUTUBE_OU_DRIVE)** |
| 🚀 **Pull Request Oficial** | [Ver commits das 49 refatorações](https://github.com/pipeshub-ai/pipeshub-ai/pull/4946/commits) | **[PR #4946 em `pipeshub-ai/pipeshub-ai`](https://github.com/pipeshub-ai/pipeshub-ai/pull/4946)** |
| 🔖 **Commit Base (Baseline)** | `93e6bd99a854071f57a8dc5b47ddc3b13f7e2e2d` | [Ver árvore no commit inicial](https://github.com/fel0psmya/pipeshub-ai/tree/93e6bd99a854071f57a8dc5b47ddc3b13f7e2e2d) |

---

## 📂 Onde Encontrar os Testes e as Métricas no Repositório

Como o **PipesHub** possui uma arquitetura monorepo (com serviços em Node.js/TypeScript e backend de IA em Python), toda a suíte de testes analisada e as pastas de métricas geradas antes e depois das refatorações estão localizadas no diretório **[`backend/python/`](./backend/python/)**:

### 1. Código de Teste Refatorado
* **Diretório dos testes unitários:** [`backend/python/tests/unit/modules/`](./backend/python/tests/unit/modules/)
* **Escopo da intervenção:** 49 ocorrências alvo refatoradas (90 *test smells* eliminados no total, considerando o efeito cascata) ao longo de **13 arquivos de teste** distribuídos nos submódulos `parsers/`, `agents/`, `indexing/` e `transformers/`. Nenhum arquivo de produção (`app/`) foi modificado.

### 2. Pastas de Métricas (Antes e Depois)
As extrações brutas (CSVs e relatórios) estão versionadas dentro de [`backend/python/`](./backend/python/):

* **TEMPY (Detecção de Test Smells):**
  * Antes (Baseline): [`backend/python/metrics-before-tempy/`](./backend/python/metrics-before-tempy/)
  * Depois (Pós-refatoração): [`backend/python/metrics-after-tempy/`](./backend/python/metrics-after-tempy/)
* **Pytest (Execução da Suíte e Cobertura):**
  * Antes (Baseline): [`backend/python/metrics-before-pytest/`](./backend/python/metrics-before-pytest/)
  * Depois (Pós-refatoração): [`backend/python/metrics-after-pytest/`](./backend/python/metrics-after-pytest/)
* **Radon (SLOC, Complexidade Ciclomática e Índice de Manutenibilidade):**
  * Antes (Baseline): [`backend/python/metrics-before-radon/`](./backend/python/metrics-before-radon/)
  * Depois (Pós-refatoração): [`backend/python/metrics-after-radon/`](./backend/python/metrics-after-radon/)

---

## 📊 Resumo dos Resultados Obtidos

| Métrica | Antes (Baseline) | Depois (Pós-Refatoração) | Variação |
| :--- | :---: | :---: | :---: |
| **Total de Test Smells (TEMPY — Global)** | 4.201 | 4.111 | **-90 (-2,14%)** |
| **Test Smells em `tests/unit/modules/`** | 596 | 506 | **-90 (-15,10%)** |
| **Testes Coletados (Pytest)** | 7.563 | 7.619 | **+56 casos líquidos** |
| **Testes Aprovados (Passed)** | 7.443 | 7.500 | **+57** |
| **Cobertura Total (%)** | 97,2% | 97,2% | **0,0 p.p.** |
| **SLOC dos Testes (`tests/unit/modules/`)** | 69.136 | 69.131 | **-5 linhas** |
| **CC Média (Padrão Radon / Sem `assert`)** | 2,6808 (1,3176) | 2,6837 (1,3159) | **+0,0029 (-0,0017)** |

---

## 🛠️ Divisão das Refatorações

* **Felipe da Silva Maia:** Refatorações `R01` a `R25` (25 ocorrências em 7 arquivos / 23 commits).
* **Guilherme Sousa Barbosa:** Refatorações `R26` a `R49` (24 ocorrências em 6 arquivos / 24 commits).