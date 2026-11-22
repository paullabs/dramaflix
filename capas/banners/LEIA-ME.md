# Banners do billboard (16:9), um por título

São 18 banners, um para cada título dos lotes v2 e v3. Mostram **os mesmos atores da capa**, enquadrados para o topo da home e da página do título:
- protagonista no terço direito;
- lado esquerdo livre para o logo, a sinopse e os botões;
- parte de baixo escura, para as fileiras entrarem por cima.

## Pastas

| Pasta | O que é | Uso |
|---|---|---|
| `NN-slug.png` | Original 2720×1536, **sem texto** | Fonte para exportar outros tamanhos |
| `web/NN-slug.jpg` | 1920×1084 JPG, **sem texto** | Billboard/hero do site. O degradê e o logo entram por CSS |
| `com-logo/NN-slug.jpg` | 2720×1536 com degradês e título-logo | Prévia do encaixe ou peça pronta para redes/anúncios |
| `mock-home-billboard.png` | Mock da home 1920×1080 | Como o banner encaixa com header, sinopse, botões e fileira |
| `vitrine-banners.jpg` | Os 18 banners com logo numa folha | Conferência rápida |
| `prompts/` | Prompt e foto de referência de cada banner | Para refazer |

## Como encaixar no site (mesma lógica da Netflix)

- **Fundo:** `web/NN-slug.jpg` com `object-fit: cover; object-position: right center` (a pessoa nunca é cortada pela direita).
- **Degradê da esquerda:** `linear-gradient(77deg, rgba(0,0,0,.78) 0%, rgba(0,0,0,.35) 38%, transparent 62%)`.
- **Fade de baixo:** `linear-gradient(180deg, transparent, rgba(20,20,20,.55) 45%, #141414 88%)` nos ~46% inferiores.
- **Logo:** `logo_titulo` do catálogo, a 4vw da esquerda, com no máximo ~36% da largura e ~28% da altura.
- **Celular:** use o `fundo` 3:4 (ou a própria capa) com o logo por cima, em vez do banner 16:9.

## Como foram feitos

O modelo é o **Seedream 5.0 Pro** (Higgsfield), com a foto da capa como referência. O pedido foi para manter as pessoas idênticas e estender o cenário para a esquerda.

O caminho mais óbvio falhou: estender a foto com outpaint simples clonou a protagonista no lado esquerdo. O Soul 2.0 com referência também não serviu, porque mudou o rosto.

Custo: ~2,5 créditos por banner (~45 no total, mais ~3 do teste que falhou).
