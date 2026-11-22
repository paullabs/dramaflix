# Referência Netflix — extração para a plataforma de dramas curtos

Extraído em **19/11/2026** da Netflix web brasileira, ao vivo no Chrome, mais capturas automáticas em 4 larguras de tela.

## Por onde começar
1. **`ESPECIFICACAO.md`**
   - §0: a "cara" da Netflix em 10 regras.
   - §1: o mapa do site.
   - §2: os fundamentos (cores, tipografia, grade, breakpoints, movimento).
   - §3–4: cada componente e cada página com medidas; §4.6 traz a área de assinante pelas imagens de referência (TV e app).
   - §6: a tabela de responsividade (393/768/1280/1920).
   - §8: como cada peça vira dramas curtos.
   - §10: o que não copiar. §11: limitações.
2. **`tokens.css`** / **`tokens.json`** — cores, tipografia, espaçamento, raios, sombras, gradientes, movimento e breakpoints prontos para código.
3. **`CAPAS.md`** — tipos de arte, anatomia da capa, selos, ranking Top 10, o que faz uma capa performar e o pacote de arte proposto para os nossos títulos.

## O que foi medido e o que não foi
| Área | Status |
|---|---|
| Login, landing (com modal de título), catálogo público por gênero, página pública do título | **Medido ao vivo** (estilo computado + variáveis do design system) |
| Mobile 393 · tablet 768 · desktop 1280 e 1920 dessas páginas | **Medido** (capturas + `dados/metricas-responsivas.json`) |
| Home do assinante, card de hover, modal completo, busca, perfis, player | **Não medido**: a conta logada no Chrome está sem plano ativo. Documentado pelas imagens de referência enviadas (TV e app) e pelo layout clássico, sempre marcado como [REF] ou [CLÁSSICO] |

Para completar a área do assinante: logar no Chrome com uma conta de plano ativo e repetir a extração (ver `ESPECIFICACAO.md` §11).

## Capturas (`capturas/`)
| Arquivo | O que mostra |
|---|---|
| `00-login-desktop.jpg` | Login em etapas (email/celular → continuar) |
| `01-landing-hero.jpg` | Hero com colagem, headline, formulário de email |
| `02-landing-banner-top10-motivos.jpg` | Curva vermelha, banner de anúncios, Top 10 numerado, motivos |
| `03-landing-motivos-faq.jpg` | Cartões de motivos com gradiente, FAQ |
| `04-landing-faq-rodape.jpg` | Formulário repetido e rodapé |
| `05-landing-top10-hover.png` | Capa do Top 10 em hover (escala 1.05) |
| `06-landing-modal-titulo.jpg` | Modal de título (hero 16:9, logo, chips, CTA) |
| `07-genero-publico-hero.jpg` | Catálogo: hero arredondado com base em arco |
| `08-genero-publico-fileiras-capas-verticais.jpg` | Fileiras de capas 5:7 com selos (N, TOP 10, "Nova temporada") |
| `09-genero-publico-planos.jpg` | Cartões de plano, banner, faixa Tudum, CTA |
| `10-genero-publico-rodape.jpg` | Rodapé sobre o fundo ambiente borrado |
| `11-titulo-publico-hero-video.jpg` | Página de título: pílula de navegação, trailer, controles |
| `12-titulo-publico-metadados-episodios.jpg` | Painel de vidro com metadados + cards de episódio |
| `13-titulo-publico-detalhes-semelhantes.jpg` | "Mais detalhes" + "Talvez você também goste" |
| `responsivo/{landing,genero,titulo}-{mobile-393,tablet-768,desktop-1280,desktop-1920}-{tela,pagina-inteira}.jpg` | 24 capturas responsivas (deslogado, banner de cookies escondido só na imagem) |
| `referencias-usuario/dramabox-*.webp` | As duas capturas de vitrine de drama curto enviadas pelo usuário (capas 3:4 com "▶ N Episódios"), analisadas em `CAPAS.md` §6.0 |

As duas imagens de referência da área de assinante (interface de TV e mockup do app) foram enviadas no chat e não estão salvas aqui. A descrição completa delas está em `ESPECIFICACAO.md` §4.6.

## Dados brutos (`dados/`)
- `notas-01-publico.md` — login, landing e modal: valores medidos.
- `notas-02-catalogo-publico.md` — catálogo e página de título: valores medidos.
- `metricas-responsivas.json` — medidas por página e largura de tela.

## Direitos
As capturas contêm artes e logos de terceiros e servem **só como referência interna**: não publicar nem usar no produto. Não copiamos código da Netflix; os documentos descrevem medidas e comportamentos para reimplementar do zero. Nome, logo, fonte Netflix Sans e o vermelho como identidade devem ser trocados pela nossa marca (ver `ESPECIFICACAO.md` §10).
