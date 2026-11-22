# Estilos de capa — o que a Netflix faz e como levar para dramas curtos

> Extraído em 19/11/2026. Legenda: **[MEDIDO]** = medido ao vivo nas páginas públicas (Chrome, 1512 px de largura) · **[CAPTURA]** = estimado nas capturas desta pasta (±2 px) · **[PESQ]** = pesquisa pública, com fonte · **[PROPOSTA]** = recomendação nossa, não é regra da Netflix.
> Capturas de referência: `capturas/02-…`, `05-…`, `08-…`, `13-…`.

---

## 1. Os tipos de arte que a Netflix usa

| Tipo (nome interno) | Proporção | Onde aparece | Tem logo/título na arte? | Tamanhos |
|---|---|---|---|---|
| **Boxshot** (capa vertical) | **5:7 (0,714)** | Fileiras do catálogo público, Top 10, "Talvez você também goste", app de TV/celular | Sim (o logo vem aplicado no JPG; existe também a versão sem texto) | Entrega 1142×1600 [PESQ: Quiver]. Exibida em 180×252 (Top 10 da landing), 184×258 (catálogo 1280–1599), 240×336/368 (≥1920), 112×157 e 132×185 (mobile/tablet) [MEDIDO] |
| **SDP** (capa horizontal) | **16:9** | Fileiras da home do assinante (tiles), busca, "Minha lista" | Sim (+ versão sem texto) | Entrega 2560×1440 [PESQ: Quiver]; "title card" 530×298 |
| **Billboard / Story Art** | 16:9 (+ versões esquerda→direita e direita→esquerda) | Hero da home, topo do modal, hero da página de título | **Não**: o logo é sobreposto pela interface | 1920×1080 JPG sem texto [PESQ]. Modal da landing: 667×375 [MEDIDO] |
| **Vertical Billboard** | vertical (~9:16) | Hero do app de celular | Não | — [PESQ] |
| **Logo / Title Treatment** | livre (horizontal ~5,7:1; empilhado ~1,7:1) | Sobre billboard, modal e hero do vídeo | É o próprio logo | PNG. Exige **4 versões**: horizontal e empilhado, cada um em claro e escuro [PESQ]. Exibido: 312×55 no hero do título, 166×100 (empilhado) no modal [MEDIDO] |
| **Title Card Background**, **Short Panel** | 16:9 / painel | Telas de destaque | Não (tom escuro) | — [PESQ] |
| **Still de episódio** | 16:9 | Cards de episódio | Não | Exibido em 307×173 com raio 16 px [MEDIDO] |
| **Character art / Avatar** | livre / quadrado | Kids, ícones de perfil | Não | — [PESQ] |

**O princípio por trás:** a arte é guardada **limpa**. O logo é um arquivo separado, e os selos e faixas são da **interface**, não da arte. A Netflix proíbe que o parceiro entregue arte com logo da Netflix, selos ou elementos de interface. [PESQ: Partner College / Artwork Portal]
**Na prática, na web pública:** os selos chegam **já compostos na imagem** pelo servidor de imagens. Nos cartões não existe HTML de selo; a URL da imagem muda conforme o selo. [MEDIDO]

---

## 2. Anatomia da capa vertical (5:7)

Medidas relativas a uma capa de **184×258 px** [CAPTURA]:

```
┌───────────────────────────┐  raio 12 px (catálogo) / 8 px (Top 10 da landing) / 16 px (app)
│▌N                  ┌────┐ │  ← "N" vermelho: ~14×24 px, ~8 px da borda (≈7,5% da largura)
│▌                   │TOP │ │  ← TOP 10: ~29×38 px, encostado no canto sup. dir. (≈16% da largura)
│                    │ 10 │ │     fundo vermelho, "TOP" pequeno sobre "10" grande, branco, bold
│                    └────┘ │
│        ( rosto / dupla    │  ← 1–2 personagens, rosto grande, expressão forte;
│          protagonista )   │     olhar ou gesto indicando o conflito
│                           │
│   ╔═══════════════════╗   │  ← logo do título: terço inferior (57–79% da altura),
│   ║  LOGO DO TÍTULO   ║   │     ~80–90% da largura, centralizado
│   ╚═══════════════════╝   │
│    ┌─────────────────┐    │  ← faixa de novidade: ~70% da largura × ~22 px, centralizada,
│    │ Nova temporada  │    │     vermelho com texto branco bold (~12–13 px)
│    ├─────────────────┤    │  ← 2ª linha opcional: branco com texto preto ("em breve")
│    │    em breve     │    │     encostada na borda inferior
└────┴─────────────────┴────┘
  Legenda opcional abaixo: 14/21 px, branca, centralizada, até 2 linhas, margem-top 4 px
```

**Faixas de texto vistas ao vivo:** "Nova temporada", "Novos episódios", "Novidade", e "Nova temporada" + "em breve" (faixa dupla). [MEDIDO]
**Vistas em 2025–2026 por terceiros:** "New Episode", "Recently Added", "Leaving Soon", "New Season Coming" e "Highly Rewatched" (estas duas no teste da web de jun/2026). [PESQ: What's on Netflix]

**Selo "N" (originais):** saiu dos *tiles* 16:9 da web entre 9 e 13/10/2025. Continua nas capas verticais, nas telas de destaque e nas páginas de detalhe. [PESQ] Ao vivo, todas as capas verticais públicas ainda têm o "N". [MEDIDO]

---

## 3. Ranking numerado (Top 10, "Em alta")

Medido na landing, 1512 px [MEDIDO]:
- Item da lista: 224 px de largura (padding 8 px 22 px); capa 180×252, raio 8 px, fundo de espera #232323.
- **Número:** 100 px, peso 700, preenchimento **#414141**, contorno `-webkit-text-stroke: 4px #fff`. Posição absoluta `left: -22px; bottom: 0`: invade a margem e **sobrepõe o canto inferior esquerdo da capa**.
- **Hover:** `transform: scale(1.05)` em 200 ms ease-in-out. Clicar abre o modal do título.
- **Seta "Próximo":** 24×120 px, `rgba(255,255,255,.1)`, raio 8 px, chevron, aparece com transição de opacidade de 400 ms.

Na **TV** [REF: imagem enviada], a fileira "Trending Now" usa capas verticais 2:3 sem número, cerca de 8 por tela.

---

## 4. O que faz uma capa performar (pesquisa publicada pela Netflix)

[PESQ] Fontes: Netflix "The Power of a Picture" (2016), Tech Blog "Artwork Personalization" (2017), AVA (2018), "Causal ML for Creative Insights" (2023) e arXiv 2601.02764 (2026). Os links estão na seção 8.

1. **A arte decide.** Ela recebe mais de 82% da atenção de quem navega. O usuário olha cada capa por ~1,8 s e desiste de escolher em ~90 s.
2. **Rosto com emoção complexa** vence rosto neutro ou sorriso genérico.
3. **Vilões e personagens polêmicos** rendem mais.
4. **No máximo 3 pessoas.** Mais que isso vira ruído em tamanho pequeno.
5. **Título legível em tamanho pequeno.** Evitar fonte fina e composição complexa.
6. **Personalização:** cada perfil vê a arte que combina com o seu gosto. Para quem vê romance, o casal; para quem vê comédia, o comediante. Fãs de romance respondem a calor emocional; fãs de ação, a cenas intensas.
7. **Teste A/B por "take rate"** (reproduções ÷ exibições). A melhor arte chegou a +14% num título.
8. **Seleção automática de quadros (AVA):** prioriza protagonistas, olhos abertos, foco nítido, boca fechada, regra dos terços e variedade de enquadramento.

**Regras de conteúdo** (princípio "Living Room Friendly") [PESQ]:
- Sem sangue ou ferimento.
- Sem arma apontada para alguém.
- Sem símbolo de ódio.
- Sem nudez ou insinuação explícita.
- Sem menor com álcool ou droga.
- Sem padrão piscante.
- Sem chamada para site externo.
- Palavrão censurado.

---

## 5. Como a Netflix monta a capa no produto

```
arte limpa (JPG)  +  logo (PNG claro/escuro)  +  selos da interface  →  capa exibida
     │                       │                         │
  varia por perfil      escolhe a versão          Top 10 (rank diário), N (original),
  (personalização)      pelo fundo                faixas de novidade (data de lançamento)
```

---

## 6. Capas para a nossa plataforma de dramas curtos [PROPOSTA]

### 6.0 O que a referência de dramas curtos mostra [REF: imagens enviadas]
O usuário enviou duas capturas da vitrine web do DramaBox, salvas em `capturas/referencias-usuario/`. É o "padrão do gênero" que as nossas capas precisam atingir:
- **Proporção 3:4** (≈308×410 px na captura), raio ≈8 px, 6 capas por linha no desktop.
- **Contador "▶ N Episódios"** no canto inferior esquerdo: ícone de play num círculo + texto branco ≈14–16 px, sobre um degradê escuro suave na base. **É interface, não arte**: o número muda com o catálogo.
- **Selo de exclusividade da plataforma** (logo + "Exclusivo") logo acima do título, só em algumas capas.
- **Título enorme no terço inferior**: ≈80–95% da largura, 2–3 linhas.
  - Tipografia **mista** na mesma capa: script caligráfica + serifada ou condensada bold.
  - A palavra-chave do tropo ganha outra cor ou outra fonte.
  - Contorno, brilho, dourado ou sombra separam o título do fundo.
  - Comparado à Netflix, o título é maior, mais saturado e com mais efeito.
- **Elenco e cena:**
  - 1 a 4 pessoas, em pose de tensão romântica ou de poder (terno, vestido de gala, joias, anel, dinheiro voando).
  - Cenário de luxo, noturno ou de fantasia.
  - Os rostos ficam no terço superior e médio, para não disputar espaço com o título.
- **Legenda fora da arte:** título completo abaixo da capa, até 2 linhas (≈16–18 px).
- **Fileira:** título à esquerda ("Tendências") e link "Mais ›" à direita.
- **Tropos que aparecem nos títulos:** realeza ou família poderosa, bilionário e contrato, segunda chance/arrependimento, chefe frio, triângulo com o irmão errado, traição, fantasia/imortal, lobisomem, "chefona", namoro de mentira com inimigo rico.

### 6.1 Proporções
| Uso | Proporção | Tamanho de entrega | Observação |
|---|---|---|---|
| **Capa de fileira** (catálogo, ranking, busca) | **3:4** | 1080×1440 | Equilíbrio entre o 5:7 da Netflix e o vertical do gênero. Cabe 2,3 por linha no celular e 6–7 no desktop |
| **Pôster do feed / player** | **9:16** | 1080×1920, **sem texto** | Fundo do player vertical e do feed estilo "Clips" |
| **Billboard desktop/TV** | 16:9 | 1920×1080, **sem texto** | Personagens à direita, área livre à esquerda para logo e texto (como na imagem de TV) |
| **Logo do título** | livre | PNG transparente, claro e escuro | Horizontal e empilhado (4 arquivos), igual à Netflix |
| **Still de episódio** | 9:16 (recorte 3:4) | quadro do próprio episódio | Na grade de episódios e no "continuar assistindo" |

### 6.2 Anatomia da capa 3:4 de drama curto
```
┌────────────────────────┐
│ [GRÁTIS 1–10]   [#3🔥] │ ← zona de selos: 14% × 14% em cada canto superior
│                        │
│   protagonistas em     │ ← casal ou protagonista em close, emoção do tropo
│   close (1–2 rostos)   │    (ciúme, choque, desafio), no máximo 3 pessoas
│                        │
│  ███ TÍTULO GRANDE ███ │ ← título em fonte display, 2 linhas no máx.,
│  ███   DISPLAY     ███ │    nos 35% inferiores
│ [CEO] [Vingança]  80ep │ ← linha de tropos + nº de episódios (overlay da UI)
└────────────────────────┘
```
- **Selos como overlay HTML/CSS**, não queimados na arte. Assim dá para trocar "Novo", "Em alta #3", "Grátis 1–10", "Dublado", "Exclusivo", "Último episódio hoje" e "Sai em breve" sem gerar arte nova. Se o CDN suportar, componha no servidor, como a Netflix.
- **Faixa inferior** (estilo Netflix): ~70% da largura, vermelho/cor de ação, texto bold 12–13 px. Para estados de novidade: "Novos episódios", "Temporada 2".
- **Ranking numerado:** use o mesmo padrão do Top 10 (número grande com contorno, sobrepondo o canto inferior esquerdo) na fileira "Em alta hoje".
- **Tropos** viram tags de metadados ("Esta série é…" na Netflix): CEO, Casamento por contrato, Vingança, Identidade secreta, Do ódio ao amor, Segunda chance.
- **Personalização desde o início:** guarde 2–4 artes por título, com foco diferente (casal, vilã, cena de choque), e meça o *take rate* por arte.

### 6.3 Pacote mínimo de arte por título
1. `capa_3x4_com-titulo.jpg` (1080×1440)
2. `capa_3x4_sem-texto.jpg` (1080×1440)
3. `poster_9x16_sem-texto.jpg` (1080×1920)
4. `billboard_16x9_sem-texto.jpg` (1920×1080), com personagens à direita
5. `logo_horizontal_claro.png` / `logo_horizontal_escuro.png`
6. `logo_empilhado_claro.png` / `logo_empilhado_escuro.png`
7. `trailer_9x16.mp4` (15–30 s) para o hover e o hero
8. Still 9:16 de cada episódio, tirado do próprio vídeo

> Nomes no padrão `tipo_proporcao_variante_idioma` (a Netflix usa, por exemplo, `sdp_na_01_en` e `logo-horizontal_dark_01_es`). [PESQ]

---

## 7. O que não copiar
- **Artes e logos dos títulos da Netflix:** são de terceiros (estúdios e Netflix). Servem só de referência visual interna.
- **O "N", o wordmark e o vermelho #E50914 como identidade:** crie selo e cor próprios. O selo "original" da nossa marca pode seguir a mesma lógica (canto superior esquerdo, ~7,5% da largura).

---

## 8. Fontes (pesquisa pública)
- Netflix, The Power of a Picture (2016): https://about.netflix.com/en/news/the-power-of-a-picture
- Top 10 (2020): https://about.netflix.com/en/news/see-whats-popular-on-netflix
- Partner College, Artwork Portal e glossário (trechos indexados): https://partnercollege.netflix.net/en/licensed/artwork-portal/ · https://partnercollege.netflix.net/th_TH/partnership/getting-started/netflix-lingo/
- Quiver Digital, especificações de entrega (antigas): https://support.quiverdigital.com/hc/en-us/articles/220024787-What-Is-Artwork-V3
- Regras de conteúdo da arte (resumo, dez/2024): https://www.whats-on-netflix.com/news/what-can-and-cant-go-in-netflix-artwork-or-thumbnails/
- Remoção do "N" dos tiles (out/2025): https://www.whats-on-netflix.com/news/netflix-removes-netflix-original-branding-label-from-tiles-on-web/
- Personalização de arte (resumo de 2017): https://www.itsnicethat.com/news/netflix-personalises-artwork-to-viewing-habits-181217
- AVA (resumo de 2018): https://gigazine.net/gsc_news/en/20180905-netflix-art-science-image-discovery/
- Causal ML for Creative Insights (2023, espelho): https://noise.getoto.net/2023/11/25/causal-machine-learning-for-creative-insights/
- Personalização com LLM (2026): https://arxiv.org/abs/2601.02764
- Boas práticas de key art (deck PBS, 2023): https://pbsdistribution.org/wp-content/uploads/2024/08/KeyArt_BestPractices_Deck_121423_Docs.pdf
