# Skybound Peaks

Demo 2D em Pygame criada para a atividade prática. O jogo usa os assets locais de `Mountain Shooter Assets/asset/` e adapta o tema para uma aventura plataforma aérea com tiro lateral.

## Como executar

No Linux, com o `uv`, crie o ambiente e instale as dependências:

```bash
uv venv --python 3.11.9 .venv
uv pip install -r requirements.txt --python .venv/bin/python
```

Ou, usando `pip` diretamente:

```bash
python -m pip install -r requirements.txt
```

Rode o jogo:

```bash
.venv/bin/python main.py
```

No Windows, instale o Python 3.11.x e rode:

```bat
run_windows.bat
```

## Controles

- `A/D` ou setas: mover
- `Espaço`: pular
- `J` ou `Ctrl`: atirar
- `Enter`: iniciar ou reiniciar
- `Esc`: voltar ao menu ou sair

## Objetivo

Derrote todos os inimigos e alcance a bandeira no final de cada fase. A demo tem 2 fases, e a segunda é mais difícil. A derrota acontece ao perder todas as vidas ou cair fora da tela.

## Build para Windows

No Windows, clone ou baixe este repositório, instale o Python 3.11.x e execute:

```bat
build_windows.bat
```

O script instala as dependências, gera `SkyboundPeaks.exe`, copia a pasta `Mountain Shooter Assets/` e cria o arquivo `SkyboundPeaks-Windows.zip` pronto para entrega.

Se aparecer erro com `distutils.msvccompiler`, confira se o comando `py -3.11 --version` funciona. Em Python 3.12+ algumas ferramentas antigas ainda podem falhar porque o `distutils` foi removido da biblioteca padrão.

Se fizer manualmente, mantenha esta estrutura ao lado do executável:

```text
SkyboundPeaks.exe
Mountain Shooter Assets/
  asset/
```

## Preparar para GitHub

Arquivos como `.venv/`, `build/`, `dist/`, `release/` e `.zip` ficam ignorados pelo Git. Suba o código-fonte, os scripts `.bat`, os arquivos `requirements*.txt` e a pasta `Mountain Shooter Assets/`.
