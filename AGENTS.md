# Repository Guidelines

## Project Structure & Module Organization

This repository contains assignment material and reusable game assets.

- `Atividade_Pratica.pdf` is the project brief or reference document.
- `Mountain Shooter Assets/asset/` contains image and audio assets for the Mountain Shooter game.
- Sprite and projectile files use entity names, such as `Player1.png`, `Enemy2.png`, and `Player1Shot.png`.
- Background and music files are grouped by screen or level: `MenuBg.png`, `Level1Bg0.png`, `Level2.mp3`.

There is no source code, test directory, or build manifest checked in yet. If code is added, keep it outside the asset package in a top-level directory such as `src/`, with tests in `tests/` or the framework-standard equivalent.

## Build, Test, and Development Commands

No project-specific build or test commands are currently defined. Useful repository checks are:

```bash
find . -maxdepth 3 -type f | sort
```

Lists the current file layout.

```bash
find "Mountain Shooter Assets/asset" -type f | sort
```

Verifies the asset inventory before packaging or importing into an engine.

When adding a build system, document exact local commands here, for example `npm test`, `make build`, or the relevant game engine export command.

## Coding Style & Naming Conventions

Preserve existing asset naming unless there is a coordinated rename in code or engine metadata. Use descriptive PascalCase names for game assets, matching the current pattern: `Level1Bg0.png`, `Enemy1Shot.png`, `ScoreBg.png`.

For new source files, follow the language or engine default formatter. Add `.editorconfig`, formatter settings, or lint rules with the first code contribution.

## Testing Guidelines

There are no automated tests at this stage. For asset-only changes, verify that files open correctly and remain in the expected format (`.png` for images, `.mp3` for audio). For future code, add tests near the implementation or under `tests/`, use names that describe behavior, and document the test command here.

## Commit & Pull Request Guidelines

Git history was not available in this environment, so no existing commit convention could be confirmed. Use short, imperative commit messages such as `Add level 2 background assets` or `Document asset structure`.

Pull requests should include a brief description, the reason for the change, and any manual validation performed. For visual asset changes, include screenshots or before-and-after notes when practical.

## Security & Configuration Tips

Do not commit generated build outputs, local editor settings, or machine-specific configuration. Keep large binary additions intentional, and avoid replacing assets without noting compatibility impacts for projects that import them.
