# Especificação de referência — Netflix web (novembro de 2026)

Documento-base para recriar a experiência da Netflix numa plataforma de **dramas curtos**.
Extração feita em **19/11/2026**: Chrome real ao vivo (viewport 1512×862, DPR 2) + Chrome sem interface e deslogado, via puppeteer, em 393, 768, 1280 e 1920 px de largura.

Arquivos irmãos: [`tokens.css`](tokens.css) e [`tokens.json`](tokens.json) (valores prontos para código), [`CAPAS.md`](CAPAS.md) (estilos de capa), [`capturas/`](capturas/) (screenshots), [`dados/`](dados/) (notas brutas e métricas).

## Legenda de confiança (vale para o documento todo)

| Marca | O que significa |
|---|---|
| **[MEDIDO]** | Lido ao vivo com `getComputedStyle` ou com as variáveis do design system da Netflix (prefixo `--hcw-`, "Hawkins"). É o valor real em 19/11/2026. |
| **[REF-TV]** | Estimado a partir da imagem de referência da interface de TV enviada pelo usuário. São proporções, não pixels exatos. |
| **[REF-MOBILE]** | Estimado a partir do mockup mobile enviado pelo usuário (layout de um designer terceiro, @bigmike_eneji, baseado no app). |
| **[PESQUISA]** | Vem do relatório de pesquisa em fontes públicas, quase sempre secundárias (imprensa, fornecedores). As URLs estão na seção 12. |
| **[CLÁSSICO]** | Layout de assinante conhecido até 2025, **não medido hoje**. Valores aproximados (≈). |

> **Limitação principal:** a conta usada no Chrome está logada, mas **sem plano ativo**. `/browse` redireciona para a landing com o botão "Concluir cadastro". Por isso, a área de assinante (home com fileiras, card de hover, modal completo, perfis, busca e player) **não foi medida ao vivo**. Ela está documentada a partir das duas imagens do usuário, da pesquisa e do layout clássico. A seção 11 diz como fechar essa lacuna.

---

## 0. A "cara" da Netflix em 10 regras

1. **Fundo preto ou quase preto.** A cor vem do conteúdo: arte, trailer e brilho ambiente.
2. **A arte manda.** O topo é um hero ou billboard gigante com trailer em autoplay mudo. No lugar do título em texto entra o **logo do título** (PNG).
3. **Fileiras horizontais de capas.** Título da fileira à esquerda, rolagem lateral, setas em pílula.
4. **Uma cor de ação só.** O vermelho fica restrito ao CTA de cadastro e conversão. Dentro do produto, "Assistir" é **branco com texto preto**.
5. **Uma família tipográfica grotesca**, em 400/500/700/900. Títulos com entrelinha 1,25; corpo com 1,5.
6. **Cantos em três níveis:** 4px em botões retangulares, chips e campos; 8–16px em cartões e capas; pílula nos CTAs novos e na navegação.
7. **Vidro sobre brilho ambiente:** painéis `rgba(255,255,255,.10)` com borda 2px `rgba(255,255,255,.04)`, sobre uma cópia borrada da arte do título.
8. **Movimento curto:** 200–250ms. Curva de saída `cubic-bezier(.4,0,.68,.06)`, de entrada e hover `cubic-bezier(.32,.94,.6,1)`.
9. **Selos por cima da arte** (Top 10, "Nova temporada", "N"). A arte em si não leva texto além do logo do título.
10. **Breakpoints 600/960/1280/1600/1920/2560.** Quanto mais largo, mais capas por fileira: 2 → 5 → 6.

---

## 1. Mapa do site

| Página | URL | Acesso | Status nesta extração |
|---|---|---|---|
| Landing (deslogado) | `/br/` | público | **[MEDIDO]** desktop + 4 larguras |
| Login (email primeiro) | `/br/login` | público | **[MEDIDO]** |
| Modal de título da landing | clique numa capa do "Em alta" | público | **[MEDIDO]** |
| Página de gênero/coleção | `/br/browse/genre/{id}` (ex.: 83 = Séries) | público | **[MEDIDO]** desktop + 4 larguras |
| Página de título | `/br/title/{id}` | público | **[MEDIDO]** desktop + 4 larguras |
| Cadastro/escolha de plano | `/signup/…` | conta sem plano | não aberto: mexeria no estado da conta |
| Quem está assistindo (perfis) | após login | assinante | [REF-MOBILE] + [CLÁSSICO] |
| Home do assinante | `/browse` | assinante | [REF-TV] + [PESQUISA] + [CLÁSSICO] |
| Séries / Filmes / Novidades / Minha lista / Idiomas / Jogos | `/browse/…` | assinante | [CLÁSSICO] + [PESQUISA] |
| Card de hover (mini-modal) e modal de detalhes | sobre a home | assinante | [CLÁSSICO] + [REF-MOBILE] (página de título mobile) |
| Busca | `/search?q=` | assinante | [CLÁSSICO] |
| Player | `/watch/{id}` | assinante | [CLÁSSICO] |
| Hub "What's Hot", aba "AI Discover", feed vertical "Clips" (celular) | — | testes 2026 | [PESQUISA] |

**Fluxo principal:** landing → email → plano → perfis → home → card/modal do título → player → próximo episódio.

---

## 2. Fundamentos visuais (tokens)

Os valores completos estão em `tokens.css` / `tokens.json`. Aqui ficam o resumo e onde cada valor aparece.

### 2.1 Cores

| Papel | Valor | Onde aparece | Fonte |
|---|---|---|---|
| Fundo das páginas públicas | `#000000` | landing, login, catálogo | [MEDIDO] |
| Fundo do app de assinante | `#141414` | home, fileiras | [CLÁSSICO] |
| Superfície do modal | `#161616` | modal de título da landing | [MEDIDO] |
| Placeholder / skeleton | `#232323` ↔ `#414141` | animação `loading` | [MEDIDO] |
| Placeholder de capa | `#262626` / `#353535` | fundo da capa antes da imagem | [MEDIDO] |
| Superfície elevada | `#2D2D2D` | item de FAQ | [MEDIDO] |
| Hover / chip | `#414141` | hover do FAQ, chips do modal, preenchimento do número Top 10 | [MEDIDO] |
| Vidro | `rgba(255,255,255,.10)` + borda 2px `rgba(255,255,255,.04)` | painéis da página de título | [MEDIDO] |
| Véu (scrim) | `rgba(0,0,0,.70)` | fundo atrás do modal, pílula de navegação | [MEDIDO] |
| Campo | `rgba(22,22,22,.70)` + borda `rgba(128,128,128,.70)` | inputs, botões de vídeo | [MEDIDO] |
| Linha fina | `rgba(128,128,128,.40)` | borda do modal | [MEDIDO] |
| Texto | `#FFF` / `.70` / `.50` / `.40` | primário / secundário / legal / desabilitado | [MEDIDO] |
| **Ação (vermelho de referência)** | `#E50914` → hover `#C11119` → pressionado `#99161D` → desabilitado `rgba(229,9,20,.4)` | CTA de cadastro | [MEDIDO] |
| Botão branco | `#FFF` → hover `rgba(255,255,255,.7)` → pressionado `.5` | "Assistir", pílulas brancas | [MEDIDO] |
| Botão cinza | `rgba(128,128,128,.40)` → pressionado `.20` | "Saiba mais", setas | [MEDIDO] |
| "Mais informações" (billboard) | `rgba(109,109,110,.70)` | botão secundário do billboard | [CLÁSSICO]/[REF-TV] |
| Erro / sucesso / aviso | `#EB3942` / `#2BB871` / `#D89D31` | validação de campos | [MEDIDO] |
| Link | `#448EF4` (pressionado `#94C2FF`) | "Ajuda", links de texto | [MEDIDO] |
| Foco | anel 2px sólido branco, offset 2px | todos os controles | [MEDIDO] |

> O par vermelho + preto é parte da identidade da Netflix. Use **outra cor de ação** (seção 10).

### 2.2 Tipografia

- **Família [MEDIDO]:** `"Netflix Sans", "Helvetica Neue", "Segoe UI", Roboto, Ubuntu, sans-serif`. Pesos carregados: 400, 500, 700 e 900. Existem também 100, 300 e uma versão variável 100–900. A Netflix Sans é **proprietária**; substitutas livres de desenho parecido: **Inter**, **Figtree**, **Manrope**.
- Base: 16px no `html`.

| Uso | Tamanho / peso / entrelinha | Fonte |
|---|---|---|
| h1 da landing | 56/700/70 (1280–1919) · 64/700/80 (≥1920) · 32/700/40 (<960) | [MEDIDO] |
| h1 da página de gênero | 48/900 (1280) · 56/900 (≥1920) · 32/700 (768) · 24/500 (393) | [MEDIDO] |
| h1 do login | 32/700 | [MEDIDO] |
| h2 de fileira (catálogo) | 32/700 desktop · 20/500 abaixo de 960 | [MEDIDO] |
| h2 de seção (landing) | 24/500 (1280) · 32/700 (≥1920) · 18/500 (mobile) | [MEDIDO] |
| Título no bloco de metadados | 24/500 | [MEDIDO] |
| Subtítulo do hero da landing | 20/500 | [MEDIDO] |
| Descrição do hero de gênero, botão M | 18/400 e 18/500 | [MEDIDO] |
| Corpo, sinopse, inputs | 16/400, entrelinha 24 | [MEDIDO] |
| Metadados, legenda de capa, links de rodapé, botão P | 14/400–500, entrelinha 21 | [MEDIDO] |
| Selo de duração, texto legal | 13/500 e 13/400 | [MEDIDO] |
| Número do Top 10 | 100/700 | [MEDIDO] |

### 2.3 Espaçamento e grade [MEDIDO]

- Escala usada: 4 · 8 · 12 · 16 · 24 · 32 · 48 · 64.
- **Landing:** container de **1216px** (148px de margem em 1512). Hero com largura máxima de 1920.
- **Catálogo (gênero e título):** margem lateral de 48px (área de 1416px em 1512). As fileiras começam em **152px** (área de 1208px).
- Margem lateral no mobile: 24px (<600); no tablet: 32px (600–959).
- Passo entre capas verticais: **196px** (capa de 184 + 12). No Top 10 da landing: **224px** (capa de 180 + padding 8/22).
- Distância vertical entre fileiras no catálogo: ≈400px de topo a topo (fileira de 368 + 32).

### 2.4 Breakpoints [MEDIDO]

| Nome | Faixa | Observação |
|---|---|---|
| xs | < 600 | mobile: formulário empilhado, 2 capas visíveis, header com só o "N" nas páginas de catálogo |
| s | ≥ 600 | tablet |
| m | ≥ 960 | header cresce (80→88 na landing, 56→72 no catálogo) e o h1 da landing vai de 32 para 56 |
| l | ≥ 1280 | desktop padrão |
| xl | ≥ 1600 | |
| xxl | ≥ 1920 | h1 64/80, capas maiores (240px de largura), 6 visíveis |
| xxxl | ≥ 2560 | |

Componentes antigos ainda usam 400 · 425 · 550 · 740 · 768 · 896 · 1024. Existe media query para `prefers-reduced-motion`.

### 2.5 Raios [MEDIDO]

2px (foco de link) · **4px** (botões retangulares, chips, inputs, selo de duração) · **8px** (capas do Top 10 da landing, modal, seta da landing) · **12px** (capas verticais do catálogo) · **16px** (painéis de vidro, cards de episódio, planos, banners) · **100px** (pílulas) · 50% (círculos).

### 2.6 Sombras, desfoques e gradientes [MEDIDO]

- Sombra do modal: `0 4px 8px rgba(0,0,0,.8)`. Sombra da pílula flutuante: `8px 8px 16px rgba(0,0,0,.5)`.
- Desfoque: pílula de navegação `blur(12px)` · cartões de motivos `blur(30px)` · fundo ambiente `blur(32px)` com opacidade .15.
- **Véu do hero da landing:** `linear-gradient(7deg, rgba(0,0,0,.85) 10% … rgba(0,0,0,.6) 97%)`, com 13 paradas suavizadas (completo em `tokens.css`).
- **Header do catálogo:** `linear-gradient(to top, transparente, #000)`.
- **"A curva"** sob o hero da landing: linha de 4px em meia-elipse, `linear-gradient(to right, #210d16 16%, #b82869, #e50914, #b82869, #210d16 84%)`, com brilho azul radial abaixo.
- Cartões "Mais motivos": `linear-gradient(149deg, #192247 0%, #210e17 96.86%)`.
- Banner promocional: `linear-gradient(91deg, #482566 0%, #161d52 99.51%)`.
- Planos: azul `#1c4072 → #172b47 → #120c1f`, roxo `#59216e → #251743 → #120c1f`, vinho `#6c1e41 → #251743 → #120c1f`, todos a 149°.
- **Fundo ambiente:** a arte do título em `<img>` fixa, `filter: blur(32px)`, `opacity: .15`, `mask-image: linear-gradient(#d9d9d9 78.62%, transparente 100%)`.

### 2.7 Movimento [MEDIDO]

| Token | Valor | Uso |
|---|---|---|
| Saída/padrão | `cubic-bezier(.4,0,.68,.06)` | fundo de botões, label de input, cabeçalho do acordeão |
| Entrada/ênfase | `cubic-bezier(.32,.94,.6,1)` | hover de botão, painel do acordeão, modal |
| 200ms ease-in-out | | escala da capa no hover (1,05) e setas |
| 250ms | | botões, inputs, acordeão, fundo do modal |
| 300–400ms | | troca imagem→vídeo no hero (crossfade de opacidade) |
| 533ms | | `transform` de entrada do modal; a opacidade leva 100ms com 100ms de atraso |
| 1000ms ease-in-out | | CTA flutuante entrando (transição de `bottom`) |
| Pressionado | 0ms | resposta imediata ao toque |

### 2.8 Camadas (z-index) [MEDIDO]

CTA flutuante 3 · header 20 · modal 1000 · toasts 1002.

### 2.9 Ícones

Traço fino com cantos arredondados, em 16, 24 e 72px (ilustrações dos motivos), sempre em `currentColor`. Chevron "›" nos links de fileira e nas setas; ícone de tradução no seletor de idioma; play, pausa, som, tela cheia e legendas nos controles de vídeo. **Desenhe os seus ou use uma biblioteca livre** (Lucide, Phosphor).

---

## 3. Componentes

### 3.1 Header da landing [MEDIDO]
- Altura 88px (80px abaixo de 960). Fica sobre o hero, sem fundo próprio.
- Logo (wordmark vermelho) 148×40 a 24px do topo.
- À direita: **seletor de idioma** 146×32 (borda 1px cinza translúcida, ícone de tradução à esquerda, seta à direita, padding 6/36/6/34, 16px; no mobile vira só ícone + seta) e botão **"Entrar"** vermelho P (72×32, 14/500, raio 4).

### 3.2 Header das páginas de catálogo [MEDIDO]
- Altura 72px (56px abaixo de 960), z 20, fundo `linear-gradient(to top, transparente, #000)`.
- Logo SVG 147×40 a 48px da esquerda. **No mobile e no tablet o wordmark vira só o símbolo "N", em 18×32.**
- Botão pílula branco à direita: "Entrar" quando deslogado, "Sair" quando logado sem plano. 14/500, preto, padding 4/16, altura 32, raio 100.

### 3.3 Header do assinante [CLÁSSICO] (não medido)
- ≈68px, padding lateral 4%. Começa com degradê `rgba(0,0,0,.7) → transparente` e fica sólido `#141414` ao rolar (transição ≈.4s).
- Logo à esquerda. Navegação principal (Início, Séries, Filmes, Bombando, Minha lista, Navegar por idiomas): 14px `#E5E5E5`, ativo em branco e negrito, vira um menu "Navegar" abaixo de ≈885px.
- À direita: busca (o ícone abre um campo preto com borda branca), "Infantil", sino com contador vermelho, avatar 32×32 (raio 4) com seta que gira 180° no hover. O menu do perfil tem fundo `rgba(0,0,0,.9)` e borda 1px `rgba(255,255,255,.15)`.
- **Na TV [REF-TV]** não há barra no topo: a navegação é um **trilho de ícones à esquerda** (seção 4.6.1). A pesquisa diz que a TV trocou o trilho por atalhos no topo em maio/2025 e testa a volta do trilho expansível desde 03/11/2026 [PESQUISA].

### 3.4 Botões
| Variante | Medidas | Fonte |
|---|---|---|
| Primário vermelho P | 32px de altura, padding 4/16, 14/500, raio 4 | [MEDIDO] |
| Primário vermelho M | 48px, padding 8/16, 18/500, raio 4 ("Continuar", CTA do modal) | [MEDIDO] |
| Primário vermelho G | 56px, padding 12/24, 24/500 + chevron 24, raio 4 ("Vamos lá ›") | [MEDIDO] |
| Pílula vermelha | 48px, 240px de largura, padding 6/32, 16/500, raio 100 ("Concluir cadastro", "Acessar agora"); 200×40 no mobile | [MEDIDO] |
| Pílula branca | 32px, padding 4/16, 14/500, texto preto ("Sair", "Entrar") | [MEDIDO] |
| Pílula escura com borda | 32px, fundo `rgba(22,22,22,.7)`, 14/500 ("Mais sobre a Netflix") | [MEDIDO] |
| Secundário cinza | 40px, padding 6/16, 16/500, `rgba(128,128,128,.4)`, raio 4 ("Saiba mais") | [MEDIDO] |
| **Assistir (billboard)** | branco, texto preto, ícone ▶, raio 4, 132×50 na imagem de TV (≈181×68 em 1080p) | [REF-TV]/[CLÁSSICO] |
| **Mais informações (billboard)** | `rgba(109,109,110,.7)`, texto branco, raio 4; ≈149×50 na imagem de TV; hover `.4` | [REF-TV]/[CLÁSSICO] |
| Botão-ícone | 32×32 (raio 16) ou 40×40 (raio 20); transparente → hover `rgba(128,128,128,.4)` → pressionado `.2` | [MEDIDO] |
| Controle de vídeo | círculo de 40px, fundo `rgba(22,22,22,.7)`, borda 1px `rgba(128,128,128,.7)`, ícone 24, espaço de 12 entre eles | [MEDIDO] |
| Seta de fileira (catálogo) | pílula vertical 24×80, `rgba(128,128,128,.4)`, raio 256, chevron 24, transição .2s | [MEDIDO] |
| Seta de fileira (landing) | 24×120, `rgba(255,255,255,.1)`, raio 8, ícone `.7`, transição de opacidade .4s | [MEDIDO] |

Todos usam transição de `background-color` em 250ms `cubic-bezier(.4,0,.68,.06)`; o hover usa a curva de entrada.

### 3.5 Campo de texto [MEDIDO]
- **Retangular** (landing, login): 56px de altura (48 no mobile), padding 24/16/8, fundo `rgba(22,22,22,.7)`, borda 1px `rgba(128,128,128,.7)`, raio 4.
- O label flutua de 16px para 12px dentro do campo (transição de 250ms em top, font-size e line-height).
- Descrição e mensagens em 13px. Estados de erro, sucesso e aviso trocam a cor da borda e do texto.
- **Pílula** (variante deslogada do catálogo): campo "Email" em pílula com borda clara, logo acima do CTA pílula "Acessar agora" (visto em 393/768/1280/1920 deslogado).

### 3.6 Hero e billboard
| Tipo | Anatomia | Fonte |
|---|---|---|
| **Landing** | 100vh (858px em 1512; 808 em 1280; 996 em 1920; 664 no mobile). Imagem única com colagem de capas 16:9 inclinadas (`object-fit: cover`), véu de 7°. Texto centralizado: h1, subtítulo, h3 do formulário e formulário inline (input 396×56 + CTA 184×56, 8px de espaço; empilhado no mobile). | [MEDIDO] |
| **Gênero** | Cartão de 1416×678 com cantos arredondados e **base em arco convexo**, colagem inclinada e degradê escuro à esquerda e embaixo. Texto a 64px da borda: h1 48/900, descrição 18px (640px de largura), CTA pílula, legenda 16px. | [MEDIDO] |
| **Título** | Mesmo cartão em arco (1416×659), com `<video>` do trailer em autoplay mudo sobre uma `<picture>` (crossfade de .4s). Logo do título (≈312×55, proporção 5,7:1, `object-fit: contain`) a 56px da esquerda, CTA e legenda abaixo. 4 controles circulares no canto inferior direito. No mobile, o logo e o CTA saem do vídeo e ficam logo abaixo, centralizados. | [MEDIDO] |
| **Assinante (web)** | Billboard em largura total, ≈16:9: imagem de fundo que vira trailer depois de ≈2–3s; degradê lateral `77deg rgba(0,0,0,.6) → transparente 85%` e degradê inferior até `#141414`. Logo do título a 4% da esquerda, sinopse em ≈1,2vw, "Assistir" + "Mais informações". À direita: botão de som e caixa de classificação etária (borda esquerda 3px `#DCDCDC` sobre `rgba(51,51,51,.6)`). Depois que o trailer começa, o logo encolhe e a sinopse some. | [CLÁSSICO] |
| **Assinante (TV)** | Arte em tela cheia, véu escuro à esquerda, rótulo "N SÉRIE", logo grande, sinopse de 4 linhas, 2 botões e a fileira começando a 70% da altura. Detalhes na seção 4.6.1. | [REF-TV] |

### 3.7 "A curva" [MEDIDO]
Divisor logo abaixo do hero da landing: uma meia-elipse larga cuja borda superior de 4px tem degradê horizontal vinho → magenta → vermelho → magenta → vinho, com brilho azul por baixo. Ela separa o hero do resto da página e é a assinatura visual da landing nova.

### 3.8 Fileira (carrossel)
- **Catálogo público [MEDIDO]:** h2 32/700 e, se a fileira tiver página própria, um botão-ícone "›" de 32px ao lado. `ul` em flex com overflow horizontal; cada `li` tem 198px (padding 10,4/6/10,4/8). Seta pílula à direita.
- Capas visíveis por largura: **2** (393) · **5** (768 e 1280) · **6** (1920).
- **Landing "Em alta" [MEDIDO]:** h2 24/500; `li` de 224px; capa vertical com número do ranking; seta 24×120.
- **Assinante [CLÁSSICO]:**
  - Título da fileira em ≈1,4vw/500 `#E5E5E5`, com link "Ver tudo ›" que aparece no hover.
  - Capas 16:9 com ≈0,2vw de espaço.
  - Capas por fileira: 6 (≥1400) · 5 (1100–1399) · 4 (800–1099) · 3 (500–799) · 2 (<500).
  - Setas de 4% da largura, fundo `rgba(20,20,20,.5)`.
  - Indicador de páginas em barrinhas (12×2px) no canto superior direito.
  - Rolagem com ≈.75s de ease.
  - Pelo teste da web de jun/2026 [PESQUISA], os tiles agora têm cantos arredondados.

### 3.9 Cartões de capa
| Cartão | Medidas | Fonte |
|---|---|---|
| Vertical do catálogo | 184×258 (≈5:7), raio 12, placeholder `#262626` (raio 16); legenda 14/21 centralizada, 4px abaixo, até 2 linhas; hover escala 1,05 em .2s. Tamanho por largura: 132×185 (<960) · 184×258 (1280) · 240×336 (≥1920) | [MEDIDO] |
| Vertical do Top 10 (landing) | 180×252, raio 8, fundo `#232323`; número 100/700 com preenchimento `#414141` e contorno branco de 4px (`-webkit-text-stroke`), em `left:-22px; bottom:0`, sobre o canto inferior esquerdo da capa. 112×157 (<960) · 214×300 (≥1920) | [MEDIDO] |
| Episódio (página de título) | 327×364, painel de vidro, padding 8, raio 16. Miniatura 16:9 307×173 (raio 16) com selo de duração no canto inferior direito. Título "1. Episódio 1" 16/500/24; sinopse 14/21 em `.7`, até 5 linhas. 281×333 no mobile | [MEDIDO] |
| Horizontal 16:9 (fileiras do assinante) | ≈16:9, raio ≈4 (arredondado após o refresh de 2026) | [CLÁSSICO]/[PESQUISA] |
| Vertical 2:3 (TV) | ≈155×232 na imagem (≈213×318 em 1080p), espaço ≈8, 7½ visíveis | [REF-TV] |
| Continuar assistindo | 16:9 com barra de progresso de 2–3px, vermelho sobre cinza, na base | [CLÁSSICO] |

### 3.10 Selos (detalhes em `CAPAS.md`)
- "N" de original no canto superior esquerdo; "TOP 10" (quadrado vermelho) no canto superior direito.
- Faixas na base: "Nova temporada", "Novos episódios", "Novidade" e a faixa dupla "Nova temporada / em breve".
- **Classificação etária "A16"**: texto 14/500 na linha de metadados, separado por "•".
- **Duração "48min"**: 13/500, fundo `rgba(0,0,0,.9)`, raio 4, padding 1/12.
- **Chips do modal:** 14/500, padding 3/4, fundo `#414141`, raio 4.
- Nas páginas públicas os selos vêm **queimados na imagem** [MEDIDO]. A regra oficial é que **a interface aplica os selos** e a arte entregue não tem selo [PESQUISA].

### 3.11 Modais
- **Modal de título da landing [MEDIDO]:**
  - Véu `rgba(0,0,0,.7)`, z 1000, centralizado.
  - Diálogo de 669px (largura máxima), fundo `#161616`, borda 1px `rgba(128,128,128,.4)`, raio 8, sombra `0 4px 8px rgba(0,0,0,.8)`, `overflow: hidden`.
  - Hero 16:9 (667×375) com degradê para `#161616` e logo do título (≈166×100) a 40px da esquerda.
  - Botão fechar circular de 40px no canto superior direito.
  - Chips de metadados (ano, classificação, tipo, gênero), sinopse 16px e CTA vermelho M.
  - Entrada: véu 250ms; diálogo com opacidade em 100ms (atraso de 100ms) e transform em 533ms.
- **Card de hover do assinante (mini-modal) [CLÁSSICO]:**
  - Depois de ≈400–500ms em cima da capa, ela cresce ≈1,5× e vira um card `#181818` (raio ≈6, sombra `0 3px 10px rgba(0,0,0,.75)`).
  - Topo 16:9 com prévia em vídeo muda.
  - Botões circulares: ▶ branco cheio, "+" Minha lista, polegar com 3 opções (Não é pra mim / Gostei / Amei!) e "⌄" à direita para abrir o modal.
  - Linha de metadados: relevância % em verde `#46D369` (talvez removida [PESQUISA]), classificação, duração ou temporadas, HD.
  - Tags de gênero separadas por "•".
  - A origem da escala depende da posição: na borda esquerda cresce para a direita, na direita cresce para a esquerda.
- **Modal de detalhes do assinante [CLÁSSICO]:**
  - Largura máxima ≈850px, 2em do topo, fundo `#181818`, raio ≈6.
  - Hero 16:9 com trailer, logo, ▶ Assistir, +, polegar e som.
  - Informações em 2 colunas (2fr/1fr). À esquerda: ano, temporadas, HD/AD, classificação com descritores, "Top 1 em séries hoje" e sinopse. À direita: "Elenco:", "Gêneros:" e "Esta série é:", com rótulos `#777` e valores `#DDD`.
  - **Episódios:** seletor de temporada (fundo `#242424`, borda `#4D4D4D`). Cada linha tem índice em `#D2D2D2`, miniatura 16:9 de ≈130px (raio 4), título em negrito, duração à direita e sinopse 14px. Divisor `#404040`; episódio atual com fundo `#333`.
  - **"Títulos semelhantes":** grade de 3 colunas, cards `#2F2F2F` (raio 4) com imagem, duração, classificação, ano, botão "+" e sinopse.
  - Por fim, "Trailers e mais" e "Sobre {título}".

### 3.12 Painel de vidro e blocos de informação [MEDIDO]
- **Painel:** `rgba(255,255,255,.1)`, borda 2px `rgba(255,255,255,.04)`, raio 16, padding 32/24.
- **Bloco de metadados** (página de título, 1208×189):
  - h2 24/500.
  - Linha 14/500: ano • nº de episódios • classificação • gênero, com "•" cinza feito por pseudo-elemento.
  - Duas colunas: sinopse 16px (≈547px) | divisor vertical 1px | "Elenco:" 14/500 branco + nomes em `.7`.
- **"Mais detalhes":** 3 painéis lado a lado (402×260; empilhados no mobile) com pares rótulo (14/500 branco) e valor (14/500 `.7`): Assista offline, Gêneros, **"Esta série é…" (tags de tom e tropo)**, Áudio, Legendas, Elenco.

### 3.13 Navegação âncora [MEDIDO]
Pílula fixa no topo, centralizada (417×41): fundo `rgba(0,0,0,.7)`, `backdrop-filter: blur(12px)`, raio 100, sombra `8px 8px 16px rgba(0,0,0,.5)`. Itens 14/500 cinza claro: "Episódios · Mais títulos para assistir · Planos". No mobile ocupa a largura toda (393×41) e rola na horizontal.

### 3.14 CTA flutuante [MEDIDO]
Faixa *sticky* de 64px na base da viewport com o CTA pílula vermelho centralizado. Aparece ao rolar (transição de `bottom` em 1s ease-in-out), z 3.

### 3.15 Blocos de venda [MEDIDO]
- **Banner promocional:** ícone 3D de 77px (pipoca) + cartão com degradê roxo→azul (raio 16), h3 20/500, p 16 e botão cinza "Saiba mais".
- **"Mais motivos para assinar":** 4 cartões de 292×310 (empilhados no mobile, 345×197), raio 16, degradê azul-marinho→vinho, `backdrop-filter: blur(30px)`, h3 24/500, p 16 em `.7`, ilustração de 72px no canto inferior direito, 16px de espaço entre cartões.
- **Planos:** h2 32/700 e 3 cartões de 395×221 (empilhados no mobile, 345×169), raio 16, degradês azul, roxo e vinho. Nome 24/500, qualidade 18/500 `.7`, benefícios com ✓ 16 `.7`, preço 18/500 ("R$ 25,90 /mês").
- **Banner "Descubra…":** 1208×104 com colagem ao fundo, texto 24/700 e pílula escura. Faixa Tudum: painel cinza translúcido com ícone e texto 14 `.5`.

### 3.16 FAQ (acordeão) [MEDIDO]
- Item de 1216×84 (72 no mobile), fundo `#2D2D2D`, hover `#414141`. Pergunta 24/400 (18 no mobile), padding 24. Itens separados por 8px; 1px entre pergunta e resposta.
- O ícone "+" gira −45° e vira "×". Painel com o mesmo fundo, transição de 250ms `cubic-bezier(.32,.94,.6,1)`.

### 3.17 Rodapé [MEDIDO]
- Texto `rgba(255,255,255,.7)`.
- "Dúvidas? Ligue para…" em 16px.
- Grade de links em 4 colunas de 25% (2 no mobile), 14/21 e sublinhados.
- Seletor de idioma, nome do país em 14px e aviso do reCAPTCHA em 13px `.5`.

### 3.18 Skeleton [MEDIDO]
Animação `loading`: o fundo vai de `#232323` para `#414141` e volta (0–40% parado, pico em 70%, volta em 90%). Fica nos espaços reservados das capas enquanto as imagens carregam.

---

## 4. Páginas

### 4.1 Login — `capturas/00-login-desktop.jpg` [MEDIDO]
- Header de 88px com o logo.
- Fundo em degradê vinho escuro (topo) → preto, com textura sutil; faixa de rodapé `#161616`.
- Formulário de 440px (coluna de 480):
  - h1 32/700 "Informe seus dados para entrar"; h2 18/400 `.7` "Ou crie uma conta.".
  - Campo "Email ou número de celular" (56px) e botão vermelho M "Continuar" (440×48).
  - "Ajuda ˅" em 16px na cor de link e aviso do reCAPTCHA em 13px.
- **Fluxo com o email primeiro:** o identificador vem antes e a senha ou o código na tela seguinte.

### 4.2 Landing — `capturas/01…05`, `capturas/responsivo/landing-*` [MEDIDO]
Ordem e posição vertical em 1512px de largura:

| y (px) | Seção |
|---|---|
| 0–88 | Header (sobre o hero) |
| 0–858 | Hero (100vh) com h1, subtítulo e formulário de email |
| ≈826 | "A curva" e banner promocional (1216×78) |
| 967–1282 | "Em alta": Top 10 com números |
| 1346–1703 | "Mais motivos para assinar": 4 cartões |
| 1767–2366 | "Perguntas frequentes": 6 itens |
| 2430–2546 | Formulário de email repetido |
| 2574–3030 | Rodapé |
| 3126 | Altura total |

Logado e sem plano, o formulário vira o CTA "Concluir cadastro ›" e "Entrar" vira "Sair".

### 4.3 Modal da landing — `capturas/06-landing-modal-titulo.jpg` [MEDIDO]
Ver 3.11.

### 4.4 Página de gênero (`/br/browse/genre/83`) — `capturas/07…10`, `responsivo/genero-*` [MEDIDO]
1. Fundo ambiente borrado e header de 72px.
2. Hero em arco: "Séries", descrição, CTA pílula e legenda "Diversão ilimitada a partir de R$ 25,90". Deslogado, entram o campo "Email" em pílula e "Acessar agora".
3. ~20 fileiras de capas verticais com legenda, a partir de y≈790 e espaçadas ≈400px. Exemplos: "Descubra suas próximas histórias", "Séries premiadas ›", "Novelas", "Séries baseadas em livros ›", "Séries românticas ›", "Reality shows…", "Desenhos animados ›", "Novidades na Netflix".
4. Planos (y≈7628).
5. Banner "Descubra…", faixa Tudum e CTA.
6. Rodapé. Altura total de 8732px em 1512.

### 4.5 Página de título (`/br/title/{id}`) — `capturas/11…13`, `responsivo/titulo-*` [MEDIDO]
| y (px, em 1512) | Seção |
|---|---|
| 72 | Navegação âncora (fixa) |
| 129–788 | Hero com o trailer |
| 827–1016 | Bloco de metadados (vidro) |
| 1056–1473 | "Episódios": carrossel de cards |
| 1513–1827 | "Mais detalhes": 3 painéis |
| 1866–2188 | "Talvez você também goste" |
| 2228–2555 | "Em alta" |
| 2595–2871 | Planos |
| 2912–3016 | Banner "Descubra…" |
| 3648 | Altura total |

### 4.6 Área de assinante (não medida ao vivo)

#### 4.6.1 Home de TV — imagem enviada pelo usuário [REF-TV]
Imagem de 1400×788 (16:9). Proporções relativas à tela e valores convertidos para 1920×1080 (×1,371):

| Elemento | Na imagem | % da tela | Em 1920×1080 |
|---|---|---|---|
| Trilho de ícones (centro dos ícones) | x≈57 | 4,1% da largura | x≈78 |
| Ícones (em ordem): Busca, **Início (ativo, sublinhado vermelho ≈20×3)**, Novidades (calendário), Séries (TV), Filmes (claquete), Minha lista (+) | ≈20px, um a cada ≈65px | 8,3% da altura | ≈27px, um a cada ≈89px |
| Grupo de ícones | y 235→561 | centralizado na vertical (≈50%) | |
| Início da coluna de texto | x≈113–117 | ≈8% | x≈158 |
| Rótulo "N SÉRIE" ("N" vermelho + palavra em caixa-alta espaçada ≈0,3em, cinza claro) | y≈133, ≈13px | 17% da altura | ≈18px |
| Logo do título | ≈308×112 | 22% da largura | ≈422×154 |
| Sinopse | 4 linhas, ≈19/26px, ≈382px de largura | 27% da largura | ≈26/36px, ≈524px |
| Botões "▶ Assistir" (branco) e "Mais informações" (cinza translúcido) | 132×50 e 149×50, espaço ≈11, raio ≈4 | 6,3% da altura | ≈181×68 e ≈204×68 |
| Título da fileira ("Em alta") | y≈554, ≈20px semibold | 70% da altura | ≈27px |
| Capas verticais 2:3 | ≈155×232, espaço ≈8, a fileira passa da borda de baixo e da direita (7½ visíveis) | 11% da largura cada | ≈213×318 |

- Fundo: arte em tela cheia, **sem barra superior**. Véu escuro forte à esquerda (≈0–45% da largura), onde ficam o texto e o trilho.
- Ícones inativos em branco ≈70%; o ativo em branco com o sublinhado vermelho.
- Capas com "N" no canto superior esquerdo e logo do título no terço inferior.
- Data: interface de TV usada até 2024–2025. Em 19/05/2025 o trilho foi trocado por atalhos no topo (Busca, Séries, Filmes, Jogos, Minha Netflix), e um teste de 03/11/2026 traz o trilho de volta como faixa de ícones que se expande, com o vídeo grande no topo e 6 tiles por fileira [PESQUISA].

#### 4.6.2 App mobile — mockup enviado pelo usuário [REF-MOBILE]
Design de terceiro (@bigmike_eneji), em tela tipo iPhone (≈375×812). Serve como referência de layout, não como medida oficial.

1. **Splash:** fundo preto com o wordmark vermelho centralizado.
2. **"Quem está assistindo?":**
   - Título centralizado no topo (≈17px semibold) e "Editar" à direita.
   - Grade de 2 colunas com avatares quadrados (≈100px, raio ≈4) e nome embaixo (≈13px).
   - O perfil "Infantil" fica centralizado numa linha própria.
3. **Home:**
   - Hero com a **arte vertical (pôster) em largura total**, ocupando ≈60% da tela e com degradê escuro embaixo.
   - No topo, sobre a arte: símbolo "N" + abas de texto (Séries · Filmes · Minha lista).
   - Rótulo "N SÉRIE", logo grande do título e linha de tags separadas por "•" (≈11px, ex.: "Novelão • Emocionante • Teen • Ação • Drama").
   - Ações: "+ Minha lista" (ícone sobre o rótulo, à esquerda), "▶ Assistir" (botão branco ≈110×32, raio 4, no centro) e "ⓘ Info" (à direita).
   - Fileira **"Prévias" com miniaturas circulares** (≈100px, anel colorido, logo do título na base do círculo), no estilo de stories.
   - Depois, fileiras de capas.
   - **Barra de abas inferior:** Início, Busca, Em breve (com contador vermelho), Downloads, Mais. Ícones de 24px com rótulo de 10px; a ativa em branco, as outras em cinza; fundo quase preto.
4. **Página do título:**
   - Fundo borrado com a capa vertical centralizada no topo (≈100×150) e "×" circular no canto superior direito.
   - Selo "TOP 10" + "nº 5 em séries hoje" (≈15px, negrito).
   - **Botão "▶ Assistir" em largura total** (≈343×36, raio 4; vermelho no mockup, branco no app real).
   - Sinopse (≈13px) e créditos (≈12px cinza).
   - Ações com ícone sobre rótulo: "+ Minha lista", "Avaliar" (polegar), "Compartilhar".
   - **Abas EPISÓDIOS | TRAILERS E MAIS | TÍTULOS SEMELHANTES** em ≈12px negrito caixa-alta; a ativa em branco com **barra vermelha de 3px acima** do rótulo.
   - Seletor "Temporada 1 ˅".
   - Linha de episódio: miniatura 16:9 (≈110×62, raio 4) com play circular, "1. Piloto" e sinopse cinza embaixo.
   - A barra inferior continua visível.
- **Hoje no app real [PESQUISA]:** o app novo de 30/04/2026 tem o feed vertical **"Clips"** (trechos de 30s a 1min+, com salvar, compartilhar e abrir detalhes), barra superior por tipo de conteúdo e menu inferior com busca, salvos e Clips. O Brasil está na próxima fase de lançamento.

#### 4.6.3 Home web do assinante [CLÁSSICO] + mudanças de 2025–2026 [PESQUISA]
- **Estrutura clássica:**
  - Header (3.3).
  - Billboard (3.6).
  - Pilha de fileiras: Continuar assistindo, Em alta, Top 10 com números grandes, Minha lista, gêneros, "Porque você assistiu a…", Jogos.
  - Card de hover e modal de detalhes (3.11).
  - Rodapé simples.
- **Refresh da web** (teste de 05/06/2026, quase todo lançado segundo matéria de 03/11/2026):
  - Tiles com cantos arredondados.
  - Fundo em degradê que muda conforme o título em foco (o mesmo princípio do "fundo ambiente" medido nas páginas públicas).
  - Faixas na base da capa: "Nova temporada chegando", "Recém-adicionado", "Muito revisto".
  - Jogos como 2ª fileira.
- **Outras mudanças:**
  - O "N" de original saiu dos tiles 16:9 da web entre 9 e 13/10/2025.
  - A ordenação A–Z, por ano e "sugeridos" saiu da web em maio/2026.
  - A porcentagem de relevância foi anunciada como "provavelmente" removida em jan/2024, sem confirmação.

#### 4.6.4 Busca, Minha lista, Perfis e Player [CLÁSSICO]
- **Busca:** o ícone vira campo no header e os resultados aparecem enquanto se digita. Grade de capas 16:9 com as mesmas colunas das fileiras e a linha "Explore títulos relacionados a: …" com links separados por "|".
- **Minha lista:** grade de capas 16:9.
- **Perfis (web):**
  - "Quem está assistindo?" em ≈3,5vw.
  - Avatares de ≈10vw (mínimo 84px, máximo 200px), raio 4.
  - Nome cinza, que fica branco no hover; o avatar ganha borda branca de ≈.3em.
  - Botão contornado "Gerenciar perfis" em caixa-alta espaçada.
- **Player:** tela cheia preta e seta de voltar no canto superior esquerdo. Na base:
  - Barra de progresso vermelha com miniatura da cena ao passar o mouse.
  - Controles: play/pausa, −10s, +10s, volume, título do episódio no centro, próximo episódio, lista de episódios, áudio e legendas, velocidade, tela cheia.
  - Os controles somem depois de ≈3s parado.
  - Botões "Pular abertura" e "Próximo episódio" (com contagem regressiva) no canto inferior direito.

---

## 5. Comportamentos e animações

| Comportamento | Detalhe | Fonte |
|---|---|---|
| Hover de capa | escala de 1,05 em 200ms ease-in-out, sem sombra | [MEDIDO] |
| Carrossel | rolagem horizontal; setas em pílula na borda direita; a capa da borda aparece cortada para indicar que há mais | [MEDIDO] |
| Trailer no hero | `<video>` mudo em autoplay sobre a `<picture>`, crossfade de opacidade em .4s; controles circulares (pausar, som, expandir, legendas) | [MEDIDO] |
| Modal | véu escurece em 250ms, diálogo entra em 533ms; fecha com Esc e com o "×" | [MEDIDO] |
| Acordeão | 250ms; "+" gira −45° | [MEDIDO] |
| Label do campo | flutua em 250ms | [MEDIDO] |
| CTA flutuante | *sticky* na base, entra em 1s | [MEDIDO] |
| Navegação âncora | fica fixa no topo enquanto a página rola | [MEDIDO] |
| Skeleton | pulso `#232323` ↔ `#414141` | [MEDIDO] |
| Movimento reduzido | existe `@media (prefers-reduced-motion)` | [MEDIDO] |
| Header do assinante | degradê → `#141414` sólido ao rolar | [CLÁSSICO] |
| Billboard do assinante | logo encolhe e sinopse some depois que o trailer começa; botão de som e "repetir" | [CLÁSSICO] |
| Card de hover | atraso ≈400–500ms, cresce ≈1,5× com prévia em vídeo | [CLÁSSICO] |
| Fundo que acompanha o foco | a cor do fundo segue a arte em foco (TV 2025, web 2026) | [PESQUISA] |

---

## 6. Responsividade (medido em 19/11/2026, deslogado)

Dados brutos em `dados/metricas-responsivas.json`. Screenshots de tela e de página inteira em `capturas/responsivo/` (banner de cookies escondido só na captura).

| Página | Viewport | Header | h1 (tam/peso/entrelinha) | Hero | CTA | Capas visíveis na 1ª fileira | Capa (no gênero inclui a legenda) | Outros | Altura total |
|---|---|---|---|---|---|---|---|---|---|
| landing | mobile-393 | 80 | 32px/700/40px | 393×664 | 139×48 18px r4px | 2 | 112×157 r8px | email 329×48; FAQ alt 72 / 18px; motivo 345×197 | 3853 |
| landing | tablet-768 | 80 | 32px/700/40px | 768×664 | 159×56 18px r4px | 5 | 112×157 r8px | email 265×56; FAQ alt 72 / 18px; motivo 704×193 | 3313 |
| landing | desktop-1280 | 88 | 56px/700/70px | 1280×808 | 184×56 24px r4px | 5 | 180×252 r8px | email 396×56; FAQ alt 84 / 24px; motivo 234×348 | 3112 |
| landing | desktop-1920 | 88 | 64px/700/80px | 1920×996 | 184×56 24px r4px | 6 | 214×300 r8px | email 472×56; FAQ alt 84 / 24px; motivo 291×324 | 3363 |
| genero | mobile-393 | 56 | 24px/500 | 345×527 | 200×40 16px r100px | 2 | 132×215 | plano 345×169 | 7722 |
| genero | tablet-768 | 56 | 32px/700 | 704×396 | — | 5 | 132×215 | plano 704×169 | 7268 |
| genero | desktop-1280 | 72 | 48px/900 | 1184×567 | — | 5 | 184×283 | plano 317×220 | 8644 |
| genero | desktop-1920 | 72 | 56px/900 | 1824×860 | — | 6 | 240×368 | plano 499×220 | 10269 |
| titulo | mobile-393 | 56 | — | 345×385 | — | 2 | 132×185 r16px | episódio 281×333; âncora 393×41; plano 345×169 | 4159 |
| titulo | tablet-768 | 56 | — | 704×600 | — | 5 | 132×185 r16px | episódio 283×334; âncora 417×41; plano 704×169 | 3952 |
| titulo | desktop-1280 | 72 | — | 1184×553 | — | 5 | 184×258 r16px | episódio 327×364; âncora 417×57; plano 317×220 | 3620 |
| titulo | desktop-1920 | 72 | — | 1824×845 | — | 6 | 240×336 r16px | episódio 327×364; âncora 417×57; plano 499×220 | 3959 |

"—" = o elemento não foi encontrado com o seletor da medição nessa versão. Deslogado, o CTA do catálogo é "Acessar agora", com outro seletor.

**O que muda em cada faixa:**
- **< 600:** formulário da landing empilhado (campo em largura total e CTA abaixo, centralizado); header do catálogo só com o "N"; cartões de motivos e de planos empilhados; FAQ em 18px; 2 capas e meia visíveis, com a seta por cima da borda; no hero da página de título, logo e CTA saem do vídeo.
- **600–959:** mesma tipografia do mobile (h1 32/40), formulário em linha, 5 capas visíveis.
- **≥ 960:** header maior e h1 de 56px.
- **≥ 1920:** h1 64/80, capas maiores (240px no catálogo, 214px no Top 10) e 6 visíveis.

---

## 7. Modelo de dados (inferido das páginas públicas)

**Título**
- `id`, `tipo` (série ou filme), `titulo` e `ano`.
- `nTemporadas` / `nEpisodios`, `classificacaoEtaria` (ex.: "A16").
- `generos[]` e `tags[]`: as tags de "Esta série é…", de tom e tropo, como "Gostinho de novela", "Do ódio ao amor", "Romântico", "Realeza".
- `sinopse`, `elencoResumo[]` (3 nomes) e `elenco[]`.
- `audios[]`, `legendas[]`, `disponivelOffline`.
- `trailerUrl`.
- `artes`:
  - `capaVertical`: com logo; também entregue sem texto;
  - `capaHorizontal16x9`;
  - `billboard`: escura, sem texto;
  - `storyArt`;
  - `logoHorizontal` e `logoEmpilhado`, cada um em versão `clara` e `escura`;
  - `fundoAmbiente`.
- `selos`: calculados pela interface, como `top10Rank`, `novaTemporada`, `novosEpisodios`, `emBreve`, `recemAdicionado`, `saiEmBreve`.
- `semelhantes[]` (ids).

**Episódio:** `numero`, `titulo`, `duracao`, `sinopse`, `miniatura16x9`.

**Coleção (fileira):** `titulo`, `temPaginaPropria` (mostra o "›"), `itens[]` (ids), `tipoDeCard` (vertical, Top 10 numerado ou 16:9).

**Para dramas curtos, acrescentar:** `nEpisodios` (o total, mostrado na capa), `duracaoMediaSeg` (60–180s), `episodiosGratis`, `precoMoedasPorEpisodio`, `exclusivo`, `completo`, `dublado`, `tropos[]`, `capa3x4`, `poster9x16`, `clipesDeGancho[]`.

---

## 8. Como isso vira a plataforma de dramas curtos

| Netflix | Nossa versão |
|---|---|
| Billboard 16:9 com trailer | Desktop: billboard 16:9 com o clipe de gancho e o fundo ambiente. Mobile: hero com o **pôster 9:16** em largura total (como no [REF-MOBILE]), logo, tags e "▶ Assistir ep. 1". |
| Capas verticais 5:7 e horizontais 16:9 | **Capa 3:4** (padrão do gênero) com o título aplicado na arte e o contador **"▶ N Episódios"** sobreposto pela interface (ver `CAPAS.md` §6). |
| Top 10 com números gigantes | "Em alta hoje" numerado, com o mesmo truque do número contornado sobre a capa. |
| Selos "Nova temporada", "TOP 10", "N" | "Novo", "Top 10", "Exclusivo", "Completo", "Dublado", "Grátis até o ep. X", "VIP", sempre como sobreposição de interface. |
| Página de título com cards de episódio de 50min | Página de série com **grade numérica de episódios** (1…80), cadeado e moedas nos bloqueados, faixa de "grátis"; "Mais detalhes" vira os **tropos**. |
| Player 16:9 | **Player vertical 9:16** em tela cheia: deslizar passa para o próximo episódio; autoplay; o paywall aparece no gancho do episódio. |
| Feed "Clips" (app 2026) | **Feed vertical como tela principal no mobile**: o centro do produto. |
| 3 cartões de plano em degradê | VIP semanal, mensal e anual + pacotes de moedas, reaproveitando o estilo dos cartões de plano. |
| "Mais motivos para assinar" | Benefícios do VIP (sem anúncios, todos os episódios, lançamentos primeiro). |
| Continuar assistindo com barra de progresso | "Continuar" com "Ep. 12/60" e barra de progresso. |
| Perfis | Opcional (dramas curtos costumam ter uma conta e uma carteira de moedas). |
| Trilho de ícones da TV / barra de abas do mobile | Desktop/TV: trilho à esquerda (Início, Busca, Em alta, Minha lista, Carteira). Mobile: barra inferior (Início, Feed, Minha lista, Carteira, Perfil). |

---

## 9. Ordem de construção sugerida

1. Tokens (`tokens.css`) com a nossa cor e a nossa fonte.
2. Primitivos: botão (todas as variantes), campo, pílula, botão-ícone, chip, selo.
3. Capa (3:4, com sobreposição de contador e selos) e fileira (carrossel com setas).
4. Billboard/hero (desktop e mobile) com fundo ambiente.
5. Página da série (metadados em vidro, grade de episódios, tropos, semelhantes).
6. Player vertical e feed.
7. Planos, moedas e paywall.
8. Landing pública, login e rodapé.

---

## 10. O que não copiar

Copiar o **layout, os padrões de interface e as medidas** como referência de design é o objetivo deste documento. Mas **não reproduza**:

- **Nome e logo da Netflix** (o wordmark e o símbolo "N"), nem o selo "N" nas nossas capas.
- **Netflix Sans:** fonte proprietária; use Inter, Figtree, Manrope ou uma fonte da nossa marca.
- **A combinação vermelho `#E50914` + preto como identidade:** é parte do *trade dress* da Netflix. Escolha **outra cor de ação** (o `tokens.css` já marca `--color-accent` para trocar).
- **Artes, logos de títulos, trailers e textos** que aparecem nas capturas: pertencem a estúdios e à Netflix e servem só de referência interna. Não publique as capturas.
- **Ícones e ilustrações** da Netflix (pipoca 3D, ícones de motivos): desenhe os próprios ou use uma biblioteca livre.
- **Código** (CSS/JS) da Netflix: nada foi copiado; só medimos valores computados.
- Textos de marketing ("Filmes, séries e muito mais, sem limites" etc.): escreva os nossos.

---

## 11. Limitações e como fechar as lacunas

- **Área de assinante não medida.** Para medir: entrar no Chrome com uma conta **com plano ativo** e repetir a extração (mesmo método das páginas públicas). Itens a medir:
  - header, com o estado depois de rolar;
  - billboard: tempos do trailer e encolhimento do logo;
  - fileiras: largura das capas por breakpoint e raio depois do refresh de 2026;
  - card de hover: atraso, escala e tamanhos;
  - modal de detalhes: largura e lista de episódios;
  - busca, Minha lista, perfis e player: controles e tempos.
- **Cadastro e plano** (`/signup`) não foram abertos, para não mexer no estado da conta.
- As mudanças de 2025–2026 vêm de **fontes secundárias** (seção 12) e não foram conferidas uma a uma.
- As medidas [REF-TV] e [REF-MOBILE] são estimativas visuais a partir de imagens, não valores de código.

---

## 12. Fontes da pesquisa (relatório de 19/11/2026; quase todas secundárias)

- Artwork Portal e glossário da Netflix (Partner College; li só os trechos indexados): https://partnercollege.netflix.net/en/licensed/artwork-portal/ · https://partnercollege.netflix.net/th_TH/partnership/getting-started/netflix-lingo/
- Regras de conteúdo das artes (via What's on Netflix, 28/12/2024): https://www.whats-on-netflix.com/news/what-can-and-cant-go-in-netflix-artwork-or-thumbnails/
- Tamanhos de entrega de fornecedores (Quiver Digital): https://support.quiverdigital.com/hc/en-us/articles/220024787-What-Is-Artwork-V3
- Deck de boas práticas de key art (PBS Distribution, 2023): https://pbsdistribution.org/wp-content/uploads/2024/08/KeyArt_BestPractices_Deck_121423_Docs.pdf
- TOP 10 (Netflix, 24/02/2020): https://about.netflix.com/en/news/see-whats-popular-on-netflix
- "N" removido dos tiles (out/2025): https://www.whats-on-netflix.com/news/netflix-removes-netflix-original-branding-label-from-tiles-on-web/
- "The Power of a Picture" (Netflix, 2016): https://about.netflix.com/en/news/the-power-of-a-picture
- Personalização de arte (resumo de 2017): https://www.itsnicethat.com/news/netflix-personalises-artwork-to-viewing-habits-181217
- Nova home de TV (2025): https://www.netflix.com/tudum/articles/netflix-new-tv-layout · https://help.netflix.com/en/node/321880164349028
- Teste de trilho lateral na TV (03/11/2026): https://www.whats-on-netflix.com/news/netflix-tv-app-redesign-test-sidebar-menu/
- Refresh da web (05/06/2026): https://www.whats-on-netflix.com/news/netflix-website-redesign-testing/
- Ordenação removida da web (mai/2026): https://www.whats-on-netflix.com/news/netflix-quietly-removes-a-z-and-other-sorting-from-web-ui/
- App novo com "Clips" (30/04/2026): https://www.thenationalnews.com/arts-culture/2026/04/30/new-vertical-videos-on-netflix-app/ · https://www.thewrap.com/media-platforms/tv/netflix-mobile-app-update-clips-explained/
- Hub "What's Hot" (12/11/2026): https://www.whats-on-netflix.com/news/netflix-launches-whats-hot-hub-trending-movies-shows/
- Dramas curtos (monetização e interface): https://www.revenuecat.com/blog/growth/short-drama-mobile-acquisition-monetization · https://oyelabs.com/reelshort-vs-dramabox-what-keeps-users-watching/
