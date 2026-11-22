#!/bin/bash
# Gerado na criação das capas (19/11/2026) com o CLI do Higgsfield. Precisa do `higgsfield` logado.
RAIZ="$(cd "$(dirname "$0")/../.." && pwd)"   # raiz do projeto
OUT="${TMPDIR:-/tmp}/dramaflix-capas"; mkdir -p "$OUT"
P=$RAIZ/capas/prompts
O=$OUT
for f in "$P"/*.txt; do
  n=$(basename "$f" .txt)
  ( higgsfield generate create gpt_image_2_5 --prompt "$(cat "$f")" --aspect_ratio 3:4 --resolution 2k --quality xhigh --wait --wait-timeout 20m --json > "$O/$n.json" 2> "$O/$n.err"; echo "done $n exit=$?" ) &
done
wait
echo ALL_DONE
