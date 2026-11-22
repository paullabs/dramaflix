# Notas brutas — páginas públicas (medido ao vivo em 19/11/2026, Chrome, viewport 1512×862, DPR 2)

## Base global (Hawkins / "hcw")
- Fonte: "Netflix Sans", "Helvetica Neue", "Segoe UI", Roboto, Ubuntu, sans-serif. Pesos carregados: 400/500/700 (existem 100/300/900 + Variable 100–900).
- html/body: 16px, fundo #000 nas páginas deslogadas.
- Breakpoints do design system: 600 / 960 / 1280 / 1600 / 1920 / 2560 (xs <600, s ≥600, m ≥960, l ≥1280, xl ≥1600, xxl ≥1920, xxxl ≥2560). Também aparecem 400/550/740/768/896/1024 em componentes legados.
- Botão primário: fundo rgb(229,9,20) #E50914; hover rgb(193,17,25) #C11119; pressed rgb(153,22,29) #99161D; disabled rgba(229,9,20,.4); texto branco; raio 4px; transição background-color 250ms cubic-bezier(.4,0,.68,.06); hover easing cubic-bezier(.32,.94,.6,1); pressed 0ms.
  - Tamanhos: P (header) 32px alt, pad 4px 16px, 14px/500 | M (login, modal) 48px, pad 8px 16px, 18px/500 | G (hero) 56px, pad 12px 24px, 24px/500 com chevron 24px.
- Botão secundário (cinza): rgba(128,128,128,.4), 40px alt, pad 6px 16px, 16px/500, raio 4px.
- Input: fundo rgba(22,22,22,.7); borda 1px rgba(128,128,128,.7); raio 4px; altura 56px; padding 24px 16px 8px; label flutuante rgba(255,255,255,.7) 16px→12px; transição top/font-size/line-height 250ms cubic-bezier(.4,0,.68,.06). Erro rgb(235,57,66) #EB3942; sucesso rgb(43,184,113) #2BB871; aviso rgb(216,157,49) #D89D31.
- Link de texto: rgb(68,142,244) #448EF4; pressed rgb(148,194,255).
- Foco: anel 2px solid branco, offset 2px.
- Texto secundário: rgba(255,255,255,.7); terciário rgba(255,255,255,.5).
- Toast z-index 1002; modal backdrop z-index 1000.

## Login (/br/login)
- Header 88px: logo 148×40 (vermelho) a 24px do topo; header max-width calc(83.333% - 96px), padding 24px 48px.
- Fundo: degradê vinho escuro (topo) → preto (≈60% da altura) com textura sutil; rodapé cinza #161616.
- Formulário 440px (container 480): h1 32px/700 "Informe seus dados para entrar"; h2 18px/400 rgba(255,255,255,.7) "Ou crie uma conta."; input 56px; botão "Continuar" 440×48 vermelho; "Ajuda ˅" 16px #448EF4; aviso reCAPTCHA 13px.
- Fluxo email-primeiro (identificador → senha/código).

## Landing deslogada (/br/)
- Container de conteúdo: 1216px (gutter lateral 148px em 1512); hero max-width 1920px.
- Header 88px: logo 148×40; seletor de idioma 146×32 (borda 1px cinza translúcida, ícone de tradução à esquerda, pad 6px 36px 6px 34px, 16px); botão "Entrar" 72×32 vermelho 14px/500.
- Hero 100vh (≈858px): colagem de capas 16:9 inclinadas (imagem única, object-fit cover) + overlay linear-gradient(7deg, rgba(0,0,0,.85) 10% → rgba(0,0,0,.6) 97%) com 13 paradas (degradê "suavizado").
  - h1 56px/700, line-height 70px, largura 588px, centralizado: "Filmes, séries e muito mais, sem limites".
  - p 20px/500: "A partir de R$ 25,90. Cancele quando quiser."
  - h3 16px/400/24px: "Quer assistir? Informe seu email para criar ou reiniciar sua assinatura."
  - Form inline: input 396×56 + botão "Vamos lá ›" 184×56 (gap 8px).
- Divisor curvo: arco com borda/brilho vermelho→rosa (#E50914 → magenta) e degradê azul-marinho embaixo.
- Banner de anúncios: ícone pipoca 3D (77px) + cartão linear-gradient(91deg, rgb(72,37,102) 0%, rgb(22,29,82) 99.51%) raio 16px; h3 20px/500, p 16px; botão "Saiba mais" cinza.
- "Em alta" (Top 10): h2 24px/500; lista horizontal (ul flex), li 224px (pad 8px 22px); capa vertical 180×252 (≈5:7), raio 8px, fundo placeholder #232323, transição transform .2s ease-in-out (hover = leve scale-up); número do ranking 100px/700, cor de preenchimento #414141 c/ contorno -webkit-text-stroke 4px branco (visual: número escuro com contorno branco), posicionado em left:-22px bottom:0, sobrepondo o canto inferior esquerdo da capa; botão "Próximo" 24×120 rgba(255,255,255,.1) raio 8px, ícone chevron, transição opacity .4s.
  - Capas com selo "N" vermelho no canto superior esquerdo e logo do título na metade inferior.
- "Mais motivos para assinar": 4 cards 292×310, raio 16px, linear-gradient(149deg, rgb(25,34,71) 0%, rgb(33,14,23) 96.86%), backdrop-filter blur(30px); h3 24px/500; p 16px rgba(255,255,255,.7); ícone ilustrado 72px no canto inferior direito; gap 16px.
- FAQ: h2 24px/500; item 1216×84, fundo rgb(45,45,45) #2D2D2D, hover rgb(65,65,65) #414141; pergunta 24px/400, padding 24px; ícone "+" gira -45° (vira ×); painel com mesmo fundo, 24px, transição 250ms cubic-bezier(.32,.94,.6,1); espaço entre itens 8px; 1px entre pergunta e resposta.
- Rodapé: texto rgba(255,255,255,.7); "Dúvidas? Ligue para 0800…" 16px; grade de links 4 colunas (25% cada), 14px/21px sublinhados; seletor de idioma; "Netflix Brasil" 14px; aviso reCAPTCHA 13px rgba(255,255,255,.5).

## Modal de título na landing (clique numa capa do Top 10)
- Backdrop fixed rgba(0,0,0,.7), z 1000, flex centralizado, transição opacity .25s cubic-bezier(.32,.94,.6,1) .067s.
- Diálogo 669px (max-width), fundo #161616, borda 1px rgba(128,128,128,.4), raio 8px, sombra rgba(0,0,0,.8) 0 4px 8px, overflow hidden; entrada: opacity .1s + transform .533s cubic-bezier(.32,.94,.6,1).
- Hero 667×375 (16:9) com imagem de fundo + 2ª camada (z -1) + gradiente para #161616; logo do título (PNG, ~166×100) a 40px da esquerda, sobre a base do hero.
- Botão fechar: círculo 40px (raio 20px), ícone 24px, canto sup. dir. (16px de margem).
- Chips de metadados (ano, classificação, tipo, gênero): 14px/500, pad 3px 4px, fundo rgb(65,65,65) #414141, raio 4px, texto rgba(255,255,255,.7), gap 8px.
- Sinopse 16px branco; CTA "Vamos lá ›" 48px vermelho.
