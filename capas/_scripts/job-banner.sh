#!/bin/bash
# Gerado na criação das capas (19/11/2026) com o CLI do Higgsfield. Precisa do `higgsfield` logado.
RAIZ="$(cd "$(dirname "$0")/../.." && pwd)"   # raiz do projeto
OUT="${TMPDIR:-/tmp}/dramaflix-capas"; mkdir -p "$OUT"
B=$RAIZ/capas/banners
name=$1
higgsfield generate create seedream_v5_pro --prompt "$(cat $B/prompts/$name.txt)" --image-references "$RAIZ/$(cat $B/prompts/$name.ref)" --aspect_ratio 16:9 --resolution 2k --wait --wait-timeout 15m --json > $OUT/$name.json 2> $OUT/$name.err
url=$(/usr/bin/python3 -I -c "import json,sys;d=json.load(open(sys.argv[1]));j=d[0] if isinstance(d,list) else d;print(j.get('result_url',''))" $OUT/$name.json 2>/dev/null)
if [ -n "$url" ]; then curl -sS -o "$B/$name.png" "$url" && echo "ok $name"; else echo "FALHOU $name: $(head -c 200 $OUT/$name.err)"; fi
