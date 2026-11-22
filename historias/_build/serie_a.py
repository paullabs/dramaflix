# -*- coding: utf-8 -*-
# Bíblia da série A — "Ganhei na Mega-Sena e Fingi Que Era Pobre"
# Roteiro em mini-marcação: linha "@..." = ação; "NOME | parentético | fala" = diálogo.

SERIE = {
 'slug': 'ganhei-na-mega-sena',
 'letra': 'A',
 'titulo': 'Ganhei na Mega-Sena e Fingi Que Era Pobre',
 'capa': 'capas/v3/10-ganhei-na-mega-sena.png',
 'logo': 'capas/v3/titulos/10.png',
 'banner': 'capas/banners/10-ganhei-na-mega-sena.png',
 'cor': '#F2B705',
 'genero': 'Comédia dramática · Virada de sorte · Romance de vizinhos',
 'formato': '3 episódios de teste · cerca de 2 min cada · vertical 9:16 · live action',
 'look_id': 'realism_cinematic',
 'logline': ('Uma caixa de supermercado ganha sozinha R$ 212 milhões, mas o bilhete vai parar dentro da panela '
             'de feijão da sogra. Em vez de contar, ela finge que foi demitida para descobrir quem a ama de verdade.'),
 'gancho': ('A sogra amassa o bilhete premiado e joga por cima do ombro: ele cai dentro da panela de pressão '
            'no exato segundo em que a TV anuncia o último número. Dani tira os R$ 212 milhões do feijão fervendo '
            'com a mão, enquanto o marido filma tudo para a internet.'),
 'tom': ('Novela popular com ritmo de short drama: humor físico e absurdo na superfície, humilhação e virada '
         'por baixo. Cada episódio abre com um absurdo e fecha num congelamento de rosto.'),
 'temas': ['Quem te ama quando você não tem nada', 'Dinheiro revela caráter', 'Pequenas gentilezas valem mais que prêmios',
           'A vingança de quem sempre engoliu sapo'],
 'publico': 'Fãs de novela e de short drama, 18 a 55 anos, mobile first, PT-BR.',
 'look': ('Luz quente de lâmpada nua e TV no apartamento, fluorescente fria no corredor, LED limpo no banco e '
          'pôr do sol laranja na laje. Cores reais da Zona Leste de São Paulo, alto contraste suave, nada de filtro.'),
 'sinopse': [
   ('Dani Rocha, 28 anos, caixa de supermercado, paga o aluguel, a luz e a internet de um apartamento onde é '
    'tratada como estorvo: o marido, Cléber, vive no sofá gravando vídeos de "empreendedor digital", e a sogra, '
    'Dona Neusa, a chama de encosto entre uma panela de feijão e outra.'),
   ('Na noite do sorteio, Dani confere o bilhete diante da TV. Antes do último número, Neusa amassa o papel e o '
    'joga por cima do ombro, direto dentro da panela de pressão. Dani resgata o bilhete do feijão fervendo, '
    'ouve o marido pedir um PIX e a sogra sonhar com Miami, e decide: não vai contar nada a ninguém.'),
   ('Para testar a família, ela anuncia que foi demitida. O marido quer vender o celular dela; a sogra culpa '
    'o azar da nora; só Tiago, o vizinho tímido do 302, aparece com os R$ 800 que guardava para o pneu da '
    'bicicleta. No banco, disfarçada com o casaco da sogra, Dani confirma o prêmio, e quase é descoberta '
    'quando o marido entra de mãos dadas com Kelly, a influenciadora do 401.'),
   ('Achando que Kelly é a milionária, Cléber pede o divórcio na hora, com uma cláusula de renúncia escrita '
    'para proteger "os milhões dele". Dani assina sorrindo. Expulsa de casa com uma lata de café debaixo do '
    'braço, ela aceita o café do vizinho, enquanto a TV anuncia que a ganhadora misteriosa acabou de comprar '
    'o prédio inteiro.'),
 ],
 'arco': [
   {'ep': 1, 'titulo': 'O bilhete na panela de pressão',
    'resumo': 'O bilhete premiado cai no feijão; Dani o resgata, decide guardar segredo e o esconde na lata de café.',
    'gancho': 'Cléber encontra o bilhete dentro da lata: "Que papel é esse?"'},
   {'ep': 2, 'titulo': 'Fui demitida (mentira)',
    'resumo': 'Dani finge a demissão, vê quem fica do lado dela e confirma no banco: R$ 212 milhões, sozinha.',
    'gancho': 'Kelly olha debaixo da mesa do banco: "Amor... aquela não é a sua mulher?"'},
   {'ep': 3, 'titulo': 'O divórcio mais rico do Brasil',
    'resumo': 'Cléber troca Dani pela "milionária" errada e assina a própria ruína; Dani é expulsa e compra o prédio.',
    'gancho': 'Na laje, ao pôr do sol: "Agora sim... começou."'},
 ],
 'curva': [('Ep 1', 'humilhada', 18), ('Ep 2', 'testando', 50), ('Ep 3', 'dona do prédio', 92)],
 'atencao': [
   'Kelly: as duas argolas douradas no peito da jaqueta vieram do flat-lay do figurino, onde os brincos estavam pousados sobre a jaqueta. '
   'Se incomodar, refaça o figurino com os brincos à parte e gere o sheet de novo; na cena, os brincos ficam só nas orelhas.',
 ],
 'regras': [
   'Um absurdo nos primeiros 15 segundos de cada episódio: o bilhete no feijão, o salto por cima do sofá, a fuga vestida de faxineira.',
   'A humilhação vem antes da virada: o público precisa sentir raiva da sogra e do marido para comemorar depois.',
   'A plateia sabe mais que a família: a graça é todo mundo saber do prêmio, menos quem humilha a Dani.',
   'Bordões que voltam sempre: "Tá tudo bem. Tá tudo ótimo.", "Encosto!", "Precisando de açúcar... é só bater."',
   'Todo episódio termina num rosto congelado e numa pergunta que obriga a ver o próximo.',
 ],
}

PERSONAGENS = [
 {'id': 'dani', 'nome': 'Dani', 'completo': 'Daniela "Dani" Rocha', 'idade': 28,
  'lado': 'Protagonista', 'role': 'underdog', 'role_pt': 'A subestimada', 'status': 'baixo → alto',
  'rota': 'foto', 'imagens': {'sheet': 'dani_sheet', 'rosto': '_refs/dani-rosto.jpg'},
  'leitura': ('A caixa de supermercado tratada como encosto que guarda, em segredo, um bilhete de R$ 212 milhões; '
              'o público torce pela virada.'),
  'aparencia': ('Mulher brasileira parda; pele morena-clara oliva com sardas leves; olhos castanhos quentes; cabelo '
                'castanho-escuro com pontas mais claras, na altura dos ombros, cachos naturais soltos; corpo esguio, '
                'com curvas naturais.'),
  'figurino': ['Camiseta de algodão verde-sálvia desbotada, gola careca', 'Calça jeans skinny, lavagem clara, gasta',
               'Tênis de lona branco, encardido', 'Brincos pequenos de ouro', 'Anel fino de prata'],
  'voz': 'Mulher, 28 anos, timbre médio e quente, sotaque paulistano da Zona Leste; fala rápido quando está nervosa e fica irônica quando engole sapo.',
  'voz_en': 'woman, 28, warm mid-range voice, São Paulo working-class accent, quick when nervous, dry and ironic when holding back',
  'personalidade': ('Trabalhadora, engraçada sem querer, engole tudo com um sorriso, mas observa e guarda cada '
                    'humilhação. Tem um senso de justiça teimoso e um coração mole para quem é gentil com ela.'),
  'objetivo': 'Descobrir quem a ama de verdade antes de contar que está rica.',
  'segredo': 'É a única ganhadora dos R$ 212 milhões, e o bilhete ainda cheira a feijão.',
  'arco': ['Ep 1: humilhada, resgata o bilhete da panela e decide calar.',
           'Ep 2: finge a demissão, separa quem fica de quem foge e confirma o prêmio.',
           'Ep 3: assina o divórcio rindo, é expulsa e vira dona do prédio.'],
  'bordao': 'Tá tudo bem. Tá tudo ótimo.',
  'relacoes': ['Esposa de Cléber', 'Nora de Dona Neusa', 'Vizinha (e amor secreto) de Tiago', 'Kelly flerta com o marido dela'],
  'eps': [1, 2, 3],
  'looks': [{'id': 'dani_look_disfarce', 'nome': 'Disfarce do banco', 'eps': 'Ep 2 (cenas 3–4) e Ep 3 (cenas 1–2)',
             'objetos': ['oculos'], 'muda': ('Por cima da roupa base: trench coat caramelo da sogra, cintado; lenço de seda preto com flores '
                      'vinho e dourado amarrado no queixo, cobrindo o cabelo. Os óculos escuros enormes são objeto à parte.')}],
 },
 {'id': 'cleber', 'nome': 'Cléber', 'completo': 'Cléber Rocha', 'idade': 32,
  'lado': 'Antagonista', 'role': 'impostor', 'role_pt': 'O impostor', 'status': 'médio · encenado',
  'rota': 'figurino', 'imagens': {'sheet': 'cleber_sheet', 'rosto': 'cleber_face', 'figurino': 'cleber_outfit'},
  'leitura': ('O marido de sofá que finge carinho enquanto pede dinheiro e flerta com a vizinha; o público quer '
              'vê-lo desmascarado.'),
  'aparencia': ('Homem brasileiro pardo; pele morena-clara; olhos castanho-escuros; cabelo preto curto em degradê '
                'com topete de gel; cavanhaque fino e barba por fazer; corpo macio, com barriguinha de cerveja.'),
  'figurino': ['Camiseta branca de algodão', 'Bermuda de moletom cinza', 'Chinelo de borracha preto com meia branca',
               'Corrente fina dourada'],
  'voz': 'Homem, 32 anos, voz média-grave, sotaque paulistano cheio de gíria de internet; tom de coach, fala com o celular como se fosse um palco.',
  'voz_en': 'man, 32, mid-low voice, São Paulo accent full of internet slang, self-help-coach tone, performs for his phone',
  'personalidade': ('Preguiçoso, vaidoso, "empreendedor digital" sem seguidores. Covarde diante da mãe, vê '
                    'dinheiro em tudo e carinho em nada.'),
  'objetivo': 'Ficar rico sem trabalhar, de preferência com o dinheiro de uma mulher.',
  'segredo': 'Tem um caso com Kelly e pediu empréstimo no banco para um "estúdio de conteúdo".',
  'arco': ['Ep 1: filma a mulher "surtando" e quase leva o bilhete.',
           'Ep 2: quer vender o celular dela e aparece no banco com a amante.',
           'Ep 3: pede o divórcio achando que a amante é a milionária e renuncia à fortuna da ex.'],
  'bordao': 'Amor, faz um PIX pro seu homem?',
  'relacoes': ['Marido de Dani', 'Filho de Dona Neusa', 'Amante de Kelly'],
  'eps': [1, 2, 3],
 },
 {'id': 'neusa', 'nome': 'Dona Neusa', 'completo': 'Neusa Rocha', 'idade': 58,
  'lado': 'Antagonista', 'role': 'oppressor', 'role_pt': 'A opressora', 'status': 'alto · exibida',
  'rota': 'figurino', 'imagens': {'sheet': 'neusa_sheet', 'rosto': 'neusa_face', 'figurino': 'neusa_outfit'},
  'leitura': ('A sogra mandona que chama a nora de encosto dentro da casa que a nora paga; o público quer vê-la '
              'no lugar dela.'),
  'aparencia': ('Mulher brasileira parda; pele morena média-clara; olhos castanho-escuros; cabelo castanho-escuro '
                'ondulado com raiz grisalha, chanel curto repicado; corpo cheio e robusto.'),
  'figurino': ['Blusa de viscose preta de manga curta com flores grandes vinho e dourado', 'Calça capri preta',
               'Chinelo de quarto bege', 'Argolas grossas douradas', 'Corrente dourada com pingente'],
  'voz': 'Mulher, 58 anos, voz forte e anasalada, sotaque paulistano carregado; fala alto, como quem nunca foi contrariada.',
  'voz_en': 'woman, 58, loud nasal voice, strong São Paulo accent, bossy, never lowers her tone',
  'personalidade': ('Dramática, mandona, idolatra o filho. Faz feijão na panela de pressão todo santo dia e sonha '
                    'em morar em Miami.'),
  'objetivo': 'Manter o filho por perto e viver de graça, às custas da nora.',
  'segredo': 'Nunca pagou um centavo de aluguel e esconde uma poupança gorda guardada "pra Miami".',
  'arco': ['Ep 1: joga o bilhete na panela.', 'Ep 2: culpa a nora pela "demissão".',
           'Ep 3: expulsa Dani e recebe o aviso de despejo da nova dona do prédio.'],
  'bordao': 'Encosto!',
  'relacoes': ['Mãe de Cléber', 'Sogra de Dani'],
  'eps': [1, 2, 3],
 },
 {'id': 'tiago', 'nome': 'Tiago', 'completo': 'Tiago Nunes', 'idade': 30,
  'lado': 'Protagonista (par romântico)', 'role': 'pure_heart', 'role_pt': 'O coração puro', 'status': 'baixo · natural',
  'rota': 'figurino', 'imagens': {'sheet': 'tiago_sheet', 'rosto': 'tiago_face', 'figurino': 'tiago_outfit'},
  'leitura': ('O vizinho tímido que sempre empresta açúcar e oferece as últimas economias; o público se apaixona '
              'pela bondade silenciosa dele.'),
  'aparencia': ('Homem brasileiro negro; pele marrom-escura; olhos castanho-escuros; cabelo preto crespo bem curto e '
                'alinhado; barba curta bem aparada; corpo esguio.'),
  'figurino': ['Camisa de chambray azul-clara com as mangas dobradas', 'Camiseta branca de gola careca por baixo',
               'Calça chino bege', 'Tênis de couro marrom, gasto'],
  'voz': 'Homem, 30 anos, voz grave e suave, sotaque paulistano; fala devagar e baixinho e tropeça nas palavras perto da Dani.',
  'voz_en': 'man, 30, deep soft voice, São Paulo accent, slow and quiet, stumbles over words when nervous',
  'personalidade': ('Professor de matemática de escola pública que faz entregas de bicicleta no fim de semana. '
                    'Gentil, honesto, envergonhado; faz contas de cabeça para disfarçar o nervosismo.'),
  'objetivo': 'Ajudar a Dani e, um dia, ter coragem de dizer o que sente.',
  'segredo': 'É apaixonado pela Dani há dois anos e usa o açúcar como desculpa para bater na porta dela.',
  'arco': ['Ep 1: aparece com a caneca de açúcar.', 'Ep 2: oferece os R$ 800 do pneu da bicicleta.',
           'Ep 3: acolhe Dani com café e divide a laje com ela.'],
  'bordao': 'Precisando de açúcar... é só bater.',
  'relacoes': ['Vizinho do 302', 'Amigo (e futuro amor) de Dani'],
  'eps': [1, 2, 3],
 },
 {'id': 'kelly', 'nome': 'Kelly', 'completo': 'Kelly Moraes', 'idade': 27,
  'lado': 'Antagonista', 'role': 'impostor', 'role_pt': 'A impostora', 'status': 'alto · encenado',
  'rota': 'figurino', 'imagens': {'sheet': 'kelly_sheet', 'rosto': 'kelly_face', 'figurino': 'kelly_outfit'},
  'leitura': ('A influenciadora fitness interesseira que corre atrás de quem parece rico; o público mal pode '
              'esperar para vê-la enganada.'),
  'aparencia': ('Mulher brasileira branca; pele clara levemente bronzeada; olhos cor de mel; cabelo loiro platinado, '
                'longo e liso, em rabo de cavalo alto e polido; maquiagem glam com cílios marcados e gloss nude; corpo '
                'esguio e tonificado.'),
  'figurino': ['Conjunto de academia rosa-claro: jaqueta cropped com zíper', 'Legging de cintura alta do mesmo conjunto',
               'Tênis branco robusto', 'Argolinhas douradas'],
  'voz': 'Mulher, 27 anos, voz aguda e cantada, sotaque paulistano de influenciadora; fala como se estivesse sempre gravando um story.',
  'voz_en': 'woman, 27, high sing-song voice, São Paulo influencer accent, always sounds like she is recording a story',
  'personalidade': 'Performática, superficial e rápida para farejar oportunidade. Vive de aparência e de permuta.',
  'objetivo': 'Arrumar um homem rico, ou que pareça rico, e fechar parceria com qualquer marca.',
  'segredo': 'Tem 40 mil seguidores e R$ 38 na conta.',
  'arco': ['Ep 2: entra no banco de mãos dadas com Cléber e acha Dani debaixo da mesa.',
           'Ep 3: finge ser a ganhadora e confessa que está falida.'],
  'bordao': 'Gente, olha a energia!',
  'relacoes': ['Vizinha do 401', 'Amante de Cléber'],
  'eps': [2, 3],
 },
 {'id': 'valter', 'nome': 'Seu Valter', 'completo': 'Valter Siqueira', 'idade': 55,
  'lado': 'Funcional', 'role': 'functional', 'role_pt': 'O funcional', 'status': 'médio',
  'rota': 'figurino', 'imagens': {'sheet': 'valter_sheet', 'rosto': 'valter_face', 'figurino': 'valter_outfit'},
  'leitura': 'O gerente educado que conta a Dani o tamanho do prêmio e quase desmaia junto com ela.',
  'aparencia': ('Homem brasileiro pardo; pele morena média; olhos castanho-escuros; cabelo preto liso e curto, '
                'grisalho nas têmporas e ralo no topo, penteado de lado; bigode fino; corpo mediano, um pouco arredondado.'),
  'figurino': ['Camisa social azul-clara de manga curta', 'Gravata azul-marinho', 'Calça cinza-chumbo',
               'Cinto e sapato pretos de couro'],
  'voz': 'Homem, 55 anos, voz média e formal, sotaque paulistano; fala baixo e rápido quando fica nervoso.',
  'voz_en': 'man, 55, formal mid-range voice, São Paulo accent, quiet and fast when nervous',
  'personalidade': 'Discreto e cerimonioso; segue o protocolo à risca, até ver o tamanho do prêmio.',
  'objetivo': 'Atender a ganhadora com sigilo absoluto.',
  'segredo': 'Ensaiou a frase "a senhora está rica" no espelho durante 20 anos de carreira.',
  'arco': ['Ep 2: confirma o prêmio.', 'Ep 3: sem querer, faz Cléber achar que Kelly é a ganhadora.'],
  'bordao': 'Sigilo absoluto, senhora.',
  'relacoes': ['Gerente da agência', 'Guardião do segredo de Dani'],
  'eps': [2, 3],
 },
]

RELACOES = [
 ('dani', 'cleber', 'casados'), ('neusa', 'cleber', 'mãe e filho'), ('neusa', 'dani', '"encosto!"'),
 ('tiago', 'dani', 'açúcar e amor calado'), ('kelly', 'cleber', 'caso escondido'), ('valter', 'dani', 'guarda o segredo'),
]

LOCACOES = [
 {'id': 'cozinha_sala', 'nome': 'Apartamento 301 — cozinha e sala', 'hora': 'Noite',
  'look': ('Apartamento popular pequeno na Zona Leste de São Paulo: cozinha americana e sala conjugadas, azulejo '
           'branco, lâmpada nua, sofá marrom gasto, TV pequena.'),
  'luz': ['Lâmpada nua no teto da cozinha (luz principal, amarela)', 'Brilho azulado da TV ligada', 'Janelas acesas dos prédios vizinhos'],
  'mapa': {'Esquerda': 'Bancada com fogão de 4 bocas, pia e geladeira sob o azulejo branco',
           'Direita': 'Sofá marrom de couro sintético rasgado e rack com a TV',
           'Fundo': 'Janela de alumínio com cortina florida desbotada',
           'Frente': 'Porta de entrada de madeira (acesso principal)'},
  'eps': 'Ep 1 (cenas 1, 2 e 4) · Ep 2 (cenas 1 e 2) · Ep 3 (cena 3)',
  'nota': 'A lata de café mora em cima da geladeira; a panela de pressão, na boca da frente do fogão.'},
 {'id': 'corredor', 'nome': 'Corredor do 3º andar (301 × 302)', 'hora': 'Noite',
  'look': ('Corredor estreito de prédio sem elevador: paredes verde-claro descascadas, piso de granilite, escada '
           'com corrimão de ferro pintado de preto.'),
  'luz': ['Lâmpada fluorescente tubular no teto (fria)', 'Luz quente vazando por baixo das portas'],
  'mapa': {'Esquerda': 'Porta do 301 (Dani) com capacho xadrez', 'Direita': 'Porta do 302 (Tiago) e a caixa de luz',
           'Fundo': 'Escada que sobe para o 4º andar (Kelly, 401)', 'Frente': 'Patamar da escada que desce'},
  'eps': 'Ep 1 (cena 3) · Ep 3 (cenas 4 e 5)',
  'nota': 'As duas portas ficam frente a frente: tudo o que acontece no 301 se ouve no 302.'},
 {'id': 'sala_ganhadores', 'nome': 'Sala reservada do banco', 'hora': 'Dia',
  'look': ('Sala de atendimento privado numa agência bancária: mesa de madeira escura com painel frontal até o '
           'chão, cadeiras de couro preto, divisória de vidro fosco com persiana.'),
  'luz': ['Painéis de LED no teto (principal, neutra)', 'Sol filtrado pela persiana', 'Abajur no aparador'],
  'mapa': {'Esquerda': 'Aparador com garrafa térmica e copos; no canto, um rodo e um balde amarelo',
           'Direita': 'Divisória de vidro fosco com persiana para o salão',
           'Fundo': 'Parede de madeira escura com um quadro abstrato azul',
           'Frente': 'Porta de vidro fosco, a única entrada'},
  'eps': 'Ep 2 (cenas 3 e 4) · Ep 3 (cenas 1 e 2)',
  'nota': 'O painel frontal da mesa é o esconderijo da Dani; o rodo e o balde são a rota de fuga do Ep 3.'},
 {'id': 'laje', 'nome': 'Laje do prédio', 'hora': 'Pôr do sol',
  'look': ('Laje de concreto no alto do prédio: caixa-d\'água azul, varal com lençóis, duas cadeiras de plástico '
           'brancas e o skyline da Zona Leste ao pôr do sol.'),
  'luz': ['Sol laranja baixo no horizonte (contraluz)', 'Lâmpada nua acesa sobre a porta da escada'],
  'mapa': {'Esquerda': 'Caixa-d\'água azul sobre uma base de tijolos', 'Direita': 'Varal com lençóis e duas cadeiras de plástico',
           'Fundo': 'Mureta baixa e o skyline ao pôr do sol', 'Frente': 'Porta de ferro da escada'},
  'eps': 'Ep 3 (cena 6)',
  'nota': 'Último plano da temporada de teste: as duas canecas brindando contra a cidade.'},
]

OBJETOS = [
 {'id': 'bilhete', 'nome': 'O bilhete premiado', 'com': 'Dani',
  'look': ('Volante de loteria de papel cartão; seis dezenas marcadas à caneta azul (07 · 13 · 21 · 34 · 46 · 58); '
           'amassado, alisado de novo e manchado de caldo de feijão.'),
  'eps': 'Ep 1 · Ep 2 · Ep 3',
  'porque': 'O motor da série: R$ 212 milhões que quase viram tempero. Na produção, sempre "bilhete de loteria" genérico, sem logotipo.'},
 {'id': 'panela', 'nome': 'A panela de pressão', 'com': 'Dona Neusa',
  'look': 'Panela de pressão de alumínio fosco, amassada na frente, cabos pretos de baquelite, válvula de peso e pino vermelho.',
  'eps': 'Ep 1',
  'porque': 'Onde o bilhete cai: o absurdo da abertura. O apito da válvula é o som da série.'},
 {'id': 'lata', 'nome': 'A lata de café (cofrinho)', 'com': 'Dani (em cima da geladeira)',
  'look': 'Lata de café antiga, vermelho desbotado com faixa mostarda, tampa plástica fosca com fenda cortada à mão e fita adesiva.',
  'eps': 'Ep 1 · Ep 2 · Ep 3',
  'porque': 'Esconderijo do bilhete. Cléber quase a leva para comprar cerveja; Dani sai de casa abraçada a ela.'},
 {'id': 'caneca', 'nome': 'A caneca azul do Tiago', 'com': 'Tiago',
  'look': 'Caneca de ágata azul-cobalto com pintinhas brancas, borda preta lascada, cheia de açúcar até a boca.',
  'eps': 'Ep 1 · Ep 3',
  'porque': 'Símbolo do romance: "Precisando de açúcar... é só bater."'},
 {'id': 'oculos', 'nome': 'Os óculos do disfarce', 'com': 'Dani',
  'look': 'Óculos escuros enormes de acetato preto brilhante, lentes fumê quadradas e arredondadas, uma haste frouxa.',
  'eps': 'Ep 2 · Ep 3',
  'porque': 'Completam o look "Disfarce do banco"; ficam fora do sheet, como objeto de mão.'},
 {'id': 'papeis_divorcio', 'nome': 'Os papéis do divórcio', 'com': 'Cléber → Dani',
  'look': 'Três folhas A4 grampeadas, cláusulas numeradas e duas linhas de assinatura; a do Cléber já assinada em azul.',
  'eps': 'Ep 3',
  'porque': 'A cláusula que Cléber escreveu para "proteger os milhões dele" entrega a fortuna à Dani (licença dramática).'},
]

EPISODIOS = [
 {'n': 1, 'frase': ('Dani', 'Tá tudo bem. Tá tudo ótimo.'), 'titulo': 'O bilhete na panela de pressão', 'duracao': '2:00',
  'logline': 'Dani acerta as seis dezenas, mas a sogra joga o bilhete dentro da panela de feijão.',
  'absurdo': 'O bilhete de R$ 212 milhões voa por cima do ombro da sogra e cai na panela de pressão no instante do último número.',
  'humilhacao': 'Neusa chama Dani de encosto e Cléber a filma "surtando" para a internet, enquanto pede um PIX.',
  'virada': 'Com o bilhete salvo do feijão, Dani sorri e decide: ninguém vai saber.',
  'elenco': ['dani', 'neusa', 'cleber', 'tiago'], 'locacoes': ['cozinha_sala', 'corredor'],
  'objetos': ['bilhete', 'panela', 'lata', 'caneca'],
  'batidas': ['Dani confere o bilhete diante da TV: cinco números certos.',
              'Neusa amassa o bilhete e o joga, sem olhar, dentro da panela de pressão. A TV anuncia o sexto número.',
              'Dani esfria a panela na pia e tira o bilhete do feijão com a mão; Cléber filma tudo.',
              'O marido pede um PIX, a sogra sonha com Miami: Dani decide não contar e esconde o bilhete na lata de café.',
              'No corredor, Tiago oferece a caneca de açúcar. Primeiro sorriso dela na noite.',
              'Gancho: Cléber acha a lata e puxa o bilhete lá de dentro.'],
  'cenas': [
   {'n': 1, 'cab': 'INT. APARTAMENTO 301 — COZINHA E SALA — NOITE', 'tempo': '0:00–0:30', 'loc': 'cozinha_sala',
    'roteiro': '''
@Uma cozinha apertada de azulejo branco, iluminada por uma lâmpada nua. Na TV pequena, bolinhas numeradas giram num globo. No fogão, uma panela de pressão de alumínio amassada borbulha, a tampa aberta ao lado.
@DANI (28), caixa de supermercado, cachos castanhos na altura dos ombros, camiseta verde-sálvia desbotada, a sacola de compras ainda no braço, confere um bilhete de loteria contra a TV. As mãos tremem.
DANI | sussurrando | Zero sete... treze... vinte e um... trinta e quatro... quarenta e seis...
@DONA NEUSA (58), a sogra, blusa preta florida e argolas douradas, arranca o bilhete da mão dela.
DONA NEUSA | | Jogando o dinheiro do gás fora de novo, encosto?
@Neusa amassa o bilhete e o joga por cima do ombro, sem olhar. O papel gira no ar, em câmera lenta, e cai direto dentro da panela de feijão. Neusa fecha a tampa com um claque. A válvula começa a apitar.
TV | O.S. | ...e cinquenta e oito! Um único apostador acertou as seis dezenas!
@Dani congela. Olha para a TV. Olha para a panela.
DANI | | ...Cinquenta e oito.
'''},
   {'n': 2, 'cab': 'INT. APARTAMENTO 301 — COZINHA E SALA — CONTÍNUO', 'tempo': '0:30–1:15', 'loc': 'cozinha_sala',
    'roteiro': '''
@Dani se joga no fogão, apaga o fogo, carrega a panela apitando até a pia e abre a torneira de água fria por cima dela.
@No sofá, CLÉBER (32), o marido, camiseta branca, bermuda de moletom, chinelo com meia branca, ergue o celular na vertical e filma.
CLÉBER | para o celular | Gente, olha isso. Minha mulher tá brigando com uma panela. Comenta aí: surtou ou não surtou?
@O apito morre. Dani abre a tampa e mergulha a mão no feijão quente.
DANI | | Ai, ai, ai, ai!
@Ela puxa o bilhete pingando caldo marrom, assopra e o ergue contra a luz. Os números continuam lá.
DONA NEUSA | | Vai comer o papel agora? Cléber, a tua mulher é doida.
CLÉBER | sem tirar os olhos do celular | Amor, já que você tá de pé... faz um PIX pro seu homem? É pra impulsionar o perfil.
DONA NEUSA | | Se essa encosto tivesse um tostão, eu já tava morando em Miami.
@Dani olha para os dois. Olha para o bilhete. E sorri, devagar.
DANI | | Tá tudo bem. Tá tudo ótimo.
@Ela enfia o bilhete numa lata de café velha, o cofrinho da casa, e põe a lata em cima da geladeira.
'''},
   {'n': 3, 'cab': 'INT. CORREDOR DO 3º ANDAR — NOITE', 'tempo': '1:15–1:35', 'loc': 'corredor',
    'roteiro': '''
@Dani sai para o corredor e encosta na parede, respirando fundo. A porta do 302 se abre.
@TIAGO (30), o vizinho, camisa de chambray clara com as mangas dobradas, segura uma caneca azul de ágata cheia de açúcar.
TIAGO | | Ouvi uma panela gritando... Tá tudo bem, Dani?
DANI | | Tá tudo bem. Tá tudo ótimo.
TIAGO | estendendo a caneca, tímido | Precisando de açúcar... é só bater.
@Ela pega a caneca. Pela primeira vez na noite, ri de verdade.
'''},
   {'n': 4, 'cab': 'INT. APARTAMENTO 301 — COZINHA E SALA — NOITE', 'tempo': '1:35–2:00', 'loc': 'cozinha_sala',
    'roteiro': '''
@Dani volta com a caneca na mão. Cléber está em cima de um banquinho, sacudindo a lata de café. Moedas chacoalham. Um papel farfalha lá dentro.
CLÉBER | | Achei o cofrinho! Isso aqui dá pra uma cervejinha.
DANI | | Cléber. Larga essa lata.
@Ele abre a tampa e puxa o bilhete manchado de feijão.
CLÉBER | | Ué. Que papel é esse?
@Close no rosto de Dani. Congela.
'''},
  ],
  'gancho': 'Cléber está com o bilhete de R$ 212 milhões na mão, e não faz ideia do que segura.',
  'clipes': [
   (1, '0:00–0:15', 1, 'Plano fechado na TV e no bilhete; Dani recita os números, mãos trêmulas.'),
   (2, '0:15–0:30', 1, 'Neusa arranca, amassa e joga o bilhete; câmera lenta até a panela; a TV anuncia o 58.'),
   (3, '0:30–0:45', 2, 'Dani corre com a panela até a pia; Cléber filma na vertical do sofá.'),
   (4, '0:45–1:00', 2, 'Mão no feijão; o bilhete pingando contra a luz; Neusa zomba.'),
   (5, '1:00–1:15', 2, 'O PIX, Miami e o sorriso de Dani; o bilhete vai para a lata.'),
   (6, '1:15–1:35', 3, 'Corredor: Tiago e a caneca de açúcar.'),
   (7, '1:35–2:00', 4, 'Cléber no banquinho com a lata; "Que papel é esse?"; congela no rosto de Dani.'),
  ]},
 {'n': 2, 'frase': ('Seu Valter', 'A senhora está rica.'), 'titulo': 'Fui demitida (mentira)', 'duracao': '2:00',
  'logline': 'Para testar a família, Dani finge que foi demitida e vai ao banco disfarçada confirmar o prêmio.',
  'absurdo': 'Dani salta por cima do sofá como numa cena de ação para arrancar uma lata de moedas da mão do marido.',
  'humilhacao': 'Diante da "demissão", a sogra culpa o azar da nora e o marido quer vender o celular dela.',
  'virada': 'No banco: R$ 212 milhões, sozinha. Dani morde o bilhete como uma medalha de ouro.',
  'elenco': ['dani', 'cleber', 'neusa', 'tiago', 'valter', 'kelly'], 'locacoes': ['cozinha_sala', 'sala_ganhadores'],
  'objetos': ['bilhete', 'lata', 'oculos'], 'looks': {'dani': 'Disfarce do banco (cenas 3 e 4)'},
  'batidas': ['Cléber cheira o bilhete; Dani diz que é a lista do mercado.',
              'Dani salta o sofá, recupera a lata e anuncia: "Eu fui demitida."',
              'Neusa culpa o azar da nora; Cléber quer vender o celular dela.',
              'Tiago bate à porta com os R$ 800 do pneu da bicicleta. Dani devolve, emocionada.',
              'No banco, disfarçada, Dani ouve de Seu Valter: R$ 212 milhões, sozinha.',
              'Gancho: Cléber entra de mãos dadas com Kelly; Dani se esconde debaixo da mesa e é vista.'],
  'cenas': [
   {'n': 1, 'cab': 'INT. APARTAMENTO 301 — COZINHA E SALA — NOITE', 'tempo': '0:00–0:30', 'loc': 'cozinha_sala',
    'roteiro': '''
@Continuação. CLÉBER (32), de pé no banquinho, cheira o bilhete manchado.
CLÉBER | | Que nojo. Tá com cheiro de feijão.
@DANI (28), rápida:
DANI | | É a lista do mercado. Caiu na panela.
CLÉBER | | Eca.
@Ele joga o bilhete de volta na lata e enfia a mão nas moedas. Dani toma distância, salta por cima do sofá, voa e arranca a lata das mãos dele. Cai sentada no chão, abraçada à lata.
@Da cozinha, DONA NEUSA (58) larga a colher de pau.
DONA NEUSA | | Pulou o sofá? Por uma lata de moeda?
@Dani se levanta, ajeita os cachos e solta:
DANI | | Gente... eu fui demitida.
'''},
   {'n': 2, 'cab': 'INT. APARTAMENTO 301 — COZINHA E SALA — CONTÍNUO', 'tempo': '0:30–1:05', 'loc': 'cozinha_sala',
    'roteiro': '''
@Silêncio. A panela de pressão chia no fogão.
DONA NEUSA | | Demitida?! E o aluguel? Eu sabia. Encosto dá azar!
CLÉBER | | Amor... então vamos ter que vender o teu celular, né? Porque o meu é ferramenta de trabalho.
@Batidas na porta. Dani abre. TIAGO (30), envergonhado, estende um envelope.
TIAGO | | Desculpa, a parede é fina... Tem oitocentos reais aqui. Era pro pneu da bicicleta. Paga quando der.
@Cléber pega o envelope por cima do ombro de Dani.
CLÉBER | | Valeu, parceiro!
@Dani arranca o envelope de Cléber e o devolve a Tiago, com os olhos marejados.
DANI | | Guarda, Tiago. Eu vou dar um jeito.
TIAGO | | Precisando... é só bater.
'''},
   {'n': 3, 'cab': 'INT. AGÊNCIA BANCÁRIA — SALA RESERVADA — DIA', 'tempo': '1:05–1:35', 'loc': 'sala_ganhadores',
    'roteiro': '''
@A porta de vidro fosco se abre. Dani entra disfarçada: o trench coat caramelo da sogra, um lenço florido amarrado no queixo, óculos escuros enormes.
@SEU VALTER (55), o gerente, camisa azul de manga curta e gravata, fecha a porta atrás dela.
SEU VALTER | baixinho | Sigilo absoluto, senhora. Pode tirar os óculos.
@Dani tira os óculos e põe o bilhete manchado em cima da mesa. Valter o examina, cheira, passa o código no leitor. Empalidece.
SEU VALTER | | Dona Daniela... duzentos e doze milhões, trezentos e quarenta mil reais. Sozinha.
DANI | | Repete, Seu Valter.
SEU VALTER | | Duzentos e doze milhões.
DANI | | Repete.
SEU VALTER | | A senhora está rica.
@Dani morde o bilhete como uma medalha de ouro. Valter se abana com uma pasta.
'''},
   {'n': 4, 'cab': 'INT. AGÊNCIA BANCÁRIA — SALA RESERVADA — CONTÍNUO', 'tempo': '1:35–2:00', 'loc': 'sala_ganhadores',
    'roteiro': '''
@Valter vai buscar os documentos e abre a porta. Do outro lado do vidro, uma risada conhecida.
KELLY | O.S. | Amor, vem! O gerente vai liberar o empréstimo do nosso estúdio de conteúdo!
CLÉBER | O.S. | Fala baixo, Kelly. A minha mulher acha que eu tô no mercado.
@Dani recolhe o bilhete e mergulha debaixo da mesa. A porta se escancara. KELLY (27), rabo de cavalo platinado, conjunto de academia rosa-claro, entra filmando um story, de mãos dadas com Cléber.
KELLY | para o celular | Gente, sala VIP do banco. Olha o luxo!
@O tênis branco de Kelly para a dois palmos do rosto de Dani. Kelly abaixa o celular e olha para baixo da mesa.
KELLY | | Amor... aquela não é a sua mulher?
@Congela.
'''},
  ],
  'gancho': 'Kelly encontrou Dani escondida debaixo da mesa, com o bilhete de R$ 212 milhões na mão.',
  'clipes': [
   (1, '0:00–0:15', 1, 'Cléber cheira o bilhete; "lista do mercado"; ele joga de volta na lata.'),
   (2, '0:15–0:30', 1, 'O salto por cima do sofá; Dani no chão abraçada à lata; "Eu fui demitida."'),
   (3, '0:30–0:50', 2, 'Reações de Neusa e Cléber; batida na porta.'),
   (4, '0:50–1:05', 2, 'Tiago e o envelope; Cléber pega, Dani devolve.'),
   (5, '1:05–1:20', 3, 'Dani entra disfarçada; Seu Valter; o bilhete na mesa.'),
   (6, '1:20–1:35', 3, '"Duzentos e doze milhões... Repete... A senhora está rica." Dani morde o bilhete.'),
   (7, '1:35–2:00', 4, 'Vozes de Kelly e Cléber; Dani debaixo da mesa; "Aquela não é a sua mulher?"; congela.'),
  ]},
 {'n': 3, 'frase': ('Dani', 'Agora sim... começou.'), 'titulo': 'O divórcio mais rico do Brasil', 'duracao': '2:05',
  'logline': 'Cléber troca Dani pela milionária errada, assina a renúncia aos bens dela e a expulsa de casa.',
  'absurdo': 'Descoberta debaixo da mesa, Dani finge ser a faxineira, com voz de senhora, e sai esfregando o chão até a porta.',
  'humilhacao': 'Cléber troca Dani pela "milionária" e Neusa a põe para fora de casa com uma sacola.',
  'virada': 'Dani assina a renúncia sorrindo: quem abriu mão da fortuna foi ele. E o prédio agora é dela.',
  'elenco': ['dani', 'cleber', 'kelly', 'valter', 'neusa', 'tiago'],
  'locacoes': ['sala_ganhadores', 'cozinha_sala', 'corredor', 'laje'],
  'objetos': ['oculos', 'papeis_divorcio', 'lata', 'caneca'], 'looks': {'dani': 'Disfarce do banco (cenas 1 e 2)'},
  'batidas': ['Dani se finge de faxineira e escapa com o rodo; Kelly sente cheiro de feijão.',
              'Seu Valter, ao telefone, diz que a ganhadora estava naquela sala. Kelly não nega: "É sigilo."',
              'Cléber volta para casa com os papéis do divórcio e a cláusula de renúncia. Dani assina sorrindo.',
              'Neusa expulsa a nora; Tiago abre a porta com café.',
              'Kelly confessa que está falida; a TV anuncia que a ganhadora comprou o prédio; chega o aviso de despejo.',
              'Na laje, ao pôr do sol: "Agora sim... começou."'],
  'cenas': [
   {'n': 1, 'cab': 'INT. AGÊNCIA BANCÁRIA — SALA RESERVADA — DIA', 'tempo': '0:00–0:25', 'loc': 'sala_ganhadores',
    'roteiro': '''
@Continuação. CLÉBER (32) se abaixa para olhar. DANI (28), ainda de lenço e óculos escuros, faz uma voz fina de senhora.
DANI | voz fina | Limpeza, senhor. Tô tirando um chiclete aqui debaixo.
CLÉBER | | Kelly, a minha mulher nunca ia estar num banco. Ela não tem nem conta.
@Dani sai engatinhando, pega o rodo e o balde do canto e vai esfregando o chão até a porta. KELLY (27) fareja o ar.
KELLY | | Gente... que cheiro de feijão é esse?
'''},
   {'n': 2, 'cab': 'INT. AGÊNCIA BANCÁRIA — SALA RESERVADA — CONTÍNUO', 'tempo': '0:25–0:45', 'loc': 'sala_ganhadores',
    'roteiro': '''
@SEU VALTER (55) volta com uma pasta, falando ao celular, sem reparar no casal.
SEU VALTER | ao telefone | A ganhadora dos duzentos milhões estava nesta sala agorinha mesmo...
@Cléber se vira, devagar, para Kelly. Kelly, em vez de negar, joga o rabo de cavalo.
KELLY | | Eu não posso falar nada... é sigilo.
CLÉBER | | Kelly?!
'''},
   {'n': 3, 'cab': 'INT. APARTAMENTO 301 — COZINHA E SALA — NOITE', 'tempo': '0:45–1:10', 'loc': 'cozinha_sala',
    'roteiro': '''
@Cléber entra de peito estufado e bate uns papéis grampeados na mesa. DONA NEUSA (58) assiste de braços cruzados.
CLÉBER | | Dani, acabou. Achei uma mulher do meu nível.
DANI | lendo em voz alta | "...e cada um renuncia a qualquer bem, presente ou futuro, do outro."
CLÉBER | | Isso. Pra você não vir atrás dos meus milhões.
@Dani pega a caneta, assina com um floreio e sorri.
DANI | | Tá tudo bem. Tá tudo ótimo.
DONA NEUSA | abrindo a porta | Agora pega as tuas coisas e some daqui, encosto!
@Dani sai com uma sacola numa mão e a lata de café debaixo do braço.
'''},
   {'n': 4, 'cab': 'INT. CORREDOR DO 3º ANDAR — NOITE', 'tempo': '1:10–1:20', 'loc': 'corredor',
    'roteiro': '''
@A porta do 302 se abre. TIAGO (30) aparece com duas canecas fumegando.
TIAGO | | Fiz café agora. Quer?
DANI | | Com açúcar?
TIAGO | | Muito açúcar.
'''},
   {'n': 5, 'cab': 'INT. CORREDOR DO 3º ANDAR — NOITE', 'tempo': '1:20–1:45', 'loc': 'corredor',
    'roteiro': '''
@Na escada, Kelly cochicha com Cléber, que carrega uma mala.
KELLY | | Amor, eu tenho quarenta mil seguidores... e trinta e oito reais na conta.
CLÉBER | | Como assim? Você não é a ganhadora?!
KELLY | | Eu disse que era sigilo!
@Pela porta aberta do 301, a TV.
TV | O.S. | A ganhadora misteriosa dos duzentos e doze milhões comprou hoje um prédio inteiro na Zona Leste...
@Neusa recolhe um papel enfiado debaixo da porta e lê, pálida.
DONA NEUSA | | "A nova proprietária pede o imóvel em trinta dias." ...Quem é a nova dona?!
'''},
   {'n': 6, 'cab': 'EXT. LAJE DO PRÉDIO — PÔR DO SOL', 'tempo': '1:45–2:05', 'loc': 'laje',
    'roteiro': '''
@Dani e Tiago nas cadeiras de plástico, canecas na mão, a cidade alaranjada à frente.
TIAGO | | Dizem que a dona nova do prédio é muito rica.
DANI | | Dizem que ela gosta de açúcar.
@Ela bate a caneca na dele e olha a cidade.
DANI | | Agora sim... começou.
'''},
  ],
  'gancho': 'Dani é a dona do prédio de onde acabou de ser expulsa, e ninguém lá embaixo sabe.',
  'clipes': [
   (1, '0:00–0:15', 1, 'Voz fina de faxineira; "ela não tem nem conta".'),
   (2, '0:15–0:30', 1, 'Dani sai esfregando com o rodo; Kelly sente cheiro de feijão.'),
   (3, '0:30–0:45', 2, 'Seu Valter ao telefone; "É sigilo"; "Kelly?!"'),
   (4, '0:45–1:10', 3, 'Os papéis do divórcio; Dani lê a cláusula, assina e sorri; Neusa a expulsa.'),
   (5, '1:10–1:20', 4, 'Corredor: "Fiz café agora." "Com açúcar?" "Muito açúcar."'),
   (6, '1:20–1:45', 5, 'Kelly falida; a TV e o prédio; Neusa lê o aviso de despejo.'),
   (7, '1:45–2:05', 6, 'Laje ao pôr do sol: o brinde e "Agora sim... começou."'),
  ]},
]
