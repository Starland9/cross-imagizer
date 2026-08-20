"""Point d'entrée PyInstaller pour Cross-Imagizer.

Ce module est utilisé par PyInstaller pour générer les exécutables
standalone. Il délègue simplement à ``app.main:main``.
"""

from __future__ import annotations

from app.main import main

if __name__ == "__main__":
    raise SystemExit(main())
