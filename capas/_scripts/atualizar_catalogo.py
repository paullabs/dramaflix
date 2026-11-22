"""Acrescenta o lote v3 e os banners ao capas/catalogo.json (idempotente)."""
import json, os
from pathlib import Path

RAIZ = str(Path(__file__).resolve().parents[2])  # raiz do projeto (antes: /Users/paul/Downloads/drama)
CAT = f"{RAIZ}/capas/catalogo.json"
cat = json.load(open(CAT, encoding="utf-8"))

v3 = [
 (10, "ganhei-na-mega-sena", "Ganhei na Mega-Sena e Fingi Que Era Pobre", "Comédia · Mega-Sena", ["sorte grande", "família interesseira", "comédia", "segredo"], 70, "10a",
  "Dani acerta as seis dezenas sozinha e decide não contar para ninguém: quer descobrir quem a ama de verdade — o marido folgado, a sogra que a chama de \"encosto\" ou o vizinho tímido. O prêmio vence em 90 dias, e a família começa a desconfiar."),
 (11, "o-motoboy-que-eu-humilhei", "O Motoboy Que Eu Humilhei Era Bilionário", "Bilionário disfarçado", ["bilionário", "identidade secreta", "humilhação e virada", "romance"], 72, "11a",
  "Na porta do prédio mais caro da Faria Lima, a influenciadora Bárbara humilha o motoboy na frente de todo mundo. No dia seguinte, a empresa dela é comprada — e o novo dono chega à reunião de capacete na mão."),
 (12, "casei-com-o-mendigo", "Casei com o Mendigo e Ele Era Dono do Banco", "Casamento por impulso", ["casamento por impulso", "bilionário", "identidade secreta", "romance"], 68, "12a",
  "Para fugir do casamento arranjado pelo pai, Laura pede em casamento o primeiro homem que vê na praça: um morador de rua de barba enorme. Ele é o herdeiro do maior banco do país — e o pai dela deve uma fortuna a esse banco."),
 (13, "a-faxineira-herdou-80-bilhoes", "A Faxineira Herdou 80 Bilhões do Patrão", "Herança", ["herança", "família rica", "humilhação e virada", "dinheiro"], 75, "13a",
  "Durante 15 anos, Rose cuidou do velho Augusto sem pedir nada. No testamento, ele deixa a fortuna inteira para ela — e os filhos dele juram tirar até o último centavo."),
 (14, "gravida-de-trigemeos", "Grávida de Trigêmeos do Bilionário Que Me Demitiu", "Bebê do CEO", ["bebê secreto", "CEO", "segunda chance", "romance"], 66, "14a",
  "Dias depois de ser demitida por mensagem, Bruna descobre que está grávida — de trigêmeos — do chefe com quem passou uma única noite. Quando volta para contar, ele está noivo da filha do sócio."),
 (15, "ajudei-um-velhinho-e-ganhei-uma-ilha", "Ajudei um Velhinho na Rua e Ganhei uma Ilha", "Comédia de sorte", ["sorte", "herança", "comédia", "romance"], 55, "15a",
  "Mel ajuda um senhor perdido na Paulista a voltar para casa. Uma semana depois, um advogado aparece com a escritura de uma ilha em Angra — e com o neto mal-humorado que jura que é golpe."),
 (16, "largada-no-altar", "Largada no Altar, Casei com o Garçom Bilionário", "Noiva abandonada", ["noiva abandonada", "casamento por impulso", "bilionário", "romance"], 64, "16a",
  "O noivo foge com a madrinha no meio da cerimônia. Com a igreja cheia, Carol puxa o garçom pela gravata e casa com ele ali mesmo. Na manhã seguinte, o \"garçom\" vem buscá-la de helicóptero."),
 (17, "minha-sogra-me-expulsou", "Minha Sogra Me Expulsou. Eu Sou a Dona do Condomínio.", "Vingança familiar", ["sogra", "vingança", "virada de poder", "família"], 60, "17a",
  "Dona Neide põe as malas da nora na calçada na frente de todos os vizinhos. Só não sabe que o condomínio de luxo onde ela mora inteiro pertence à empresa que a nora fundou em segredo."),
 (18, "o-cachorro-herdou-tudo", "O Cachorro Herdou Tudo e Eu Virei Secretária Dele", "Comédia absurda", ["herança", "comédia", "família rica", "pet"], 50, "18b",
  "O magnata excêntrico deixa 3 bilhões para Duque, seu samoieda — e só a passeadora, Ana, pode administrar a fortuna em nome dele. Agora a família inteira tem que pedir dinheiro para ela."),
]

ids = {t["id"] for t in cat["titulos"]}
for n, slug, tit, gen, tags, eps, foto, sin in v3:
    if slug in ids:
        continue
    cat["titulos"].append({
        "id": slug, "numero": n, "titulo": tit, "genero": gen, "tags": tags, "sinopse": sin,
        "episodios": eps, "dublado": False, "lote": "v3",
        "arquivos": {
            "capa": f"capas/v3/{n:02d}-{slug}.png",
            "capa_web": f"capas/v3/web/{n:02d}-{slug}.jpg",
            "fundo": f"capas/v3/fotos/{foto}.png",
            "logo_titulo": f"capas/v3/titulos/{n:02d}.png",
        },
    })

for t in cat["titulos"]:
    n, slug = t["numero"], t["id"]
    t["arquivos"]["banner"] = f"capas/banners/web/{n:02d}-{slug}.jpg"
    t["arquivos"]["banner_original"] = f"capas/banners/{n:02d}-{slug}.png"
    t["arquivos"]["banner_com_logo"] = f"capas/banners/com-logo/{n:02d}-{slug}.jpg"

cat["titulos"].sort(key=lambda t: t["numero"])
cat["como_usar"]["banner"] = ("Banner 16:9 SEM texto (web: 1920x1084 JPG; original: 2720x1536 PNG) com os mesmos atores da capa: "
    "protagonista no terço direito, lado esquerdo livre para logo, sinopse e botões. Use no billboard/hero da home e no topo da página do título. "
    "Aplique por CSS o degradê da esquerda e o fade inferior para a cor da página e sobreponha o logo_titulo.")
cat["como_usar"]["banner_com_logo"] = "Prévia do billboard já com degradês e logo — referência visual ou peça para redes/anúncios."
cat["como_usar"]["mobile"] = "No celular, o hero usa o 'fundo' (3:4) com o logo_titulo por cima, ou a própria 'capa'."
cat["atualizado_em"] = "2026-11-19"
json.dump(cat, open(CAT, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
faltando = [p for t in cat["titulos"] for p in t["arquivos"].values() if not os.path.exists(f"{RAIZ}/{p}")]
print("titulos:", len(cat["titulos"]), "| arquivos faltando:", len(faltando))
for p in faltando:
    print("  ", p)
