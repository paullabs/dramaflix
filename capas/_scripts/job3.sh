#!/bin/bash
# Gerado na criação das capas (19/11/2026) com o CLI do Higgsfield. Precisa do `higgsfield` logado.
RAIZ="$(cd "$(dirname "$0")/../.." && pwd)"   # raiz do projeto
OUT="${TMPDIR:-/tmp}/dramaflix-capas"; mkdir -p "$OUT"
# uso: job.sh foto|titulo NOME ASPECT
V=$RAIZ/capas/v3
kind=$1; name=$2; ar=$3
if [ "$kind" = foto ]; then
  higgsfield generate create text2image_soul_v2 --prompt "$(cat $V/prompts-foto/$name.txt)" --aspect_ratio 3:4 --quality 2k --wait --wait-timeout 20m --json > $OUT/foto-$name.json 2> $OUT/foto-$name.err
  dest=$V/fotos/$name
else
  higgsfield generate create gpt_image_2_5 --prompt "$(cat $V/prompts-titulo/$name.txt)" --aspect_ratio $ar --resolution 2k --quality xhigh --background transparent --wait --wait-timeout 20m --json > $OUT/titulo-$name.json 2> $OUT/titulo-$name.err
  dest=$V/titulos/$name
fi
url=$(/usr/bin/python3 -I -c "import json,sys;d=json.load(open(sys.argv[1]));j=d[0] if isinstance(d,list) else d;print(j.get('result_url',''))" $OUT/$kind-$name.json 2>/dev/null)
if [ -n "$url" ]; then ext="${url##*.}"; curl -sS -o "$dest.$ext" "$url" && echo "ok $kind $name"; else echo "FALHOU $kind $name: $(head -c 200 $OUT/$kind-$name.err)"; fi
