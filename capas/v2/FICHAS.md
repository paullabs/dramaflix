# Catálogo v2 — 9 dramas curtos, 9 gêneros diferentes (capas realistas)

A v1 ficou em `capas/v1/`. Tinha um problema: quase tudo era romance com homem rico, e as fotos tinham cara de IA.
Nesta versão cada capa é de um gênero diferente e foi feita em três partes, como numa agência:

1. **Foto realista** gerada no **Soul 2.0**, modelo do Higgsfield para foto de ensaio. A foto sai sem nenhum texto e com o terço de baixo escuro para o título. Pedimos sempre: luz com direção e sombra, preto de verdade, grão de filme, pele com textura e um momento de atuação em vez de pose de banco de imagem.
2. **Título-logo** gerado à parte no **GPT Image 2.5**, em PNG com fundo transparente. A Netflix trabalha assim: arte sem texto de um lado, logo do título do outro. O mesmo PNG serve depois para o banner grande (billboard) e para a página do título.
3. **Montagem em pixel** (`montar_capa.py`), que junta tudo em ordem:
   - a foto;
   - um degradê escuro na base, que dá leitura ao título e abre espaço para o "▶ N Episódios" da interface;
   - o título com sombra suave;
   - grão por cima do título, para casar com o filme da foto.

## Os 9 títulos

| Nº | Gênero | Título | Episódios (sugestão) |
|---|---|---|---|
| 01 | Vingança | Ele Me Trocou. Eu Comprei a Empresa Dele. | 64 |
| 02 | Ação · identidade secreta (protagonista homem) | O Genro Humilhado Era o Dono de Tudo | 80 |
| 03 | Suspense doméstico | A Segunda Família do Meu Marido | 52 |
| 04 | Terror | Não Atenda Depois da Meia-Noite | 40 |
| 05 | Comédia (troca de corpos) | Troquei de Corpo com a Minha Sogra | 60 |
| 06 | Policial | A Delegada Que Prendeu o Próprio Pai | 58 |
| 07 | Fantasia (lobisomem) | Rejeitada Pelo Alfa, Escolhida Pela Lua | 80 |
| 08 | Época asiática (dublado) | A Concubina Que Renasceu Para Reinar | 90 |
| 09 | Jovem · universitário | Fingi Namorar Meu Pior Inimigo | 62 |

## Arquivos

| Nº | Capa final (1536×2048) | Foto usada | Título-logo (PNG transparente) |
|---|---|---|---|
| 01 | `01-ele-me-trocou.png` | `fotos/01b.png` | `titulos/01.png` |
| 02 | `02-o-genro-humilhado.png` | `fotos/02a.png` | `titulos/02.png` |
| 03 | `03-a-segunda-familia-do-meu-marido.png` | `fotos/03a.png` | `titulos/03.png` |
| 04 | `04-nao-atenda-depois-da-meia-noite.png` | `fotos/04a.png` | `titulos/04.png` |
| 05 | `05-troquei-de-corpo-com-a-minha-sogra.png` | `fotos/05a.png` | `titulos/05.png` |
| 06 | `06-a-delegada-que-prendeu-o-proprio-pai.png` | `fotos/06a.png` | `titulos/06.png` |
| 07 | `07-rejeitada-pelo-alfa.png` | `fotos/07a.png` | `titulos/07.png` |
| 08 | `08-a-concubina-que-renasceu.png` | `fotos/08a.png` | `titulos/08.png` |
| 09 | `09-fingi-namorar-meu-pior-inimigo.png` | `fotos/09c.png` | `titulos/09.png` |

- `web/`: as mesmas capas em 600×800 JPG para o site.
- `fotos/`: as fotos sem texto, incluindo as versões que não foram usadas. Servem para banner, fundo do player e página do título.
- `titulos/`: os títulos-logo em PNG transparente, prontos para o banner grande e para a página do título.
- `vitrine-capas-v2.png`: as 9 capas na grade da plataforma, com o contador "▶ N Episódios".
- `prompts-foto/` e `prompts-titulo/`: os prompts exatos de cada parte.

**O que foi conferido**
- Todos os 9 títulos estão com a grafia e os acentos certos.
- Mãos e dedos vistos em zoom: celular, xícara, algemas e mãos na mesa estão corretos.
- O medidor da skill de realismo (`medir.py`) não mostrou a assinatura de foto falsa: o microcontraste ficou dentro da faixa e não há branco estourado. As cenas noturnas medem escuras de propósito.
- Na 09, a 1ª foto foi trocada porque o rapaz parecia bem mais velho que a moça. Ficou a `09c`, com os dois em idade de faculdade.

**Custo:** 20 fotos no Soul 2.0 a 0,12 crédito (≈2,4) mais 9 títulos no GPT Image 2.5 a ≈4,5 créditos (≈40,5). Total ≈ 43 créditos.

## Histórias

**01 · Vingança — Ele Me Trocou. Eu Comprei a Empresa Dele.**
Depois de 7 anos bancando o marido, Helena é trocada pela estagiária no aniversário de casamento. Ela some por um ano e volta como a investidora que acabou de comprar a empresa dele. Agora ele precisa da assinatura dela para não falir.

**02 · Ação — O Genro Humilhado Era o Dono de Tudo**
Há três anos, Lucas aguenta calado as humilhações da família rica da esposa, que o trata como um fracassado. Na festa de aniversário da sogra, chegam os seguranças de um grupo bilionário à procura do "presidente". É ele, e acabou o tempo de ficar quieto.

**03 · Suspense doméstico — A Segunda Família do Meu Marido**
Marina acha um segundo celular na gaveta do marido. Uma noite ela o segue e vê, pela janela de outra casa, o homem que ama abraçando outra mulher e uma filha de 6 anos. A investigação dela revela algo muito pior que uma traição.

**04 · Terror — Não Atenda Depois da Meia-Noite**
Um ano depois do desaparecimento da irmã, Bia começa a receber ligações do número dela, sempre às 00h00. Cada vez que atende, alguém da cidade some. A voz do outro lado diz que só para quando ela for buscá-la.

**05 · Comédia — Troquei de Corpo com a Minha Sogra**
Clara e dona Lourdes se odeiam. Depois de uma briga no aniversário da família e de um raio, as duas acordam uma no corpo da outra. Agora a sogra precisa ir ao trabalho da nora e a nora precisa enfrentar o grupo de oração da sogra, sem ninguém desconfiar.

**06 · Policial — A Delegada Que Prendeu o Próprio Pai**
A delegada Renata investiga uma rede de lavagem de dinheiro que domina o porto de Santos. Todas as provas apontam para o empresário mais respeitado da cidade: o pai dela. Prender o pai é a única forma de salvar o próprio nome, e talvez a vida da mãe.

**07 · Fantasia — Rejeitada Pelo Alfa, Escolhida Pela Lua**
Na noite do vínculo, o Alfa Kael rejeita Maya diante de toda a matilha. Mas ela é a primeira loba branca em 300 anos, e o líder da matilha rival está disposto a tudo para tê-la ao seu lado.

**08 · Época asiática — A Concubina Que Renasceu Para Reinar**
Envenenada pela imperatriz no dia da coroação, Lian acorda dez anos no passado. Desta vez ela conhece cada traição do palácio, e o imperador frio vai perceber que a concubina esquecida virou a jogadora mais perigosa da corte.

**09 · Jovem — Fingi Namorar Meu Pior Inimigo**
Para fazer ciúme no ex, Júlia propõe um namoro de mentira a Theo, o cara que ela mais detesta na faculdade. As regras são três: sem beijo, sem sentimentos e sem contar para ninguém. Em uma semana as três já foram quebradas.
