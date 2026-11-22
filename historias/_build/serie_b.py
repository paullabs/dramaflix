# -*- coding: utf-8 -*-
# Bíblia da série B — "Casei com o Mendigo e Ele Era Dono do Banco"
# Roteiro em mini-marcação: linha "@..." = ação; "NOME | parentético | fala" = diálogo.

SERIE = {
 'slug': 'casei-com-o-mendigo',
 'letra': 'B',
 'titulo': 'Casei com o Mendigo e Ele Era Dono do Banco',
 'capa': 'capas/v3/12-casei-com-o-mendigo.png',
 'logo': 'capas/v3/titulos/12.png',
 'banner': 'capas/banners/12-casei-com-o-mendigo.png',
 'cor': '#C9A45C',
 'genero': 'Romance · Casamento por impulso · Bilionário disfarçado',
 'formato': '3 episódios de teste · cerca de 2 min cada · vertical 9:16 · live action',
 'look_id': 'realism_cinematic',
 'logline': ('No altar de um casamento arranjado para pagar as dívidas do pai, uma arquiteta larga o noivo milionário '
             'e se casa com o primeiro homem que vê do portão: um morador de rua de barba enorme. Ela não sabe que ele '
             'é o herdeiro desaparecido do banco que vai cobrar a dívida da família.'),
 'gancho': ('Diante de 200 convidados, a noiva diz "não" ao noivo, atravessa o jardim e pede em casamento o mendigo '
            'que espiava o bolo pelo portão. "Tem bolo?" "Três andares." "Aceito." A aliança é o lacre de uma latinha.'),
 'tom': ('Conto de fadas de short drama com humor seco: humilhação pública, revelação em câmera lenta e réplicas '
         'curtas. Cada episódio abre com um absurdo e fecha num rosto congelado.'),
 'temas': ['O valor de alguém não está no sobrenome', 'Escolher a própria vida', 'Orgulho custa caro',
           'Quem te olha nos olhos quando você não tem nada'],
 'publico': 'Fãs de romance, novela e short drama de CEO disfarçado, 18 a 55 anos, mobile first, PT-BR.',
 'look': ('Romance em tom alto: o dourado do pôr do sol no casamento, o laranja do poste de sódio na praça, a luz '
          'de vitrine na barbearia e o contraluz frio da torre do banco. Luz e cenário fazem o clima, nada de filtro.'),
 'sinopse': [
   ('Laura Valente, 27 anos, arquiteta, vai se casar com Henrique Lacerda, herdeiro de uma incorporadora, porque o '
    'pai, Augusto, deve R$ 300 milhões ao Banco Monteiro e o noivo prometeu pagar. No altar, ao ver Henrique '
    'conferir o celular enquanto o juiz pergunta se ela aceita, Laura diz "não".'),
   ('Pelo portão aberto do jardim, ela vê um morador de rua de barba enorme, de olho no bolo. Atravessa o '
    'corredor e o pede em casamento. Ele aceita, pelo bolo. Dobra em rosa a nota de cem que o noivo atira nele, '
    'faz uma aliança com o lacre de uma latinha e assina o livro: Teodoro Albuquerque Monteiro. "Coincidência."'),
   ('Expulsa de casa pelo pai, Laura passa a noite de núpcias num banco de praça, comendo miojo com um homem que '
    'fala de juros e cita francês. Ao ler a notificação da dívida, Téo percebe o que ninguém viu: ela foi comprada '
    'por uma empresa de fachada. Na barbearia, a barba cai, e a avó dele, Dona Celeste, presidente do conselho '
    'do banco, entra pela porta.'),
   ('Na reunião de cobrança, a cadeira da presidência gira: o "mendigo" é o novo presidente do Banco Monteiro. Ele '
    'desmascara Henrique como dono secreto da dívida, congela a cobrança com uma condição para o sogro e enfrenta '
    'o ultimato da avó: anular o casamento ou perder o banco.'),
 ],
 'arco': [
   {'ep': 1, 'titulo': 'Aceito (tem bolo?)',
    'resumo': 'Laura recusa o noivo e casa com o mendigo do portão; a assinatura no livro diz "Monteiro".',
    'gancho': 'O motorista dos Monteiro liga para a avó: "Encontrei o seu neto. Ele acabou de se casar."'},
   {'ep': 2, 'titulo': 'A noite na praça',
    'resumo': 'Expulsa de casa, Laura passa a noite com Téo na praça; ele lê a dívida e raspa a barba.',
    'gancho': 'A avó entra na barbearia; Laura não reconhece o marido barbeado: "Laura. Sou eu."'},
   {'ep': 3, 'titulo': 'A reunião de cobrança',
    'resumo': 'A cadeira da presidência gira; Henrique cai; o pai de Laura engole o orgulho.',
    'gancho': 'Ultimato da avó, e a resposta de Téo: "Vó... então pode ficar com o banco."'},
 ],
 'curva': [('Ep 1', 'mendigo', 12), ('Ep 2', 'barba feita', 45), ('Ep 3', 'presidente', 95)],
 'regras': [
   'Um absurdo nos primeiros 15 segundos de cada episódio: a noiva troca de noivo, as malas voam por cima do portão, a cadeira que gira.',
   'Humilhação pública do "pobre" antes de cada pista da riqueza: a rosa de cem reais, o relógio gravado, o cartão preto.',
   'O público descobre antes da Laura: cada cena planta uma prova de quem o Téo é de verdade.',
   'Réplicas curtas e bordões: "Eu escolho.", "Tudo tem preço.", "Um Valente não implora.", "Monteiro não se esconde."',
   'Todo episódio termina num rosto congelado e numa escolha.',
 ],
}

PERSONAGENS = [
 {'id': 'laura', 'nome': 'Laura', 'completo': 'Laura Valente', 'idade': 27,
  'lado': 'Protagonista', 'role': 'pure_heart', 'role_pt': 'O coração puro', 'status': 'baixo · natural',
  'rota': 'foto', 'imagens': {'sheet': 'laura_sheet', 'rosto': '_refs/laura-rosto.jpg'},
  'leitura': ('A noiva vendida para pagar a dívida do pai, que prefere casar com um desconhecido a se perder; o público '
              'ama a coragem e a bondade dela.'),
  'aparencia': ('Mulher brasileira parda; pele oliva clara; olhos castanhos; cabelo castanho-escuro longo, passando dos '
                'ombros, ondulado, solto com risca lateral e ondas jogadas para um lado; corpo esguio, com curvas naturais.'),
  'figurino': ['Vestido de noiva de cetim marfim cortado no viés, alças finas e decote reto',
               'Echarpe longa de chiffon marfim no pescoço, caindo sobre um ombro', 'Sandália de salto marfim',
               'Brincos de gota prateados'],
  'voz': 'Mulher, 27 anos, voz média e suave, firme quando decide; sotaque paulistano de classe alta, sem afetação; fala pausada.',
  'voz_en': 'woman, 27, soft mid-range voice that turns firm when she decides, educated São Paulo accent, unhurried',
  'personalidade': ('Arquiteta idealista, gentil com todo mundo (com o garçom, com o porteiro, com o mendigo) e teimosa '
                    'como o pai. Odeia ser tratada como moeda de troca.'),
  'objetivo': 'Escolher a própria vida e salvar a empresa do pai sem se vender.',
  'segredo': 'Desenhou, escondida, um projeto para transformar a fábrica falida do pai em moradia popular.',
  'arco': ['Ep 1: recusa o noivo no altar e casa com o mendigo.',
           'Ep 2: expulsa de casa, passa a noite na praça e descobre quem é o marido.',
           'Ep 3: confronta Téo, "Você mentiu", e vê ele escolher ela no lugar do banco.'],
  'bordao': 'Eu escolho.',
  'relacoes': ['Filha de Augusto', 'Noiva rejeitada de Henrique', 'Esposa de Téo', 'Dona Celeste vira sua "avó" hostil'],
  'eps': [1, 2, 3],
 },
 {'id': 'teo', 'nome': 'Téo', 'completo': 'Teodoro Albuquerque Monteiro', 'idade': 31,
  'lado': 'Protagonista', 'role': 'underdog', 'role_pt': 'O subestimado', 'status': 'baixo → alto',
  'rota': 'foto', 'imagens': {'sheet': 'teo_sheet', 'rosto': '_refs/teo-rosto.jpg'},
  'leitura': ('O mendigo barbudo de quem os convidados riem, secretamente o herdeiro desaparecido do maior banco do país; '
              'o público espera a revelação.'),
  'aparencia': ('Homem brasileiro branco; pele clara de subtom quente; olhos castanho-esverdeados; cabelo castanho-escuro '
                'grosso e ondulado na altura dos ombros, desgrenhado; barba castanho-escura enorme, cheia e sem aparar; '
                'alto e esguio.'),
  'figurino': ['Sobretudo longo de lã marrom, gasto, punhos puídos e um botão faltando', 'Henley cinza desbotada por baixo',
               'Calça escura gasta', 'Botas de couro marrom arranhadas', 'Luvas de tricô pretas sem dedos',
               'Relógio de ouro antigo no pulso esquerdo (a única pista da fortuna)'],
  'voz': 'Homem, 31 anos, voz grave e calma, dicção culta, sotaque paulistano neutro, humor seco; solta frases em francês.',
  'voz_en': 'man, 31, calm deep voice, cultured diction, neutral São Paulo accent, dry humour, drops French phrases',
  'personalidade': ('Culto, irônico, observador e gentil com quem ninguém olha. Sumiu da própria vida para descobrir quem o '
                    'trataria como gente sem o sobrenome.'),
  'objetivo': 'Desmascarar quem conspirou contra ele no banco e, agora, proteger a Laura.',
  'segredo': ('É o herdeiro do Banco Monteiro, desaparecido há dois anos, depois de descobrir um esquema de dívidas '
              'compradas por empresas de fachada.'),
  'arco': ['Ep 1: aceita casar "pelo bolo".', 'Ep 2: passa a noite com Laura na praça e raspa a barba.',
           'Ep 3: assume a presidência, derruba Henrique e escolhe Laura no lugar do banco.'],
  'bordao': 'Dinheiro não compra quem eu sou. Mas compra uma dívida.',
  'relacoes': ['Marido de Laura', 'Neto de Dona Celeste', 'Osvaldo, o motorista, quase um pai', 'Inimigo de Henrique'],
  'eps': [1, 2, 3],
  'looks': [{'id': 'teo_look_presidente', 'nome': 'O presidente', 'eps': 'Ep 3 (todas as cenas)',
             'objetos': ['relogio'], 'muda': ('Rosto novo (edição aprovada): barba toda raspada, cabelo curto nas laterais e penteado para trás. '
                      'Terno grafite de três peças em lã fria, camisa branca, gravata de seda grafite, oxford preto, o mesmo '
                      'relógio de ouro e um anel de sinete liso.'),
             'rosto': 'teo_face_edit2'}],
 },
 {'id': 'henrique', 'nome': 'Henrique', 'completo': 'Henrique Lacerda', 'idade': 35,
  'lado': 'Antagonista', 'role': 'impostor', 'role_pt': 'O impostor', 'status': 'alto · encenado',
  'rota': 'figurino', 'imagens': {'sheet': 'henrique_sheet', 'rosto': 'henrique_face', 'figurino': 'henrique_outfit'},
  'leitura': ('O noivo polido que posa de salvador da família enquanto é, em segredo, o dono da dívida; o público quer '
              'vê-lo desmascarado.'),
  'aparencia': ('Homem brasileiro branco; pele clara; olhos azul-acinzentados; cabelo preto curto e liso, penteado para '
                'trás com pomada; barba feita; alto e atlético.'),
  'figurino': ['Smoking marfim de gola xale em lã fina', 'Camisa branca de peito plissado', 'Gravata-borboleta de seda preta',
               'Calça preta com faixa de cetim', 'Abotoaduras de ouro', 'Oxford preto de verniz', 'Botão de rosa branca na lapela'],
  'voz': 'Homem, 35 anos, voz média-grave, macia e arrogante, sotaque paulistano de mercado financeiro; ri pelo nariz.',
  'voz_en': 'man, 35, smooth mid-low voice, arrogant, upscale São Paulo finance accent, laughs through his nose',
  'personalidade': 'Charmoso em público e frio em particular; mede tudo, e todos, em dinheiro.',
  'objetivo': 'Casar com Laura para ficar com a fábrica dos Valente por quase nada.',
  'segredo': 'Comprou a dívida de R$ 300 milhões por meio de uma empresa de fachada: o credor é ele.',
  'arco': ['Ep 1: humilhado no altar.', 'Ep 2: tenta comprar Laura de volta na praça.', 'Ep 3: desmascarado e posto para fora do banco.'],
  'bordao': 'Tudo tem preço.',
  'relacoes': ['Noivo rejeitado de Laura', '"Aliado" de Augusto', 'Inimigo de Téo'],
  'eps': [1, 2, 3],
 },
 {'id': 'augusto', 'nome': 'Augusto', 'completo': 'Augusto Valente', 'idade': 60,
  'lado': 'Antagonista', 'role': 'oppressor', 'role_pt': 'O opressor', 'status': 'alto · exibido',
  'rota': 'figurino', 'imagens': {'sheet': 'augusto_sheet', 'rosto': 'augusto_face', 'figurino': 'augusto_outfit'},
  'leitura': 'O patriarca orgulhoso e falido que vende a mão da filha para salvar a empresa; o público quer vê-lo humilhado.',
  'aparencia': ('Homem brasileiro branco; pele clara e corada; olhos castanhos; cabelo grisalho prateado, curto e penteado '
                'para trás; bigode grisalho bem aparado; corpo largo, um pouco pesado.'),
  'figurino': ['Terno preto de três peças em lã fina', 'Camisa branca', 'Gravata de seda cor de vinho com prendedor dourado',
               'Lenço de bolso vinho', 'Relógio de ouro pesado'],
  'voz': 'Homem, 60 anos, voz grave e alta, sotaque paulistano antigo; fala sempre em tom de discurso.',
  'voz_en': 'man, 60, loud deep voice, old-money São Paulo accent, speaks as if giving a speech',
  'personalidade': 'Vaidoso, autoritário e apegado ao sobrenome; ama a filha do jeito errado.',
  'objetivo': 'Salvar a Valente Têxtil e as aparências.',
  'segredo': 'Está falido há três anos e hipotecou até a mansão.',
  'arco': ['Ep 1: empurra a filha para o casamento.', 'Ep 2: joga as malas dela por cima do portão.',
           'Ep 3: descobre que o "mendigo" é o banco e engole o orgulho.'],
  'bordao': 'Um Valente não implora.',
  'relacoes': ['Pai de Laura', 'Devedor do Banco Monteiro', 'Cúmplice enganado de Henrique'],
  'eps': [1, 2, 3],
 },
 {'id': 'celeste', 'nome': 'Dona Celeste', 'completo': 'Celeste Monteiro', 'idade': 74,
  'lado': 'Secundária', 'role': 'witness', 'role_pt': 'A testemunha', 'status': 'médio · funcional',
  'rota': 'figurino', 'imagens': {'sheet': 'celeste_sheet', 'rosto': 'celeste_face', 'figurino': 'celeste_outfit'},
  'leitura': 'A matriarca gelada do banco que revela quem o neto é de verdade e julga a noiva; o público teme o veredito dela.',
  'aparencia': ('Mulher brasileira branca; pele clara; olhos azul-acinzentados; cabelo branco-prateado liso em chanel na '
                'altura do queixo; corpo esguio e ereto.'),
  'figurino': ['Tailleur de bouclé grafite (blazer e saia)', 'Blusa de seda marfim', 'Colar de pérolas de duas voltas',
               'Brincos de pérola', 'Scarpin baixo preto'],
  'voz': 'Mulher, 74 anos, voz baixa, seca e precisa, sotaque paulistano tradicional; nunca levanta o tom.',
  'voz_en': 'woman, 74, low dry precise voice, traditional São Paulo accent, never raises her tone',
  'personalidade': 'Fria e estrategista, leal ao nome da família; esconde a saudade do neto atrás das regras.',
  'objetivo': 'Trazer o Teodoro de volta e proteger o banco.',
  'segredo': 'Guarda há dois anos a carta de demissão que o neto deixou, e nunca a entregou ao conselho.',
  'arco': ['Ep 1: descobre o casamento pelo telefone.', 'Ep 2: encontra o neto na barbearia.',
           'Ep 3: dá o ultimato: o banco ou a Laura.'],
  'bordao': 'Monteiro não se esconde.',
  'relacoes': ['Avó de Téo', 'Presidente do conselho do banco', 'Patroa de Osvaldo'],
  'eps': [1, 2, 3],
 },
 {'id': 'osvaldo', 'nome': 'Osvaldo', 'completo': 'Osvaldo Ferreira', 'idade': 62,
  'lado': 'Secundário', 'role': 'witness', 'role_pt': 'A testemunha', 'status': 'médio · funcional',
  'rota': 'figurino', 'imagens': {'sheet': 'osvaldo_sheet', 'rosto': 'osvaldo_face', 'figurino': 'osvaldo_outfit'},
  'leitura': 'O motorista fiel da família que reconhece o herdeiro pelo relógio e faz a ligação que muda tudo.',
  'aparencia': ('Homem brasileiro negro; pele marrom-escura; olhos castanho-escuros; cabelo grisalho crespo bem rente; '
                'barba grisalha curta e bem feita; alto e sólido.'),
  'figurino': ['Terno preto de motorista', 'Camisa branca', 'Gravata preta', 'Quepe preto de motorista', 'Sapato preto engraxado'],
  'voz': 'Homem, 62 anos, voz grave e calorosa, sotaque mineiro leve; fala pouco e com respeito.',
  'voz_en': 'man, 62, warm deep voice, light Minas Gerais accent, speaks little and respectfully',
  'personalidade': 'Leal e paciente; enxerga tudo e fala pouco.',
  'objetivo': 'Levar o Teodoro para casa.',
  'segredo': 'Sabia o tempo todo que Téo estava vivo: recebia um cartão-postal sem remetente todo Natal.',
  'arco': ['Ep 1: encontra Téo e liga para Dona Celeste.', 'Ep 2: leva a patroa até a barbearia.',
           'Ep 3: acompanha Henrique até a rua.'],
  'bordao': 'Sim, senhora.',
  'relacoes': ['Motorista dos Monteiro há 30 anos', 'Quase um pai para Téo'],
  'eps': [1, 2, 3],
 },
 {'id': 'juiz', 'nome': 'Juiz de paz', 'completo': 'Seu Amâncio, o juiz de paz', 'idade': 66,
  'lado': 'Funcional', 'role': 'functional', 'role_pt': 'O funcional', 'status': 'médio',
  'rota': 'figurino', 'imagens': {'sheet': 'juiz_sheet', 'rosto': 'juiz_face', 'figurino': 'juiz_outfit'},
  'leitura': 'O juiz de paz atrapalhado que casa a noiva com um mendigo e repara num sobrenome famoso no livro.',
  'aparencia': ('Homem brasileiro branco; pele clara e rosada; olhos azuis; careca no alto, com uma coroa de cabelo branco '
                'nas laterais; barba feita; baixo e redondo.'),
  'figurino': ['Terno de linho bege', 'Camisa branca', 'Gravata-borboleta vinho', 'Sapato de couro marrom'],
  'voz': 'Homem, 66 anos, voz aguda e cerimoniosa, sotaque paulistano; pigarreia antes de falar.',
  'voz_en': 'man, 66, high ceremonious voice, São Paulo accent, clears his throat before speaking',
  'personalidade': 'Formal, adora um protocolo e morre de medo de confusão.',
  'objetivo': 'Terminar a cerimônia sem escândalo (não consegue).',
  'segredo': 'Nunca tinha visto uma noiva trocar de noivo no altar, e vai contar essa história até morrer.',
  'arco': ['Ep 1: casa Laura e Téo e lê "Monteiro" no livro.'],
  'bordao': 'Maiores de idade... documentos em ordem...',
  'relacoes': ['Contratado por Augusto para o casamento'],
  'eps': [1],
 },
 {'id': 'barbeiro', 'nome': 'Seu Nenê', 'completo': 'Seu Nenê, o barbeiro', 'idade': 70,
  'lado': 'Funcional', 'role': 'functional', 'role_pt': 'O funcional', 'status': 'baixo',
  'rota': 'figurino', 'imagens': {'sheet': 'barbeiro_sheet', 'rosto': 'barbeiro_face', 'figurino': 'barbeiro_outfit'},
  'leitura': 'O velho barbeiro que raspa o mendigo e quase desmaia com o cartão preto.',
  'aparencia': ('Homem brasileiro pardo; pele morena média; olhos castanhos; cabelo branco curto e cacheado; bigode branco '
                'grosso; magro e um pouco curvado.'),
  'figurino': ['Jaleco branco de barbeiro, manga curta, abotoado de lado', 'Calça preta', 'Sapato preto'],
  'voz': 'Homem, 70 anos, voz rouca e animada, sotaque paulistano antigo; fala cantando.',
  'voz_en': 'man, 70, raspy cheerful voice, old São Paulo accent, sing-song',
  'personalidade': 'Falador, curioso e orgulhoso da navalha.',
  'objetivo': 'Fazer a melhor barba da vida dele.',
  'segredo': 'Reconhece o rosto da capa da revista antes de todo mundo, e fica quieto.',
  'arco': ['Ep 2: raspa a barba de Téo e vê o cartão preto.'],
  'bordao': 'Navalha não mente.',
  'relacoes': ['Barbeiro do bairro da praça'],
  'eps': [2],
 },
]

RELACOES = [
 ('laura', 'teo', 'casaram no ato'), ('augusto', 'laura', 'pai que a "vendeu"'), ('henrique', 'laura', 'noivo rejeitado'),
 ('henrique', 'augusto', 'dono secreto da dívida'), ('celeste', 'teo', 'avó e neto'), ('osvaldo', 'teo', 'o reconhece'),
 ('juiz', 'laura', 'celebra o casamento'), ('barbeiro', 'teo', 'raspa a barba'),
]

LOCACOES = [
 {'id': 'jardim_mansao', 'nome': 'Jardim da mansão Valente — o casamento', 'hora': 'Pôr do sol',
  'look': ('Jardim de mansão em São Paulo montado para casamento: arco de rosas brancas, corredor de tapete branco, '
           'cadeiras com laços de tule, gazebo com bolo de três andares e um portão de ferro que dá para a praça.'),
  'luz': ['Sol dourado baixo atrás das árvores (principal)', 'Varais de lâmpadas acesos sobre o corredor', 'Lanternas no gazebo'],
  'mapa': {'Esquerda': 'Gazebo branco com o bolo de três andares', 'Direita': 'Fileiras de cadeiras brancas com laços de tule',
           'Fundo': 'Arco de flores e, atrás, muro de hera com o portão de ferro para a rua e a praça',
           'Frente': 'Início do corredor de tapete branco'},
  'eps': 'Ep 1 (cenas 1 a 3; a cena 4 do lado de fora do portão)',
  'nota': 'No Ep 1 o portão fica aberto do começo ao fim (Téo espia o bolo por ele): pedir a variação "portão aberto" na produção.'},
 {'id': 'praca', 'nome': 'Praça dos Ipês', 'hora': 'Noite',
  'look': ('Praça arborizada em frente à mansão: ipês-rosa floridos, calçada de pedra portuguesa ondulada, banco verde '
           'de madeira, banca de jornal fechada e o carrinho de supermercado com os cobertores do Téo.'),
  'luz': ['Poste com luz de sódio laranja sobre o banco (principal)', 'Janelas frias da mansão do outro lado da rua'],
  'mapa': {'Esquerda': 'Banca de jornal verde, fechada', 'Direita': 'Banco verde de madeira e o carrinho com os cobertores',
           'Fundo': 'A rua e o muro branco da mansão com o portão de ferro', 'Frente': 'Canteiro de pedra com ipês'},
  'eps': 'Ep 2 (cenas 1 a 3)',
  'nota': 'O "banco" de que Téo fala ("Eu tenho um banco") é o banco verde da praça.'},
 {'id': 'barbearia', 'nome': 'Barbearia do Seu Nenê', 'hora': 'Dia',
  'look': ('Barbearia antiga de bairro: piso xadrez preto e branco, cadeira de barbeiro vermelha com cromados, espelho '
           'grande, sofá de espera de couro e revisteiro.'),
  'luz': ['Luz do dia pela vitrine (principal)', 'Luminárias de globo leitoso', 'Arandelas dos dois lados do espelho'],
  'mapa': {'Esquerda': 'Espelho grande, bancada de mármore e a cadeira vermelha', 'Direita': 'Sofá de couro marrom e revisteiro de madeira',
           'Fundo': 'Prateleiras com frascos e toalhas e a porta dos fundos', 'Frente': 'Vitrine e porta de vidro com sininho'},
  'eps': 'Ep 2 (cena 4)',
  'nota': 'A revista com a capa "Onde está o herdeiro do Banco Monteiro?" fica no revisteiro, ao alcance de Laura.'},
 {'id': 'sala_presidencia', 'nome': 'Sala da presidência do Banco Monteiro', 'hora': 'Dia',
  'look': ('Sala de reuniões no último andar de uma torre de vidro: mesa longa de madeira escura, doze cadeiras de couro, '
           'janelas do chão ao teto sobre São Paulo e a cadeira presidencial de costas para a sala.'),
  'luz': ['Luz do dia em contraluz pelas janelas (principal)', 'Pendentes lineares sobre a mesa'],
  'mapa': {'Esquerda': 'Parede de madeira escura com porta dupla de maçanetas de latão', 'Direita': 'Aparador com garrafa e copos de cristal',
           'Fundo': 'Janelas do chão ao teto e a cadeira presidencial virada para a cidade', 'Frente': 'A cabeceira próxima da mesa'},
  'eps': 'Ep 1 (cena 4, Dona Celeste ao telefone) · Ep 3 (cenas 1 a 4)',
  'nota': 'O giro da cadeira é o plano-assinatura da série: a cadeira começa de costas, sempre.'},
]

OBJETOS = [
 {'id': 'relogio', 'nome': 'O relógio de ouro', 'com': 'Téo',
  'look': 'Relógio de pulso antigo de ouro amarelo, pulseira de couro marrom rachada, tampa traseira gravada "T.M. 1952".',
  'eps': 'Ep 1 · Ep 2 · Ep 3',
  'porque': 'A única pista da fortuna de Téo. Osvaldo o reconhece por ele; Laura lê a gravação na praça.'},
 {'id': 'anel_latinha', 'nome': 'A aliança de latinha', 'com': 'Laura',
  'look': 'Anel feito com o lacre de uma lata de refrigerante, alumínio prateado, com um lacinho de fita de cetim marfim.',
  'eps': 'Ep 1 · Ep 2 · Ep 3',
  'porque': 'A aliança do casamento-relâmpago. Laura nunca tira, nem quando descobre a verdade.'},
 {'id': 'rosa_nota', 'nome': 'A rosa de cem reais', 'com': 'Téo → Laura',
  'look': 'Rosa de origami dobrada com uma cédula azul-acinzentada, pétalas em espiral, caule enrolado e uma folha.',
  'eps': 'Ep 1',
  'porque': 'Henrique atira a nota para humilhar; Téo a devolve como presente à noiva. Primeira prova de que ele não é quem parece.'},
 {'id': 'livro_registro', 'nome': 'O livro de registro', 'com': 'Juiz de paz',
  'look': 'Livro de casamentos encadernado em couro verde-escuro com douração gasta, páginas creme pautadas, duas assinaturas novas.',
  'eps': 'Ep 1',
  'porque': 'A assinatura "Teodoro A. Monteiro": "Monteiro como o banco?" "Coincidência."'},
 {'id': 'notificacao_divida', 'nome': 'A notificação da dívida', 'com': 'Laura',
  'look': 'Carta oficial em papel encorpado, timbre azul-marinho, valor em destaque R$ 300.000.000,00 sublinhado em vermelho, carimbo vermelho.',
  'eps': 'Ep 2 · Ep 3',
  'porque': 'Explica o casamento arranjado; lendo-a, Téo percebe a empresa de fachada.'},
 {'id': 'cartao_preto', 'nome': 'O cartão preto', 'com': 'Téo',
  'look': 'Cartão de pagamento de metal preto escovado, chip dourado, números em relevo prata-escuro.',
  'eps': 'Ep 2',
  'porque': 'Pista da identidade: o barbeiro vê, Laura não.'},
]

EPISODIOS = [
 {'n': 1, 'frase': ('Téo', '...Tem bolo?'), 'titulo': 'Aceito (tem bolo?)', 'duracao': '2:00',
  'logline': 'No altar, Laura recusa o noivo milionário e casa com o mendigo que espiava o bolo pelo portão.',
  'absurdo': 'A noiva larga o noivo no altar e pede em casamento um morador de rua; ele só quer saber se tem bolo.',
  'humilhacao': 'Henrique atira uma nota de cem no "mendigo" diante de duzentos convidados.',
  'virada': 'Téo transforma a nota numa rosa e assina "Monteiro" no livro: "Coincidência."',
  'elenco': ['laura', 'henrique', 'juiz', 'augusto', 'teo', 'osvaldo', 'celeste'],
  'locacoes': ['jardim_mansao', 'sala_presidencia'], 'objetos': ['rosa_nota', 'anel_latinha', 'livro_registro', 'relogio'],
  'batidas': ['O juiz pergunta; o pai cochicha "trezentos milhões"; o noivo confere o celular.',
              'Laura diz "não" e aponta o homem de barba no portão.',
              '"Tem bolo?" "Três andares." "Aceito."',
              'Henrique atira uma nota de cem; Téo a dobra em rosa para a noiva. A aliança vem de uma latinha.',
              'A assinatura no livro: "Monteiro como o banco?" "Coincidência."',
              'Gancho: Osvaldo reconhece o relógio e liga para Dona Celeste.'],
  'cenas': [
   {'n': 1, 'cab': 'EXT. JARDIM DA MANSÃO VALENTE — PÔR DO SOL', 'tempo': '0:00–0:45', 'loc': 'jardim_mansao',
    'roteiro': '''
@Um casamento de revista: arco de rosas brancas, cadeiras com laços de tule, um bolo branco de três andares sob o gazebo. Duzentos convidados. O portão de ferro do fundo está aberto para a praça.
@No altar, LAURA (27), arquiteta, vestido de cetim marfim e echarpe de chiffon, segura o buquê como quem segura uma granada. Ao lado dela, HENRIQUE (35), smoking marfim impecável, confere o celular.
@O JUIZ DE PAZ (66), terno de linho bege e gravata-borboleta vinho, pigarreia e abre o livro de registro.
JUIZ DE PAZ | | Laura Valente, aceita Henrique Lacerda como seu legítimo esposo?
@Da primeira fila, AUGUSTO (60), o pai, terno preto de três peças e gravata cor de vinho, cochicha entre os dentes.
AUGUSTO | | Diz sim, filha. São trezentos milhões.
@Laura olha para o noivo. Henrique nem levanta os olhos do celular.
LAURA | | Não.
@Os convidados prendem a respiração.
LAURA | | Eu caso. Mas não com ele.
@Ela olha para o portão aberto. Ali, encostado na grade, TÉO (31), barba enorme, cabelo selvagem, sobretudo marrom surrado e luvas sem dedos, olha fixo para o bolo. Laura atravessa o corredor inteiro e para na frente dele.
LAURA | | Você. Quer casar comigo?
TÉO | | ...Tem bolo?
LAURA | | Três andares.
TÉO | | Aceito.
'''},
   {'n': 2, 'cab': 'EXT. JARDIM DA MANSÃO VALENTE — CONTÍNUO', 'tempo': '0:45–1:20', 'loc': 'jardim_mansao',
    'roteiro': '''
@Henrique ri pelo nariz, puxa uma nota de cem reais da carteira e a atira no peito de Téo.
HENRIQUE | | Toma. Pra comprar um terno.
@Téo pega a nota no ar, dobra em três movimentos rápidos e a transforma numa rosa. Entrega para Laura.
TÉO | | Pra noiva.
HENRIQUE | | Tudo tem preço, Laura.
TÉO | | Quase tudo.
AUGUSTO | | Seu juiz, isso não vale!
JUIZ DE PAZ | dando de ombros | Maiores de idade... documentos em ordem... Cadê a aliança?
@Téo tira uma latinha de refrigerante do bolso do casaco, arranca o lacre e o entorta até virar um anel. Laura puxa um fio de cetim da própria echarpe e amarra um lacinho nele. Téo coloca o anel no dedo dela.
'''},
   {'n': 3, 'cab': 'EXT. JARDIM DA MANSÃO VALENTE — CONTÍNUO', 'tempo': '1:20–1:40', 'loc': 'jardim_mansao',
    'roteiro': '''
@Téo assina o livro de registro com uma assinatura enorme, cheia de floreios. O juiz aproxima o livro do rosto.
JUIZ DE PAZ | | Teodoro... Albuquerque... Monteiro? Monteiro como o banco?
TÉO | | Coincidência.
@Henrique bufa. Augusto passa a mão no rosto.
JUIZ DE PAZ | | Eu os declaro marido e mulher.
TÉO | | Agora o bolo?
@Laura ri pela primeira vez no dia.
'''},
   {'n': 4, 'cab': 'EXT. PORTÃO DA MANSÃO / INT. SALA DA PRESIDÊNCIA DO BANCO — CONTÍNUO', 'tempo': '1:40–2:00', 'loc': 'sala_presidencia',
    'roteiro': '''
@Do lado de fora do portão, ao lado de um carro preto, OSVALDO (62), motorista de terno preto e quepe, observa Téo comer bolo com a mão. Os olhos dele param no relógio de ouro. Ele disca.
OSVALDO | ao telefone | Dona Celeste... encontrei o seu neto.
@No alto de uma torre de vidro, DONA CELESTE (74), chanel prateado e colar de pérolas, se vira da janela.
DONA CELESTE | | Onde?
OSVALDO | O.S. | Ele acabou de se casar.
DONA CELESTE | | Casar?! Com quem?
OSVALDO | O.S. | Com a filha do Valente.
@Celeste fica imóvel.
DONA CELESTE | | A filha do homem que nos deve trezentos milhões.
'''},
  ],
  'gancho': 'O mendigo é o herdeiro desaparecido, e a avó dele acaba de descobrir com quem ele casou.',
  'clipes': [
   (1, '0:00–0:15', 1, 'O casamento de revista; o juiz pergunta; o pai cochicha "trezentos milhões".'),
   (2, '0:15–0:30', 1, '"Não." "Eu caso. Mas não com ele." Laura vira para o portão: o homem de barba e o bolo.'),
   (3, '0:30–0:45', 1, 'Laura atravessa o corredor: "Você. Quer casar comigo?" "Tem bolo?" "Três andares." "Aceito."'),
   (4, '0:45–1:05', 2, 'A nota atirada; a rosa de origami; "Tudo tem preço." "Quase tudo."'),
   (5, '1:05–1:20', 2, 'O juiz cede; a aliança de latinha com o lacinho de cetim.'),
   (6, '1:20–1:40', 3, 'A assinatura; "Monteiro como o banco?" "Coincidência."; "Agora o bolo?"'),
   (7, '1:40–2:00', 4, 'Osvaldo vê o relógio e liga; Dona Celeste na torre: "...nos deve trezentos milhões."'),
  ]},
 {'n': 2, 'frase': ('Laura', 'Eu escolho.'), 'titulo': 'A noite na praça', 'duracao': '2:00',
  'logline': 'Expulsa de casa, Laura passa a noite de núpcias na praça e começa a desconfiar de quem é o marido.',
  'absurdo': 'O pai joga as malas da noiva por cima do portão, e a noite de núpcias é miojo num banco de praça.',
  'humilhacao': 'Expulsa de casa, Laura ouve Henrique zombar do "banco de praça" do marido.',
  'virada': 'Téo lê a dívida como um banqueiro e raspa a barba: é o rosto da capa da revista.',
  'elenco': ['laura', 'teo', 'augusto', 'henrique', 'barbeiro', 'celeste', 'osvaldo'],
  'locacoes': ['praca', 'barbearia'], 'objetos': ['relogio', 'notificacao_divida', 'anel_latinha', 'cartao_preto'],
  'looks': {'teo': 'base; o rosto barbeado do look O presidente aparece no fim da cena 4'},
  'batidas': ['As malas voam por cima do portão: "Um Valente não implora!"',
              'Miojo no banco da praça; Téo fala de juros e cita francês.',
              'O relógio cai virado: "T.M. 1952". "Tio Mário. Herança."',
              'A notificação de R$ 300 milhões: "Essa dívida foi vendida pra uma empresa de fachada."',
              'Henrique tenta comprá-la de volta: "Eu tenho um banco." "De praça!" "Eu escolho."',
              'Gancho: na barbearia, a barba cai, a avó entra e Laura não reconhece o marido.'],
  'cenas': [
   {'n': 1, 'cab': 'EXT. CALÇADA DA MANSÃO / PRAÇA DOS IPÊS — NOITE', 'tempo': '0:00–0:15', 'loc': 'praca',
    'roteiro': '''
@Duas malas voam por cima do portão da mansão e caem na calçada, aos pés de LAURA (27), ainda de vestido de noiva.
AUGUSTO | O.S., do outro lado do portão | Um Valente não implora! Quer viver de lixo? Vai morar no lixo!
@O portão bate. TÉO (31), barba enorme e sobretudo surrado, pega as malas, uma em cada mão, e aponta com o queixo para a praça.
TÉO | | Bem-vinda à minha casa. É ali. O banco verde.
'''},
   {'n': 2, 'cab': 'EXT. PRAÇA DOS IPÊS — NOITE', 'tempo': '0:15–1:05', 'loc': 'praca',
    'roteiro': '''
@No banco verde, sob o poste, Téo serve miojo num copo de plástico. Laura come com um garfinho, a cauda do vestido sobre as pedras portuguesas.
TÉO | | Os juros subiram meio ponto hoje. Péssimo pra quem deve. C'est la vie, madame.
LAURA | | Você fala francês. Entende de juros. Quem é você?
TÉO | | Um homem que lê o jornal que embrulha o pão.
@O relógio de ouro escorrega do pulso dele e cai no banco, virado. Laura o pega. Na tampa, gravado: T.M. 1952.
LAURA | | T.M.?
TÉO | pegando o relógio de volta | Tio Mário. Herança.
@Laura tira da bolsinha uma carta dobrada e a entrega a ele.
LAURA | | Meu pai deve trezentos milhões pro Banco Monteiro. Vence sexta. Por isso o casamento.
@Téo lê. O rosto dele muda.
TÉO | | Essa dívida foi vendida. Pra uma empresa de fachada.
LAURA | | Como você sabe disso?
TÉO | | Eu já fui... contador.
'''},
   {'n': 3, 'cab': 'EXT. PRAÇA DOS IPÊS — CONTÍNUO', 'tempo': '1:05–1:25', 'loc': 'praca',
    'roteiro': '''
@Faróis. HENRIQUE (35), ainda de smoking, desce de um carro esportivo.
HENRIQUE | | Laura. Última chance. Larga esse mendigo e amanhã eu pago a dívida do teu pai.
TÉO | | Ela não precisa. Eu tenho um banco.
HENRIQUE | gargalhando, apontando o banco da praça | De praça!
@Laura se levanta, passa o braço pelo de Téo e encara o ex-noivo.
LAURA | | Eu escolho.
HENRIQUE | voltando para o carro | Tudo tem preço, Laura. Até você.
'''},
   {'n': 4, 'cab': 'INT. BARBEARIA DO SEU NENÊ — DIA', 'tempo': '1:25–2:00', 'loc': 'barbearia',
    'roteiro': '''
@SEU NENÊ (70), barbeiro de jaleco branco, passa a navalha na barba de Téo, coberto por uma toalha quente. Laura espera no sofá de couro, folheando uma revista de negócios. Na capa: "ONDE ESTÁ O HERDEIRO DO BANCO MONTEIRO?"
@Téo estende um cartão preto de metal. Seu Nenê arregala os olhos.
SEU NENÊ | | Cartão preto?!
@Téo leva o dedo aos lábios. O sininho da porta toca. DONA CELESTE (74) entra, seguida de OSVALDO (62).
DONA CELESTE | | Teodoro Albuquerque Monteiro. Dois anos.
@A toalha sai. Um homem barbeado, de cabelo curto, se levanta da cadeira. Laura se levanta, educada, sem reconhecê-lo.
LAURA | | Desculpa, senhora, eu tô esperando o meu marido...
TÉO | | Laura. Sou eu.
@Laura olha para a capa da revista. Olha para ele. É o mesmo rosto. Congela.
'''},
  ],
  'gancho': 'O mendigo com quem ela casou é o rosto da capa: o herdeiro do banco que cobra a dívida do pai dela.',
  'clipes': [
   (1, '0:00–0:15', 1, 'As malas voam por cima do portão; "Um Valente não implora!"; "O banco verde."'),
   (2, '0:15–0:35', 2, 'Miojo no banco; juros; francês; "Quem é você?"'),
   (3, '0:35–0:50', 2, 'O relógio cai virado: "T.M.?" "Tio Mário. Herança."'),
   (4, '0:50–1:05', 2, 'A notificação; "empresa de fachada"; "Eu já fui... contador."'),
   (5, '1:05–1:25', 3, 'Henrique; "Eu tenho um banco." "De praça!" "Eu escolho."'),
   (6, '1:25–1:45', 4, 'Navalha, revista e cartão preto; "Cartão preto?!"'),
   (7, '1:45–2:00', 4, 'Dona Celeste entra; a toalha sai; "Laura. Sou eu."; congela.'),
  ]},
 {'n': 3, 'frase': ('Téo', 'Vó... então pode ficar com o banco.'), 'titulo': 'A reunião de cobrança', 'duracao': '2:00',
  'logline': 'Na reunião que ia executar a dívida, a cadeira da presidência gira, e o mendigo está nela.',
  'absurdo': 'A cadeira presidencial gira devagar e revela o "mendigo" de terno; o sogro derruba a xícara.',
  'humilhacao': 'Henrique e Augusto chegam para tomar a fábrica "por um real", certos de que venceram.',
  'virada': 'O mendigo é o presidente: Henrique é desmascarado e Augusto precisa agradecer ao genro.',
  'elenco': ['augusto', 'henrique', 'teo', 'celeste', 'osvaldo', 'laura'],
  'locacoes': ['sala_presidencia'], 'objetos': ['notificacao_divida', 'relogio', 'anel_latinha'],
  'looks': {'teo': 'O presidente (todas as cenas)'},
  'batidas': ['Henrique tranquiliza Augusto: vai comprar a empresa "por um real".',
              'A cadeira gira: Téo, barbeado, de terno. A xícara cai.',
              'Téo prova que a dívida é de Henrique; Dona Celeste manda tirá-lo da sala.',
              'A condição para Augusto: nunca mais escolher pela filha.',
              'Laura: "Você mentiu." "Eu só não contei."',
              'Gancho: o ultimato da avó, e a resposta: "Vó... então pode ficar com o banco."'],
  'cenas': [
   {'n': 1, 'cab': 'INT. SALA DA PRESIDÊNCIA DO BANCO — DIA', 'tempo': '0:00–0:30', 'loc': 'sala_presidencia',
    'roteiro': '''
@Sexta-feira. AUGUSTO (60), suando no terno preto, e HENRIQUE (35), impecável, sentados à mesa comprida. A cadeira da presidência está de costas, virada para a janela.
HENRIQUE | baixo, para Augusto | Relaxa, sogrão. O banco executa a dívida, eu compro a tua empresa por um real... digo, eu te salvo.
AUGUSTO | | Onde está o presidente?
@A cadeira gira devagar. TÉO (31): barbeado, cabelo curto penteado para trás, terno grafite de três peças, o mesmo relógio de ouro no pulso. Augusto deixa a xícara cair. Ela se espatifa no chão.
AUGUSTO | | O... o mendigo?
TÉO | | O genro.
'''},
   {'n': 2, 'cab': 'INT. SALA DA PRESIDÊNCIA DO BANCO — CONTÍNUO', 'tempo': '0:30–1:05', 'loc': 'sala_presidencia',
    'roteiro': '''
@Téo desliza uma pasta pela mesa até Henrique. Por cima, a notificação de trezentos milhões.
TÉO | | A dívida da Valente Têxtil foi comprada há seis meses por uma empresa de fachada. O dono: Henrique Lacerda.
HENRIQUE | | Isso é mentira!
TÉO | | Você comprou a dívida pra forçar o casamento e ficar com a fábrica.
@A porta dupla se abre. DONA CELESTE (74) entra, seguida de OSVALDO (62).
DONA CELESTE | | Osvaldo, acompanhe o senhor Lacerda até a rua.
HENRIQUE | sendo levado | Tudo tem preço!
TÉO | | E o seu acabou de vencer.
'''},
   {'n': 3, 'cab': 'INT. SALA DA PRESIDÊNCIA DO BANCO — CONTÍNUO', 'tempo': '1:05–1:40', 'loc': 'sala_presidencia',
    'roteiro': '''
@Téo se vira para Augusto.
TÉO | | A dívida está congelada. Com uma condição: o senhor nunca mais escolhe nada pela sua filha.
AUGUSTO | engolindo o orgulho | Um Valente... agradece.
@LAURA (27) aparece na porta. Na mão, ainda o anel de latinha.
LAURA | | Você mentiu pra mim.
TÉO | | Eu só não contei.
LAURA | | É a mesma coisa.
TÉO | | Você foi a única pessoa que me olhou nos olhos quando eu não tinha nada.
'''},
   {'n': 4, 'cab': 'INT. SALA DA PRESIDÊNCIA DO BANCO — CONTÍNUO', 'tempo': '1:40–2:00', 'loc': 'sala_presidencia',
    'roteiro': '''
@Dona Celeste apoia as duas mãos na mesa.
DONA CELESTE | | Teodoro. Monteiro não se esconde: nem do banco, nem da família. Ou você anula esse casamento até amanhã, ou perde a presidência.
@Laura olha para Téo. Téo olha para o anel de latinha no dedo dela. Depois, para a avó.
TÉO | | Vó... então pode ficar com o banco.
@Ele pega a mão de Laura. Dona Celeste, pela primeira vez, quase sorri. Congela.
'''},
  ],
  'gancho': 'Téo escolhe Laura no lugar do banco, e Dona Celeste ainda não disse a última palavra.',
  'clipes': [
   (1, '0:00–0:15', 1, 'Augusto e Henrique à mesa; "compro a tua empresa por um real... digo, eu te salvo."'),
   (2, '0:15–0:30', 1, 'A cadeira gira: Téo de terno; a xícara se espatifa; "O mendigo?" "O genro."'),
   (3, '0:30–0:50', 2, 'A pasta e a empresa de fachada; "Isso é mentira!"'),
   (4, '0:50–1:05', 2, 'Dona Celeste manda tirar Henrique; "E o seu acabou de vencer."'),
   (5, '1:05–1:20', 3, 'A condição para Augusto; "Um Valente... agradece."'),
   (6, '1:20–1:40', 3, 'Laura na porta: "Você mentiu pra mim." "Eu só não contei."'),
   (7, '1:40–2:00', 4, 'O ultimato; "Vó... então pode ficar com o banco."; congela no quase sorriso.'),
  ]},
]
