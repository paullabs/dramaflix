// Gera src/components/icones.gerado.ts com SÓ os ícones usados no site.
// Fontes (instaladas como devDependencies, nada vai para o navegador além do que está aqui):
//   - Solar Icons, estilo "Bold Duotone" (CC BY 4.0, 480 Design): lugares, categorias e estados.
//   - Phosphor Icons, estilos "Fill" e "Bold" (MIT): ações dentro de botões.
// Uso: node scripts/gerar_icones.mjs   (rodar dentro de web/)
import { writeFileSync } from "node:fs";
import { createRequire } from "node:module";

const require = createRequire(import.meta.url);
const conjuntos = {
  solar: require("@iconify-json/solar/icons.json"),
  ph: require("@iconify-json/ph/icons.json"),
};

// nome no código → ícone da biblioteca
const MAPA = {
  // lugares e coisas (Solar Bold Duotone)
  inicio: "solar:home-smile-bold-duotone",
  paraVoce: "solar:video-frame-play-vertical-bold-duotone",
  emAlta: "solar:fire-bold-duotone",
  lista: "solar:bookmark-bold-duotone",
  listaSalvo: "solar:bookmark-check-bold-duotone",
  buscar: "solar:magnifer-bold-duotone",
  perfil: "solar:user-circle-bold-duotone",
  ajuda: "solar:question-circle-bold-duotone",
  info: "solar:info-circle-bold-duotone",
  cadeado: "solar:lock-keyhole-bold-duotone",
  cadeadoAberto: "solar:lock-keyhole-unlocked-bold-duotone",
  presente: "solar:gift-bold-duotone",
  coroa: "solar:crown-star-bold-duotone",
  relogio: "solar:clock-circle-bold-duotone",
  microfone: "solar:microphone-3-bold-duotone",
  idioma: "solar:translation-2-bold-duotone",
  episodios: "solar:clapperboard-play-bold-duotone",
  historico: "solar:history-bold-duotone",
  estrelas: "solar:stars-bold-duotone",
  dinheiro: "solar:money-bag-bold-duotone",
  raio: "solar:bolt-bold-duotone",
  fantasma: "solar:ghost-bold-duotone",
  romance: "solar:heart-shine-bold-duotone",
  risada: "solar:emoji-funny-circle-bold-duotone",
  sol: "solar:sun-2-bold-duotone",
  lua: "solar:moon-stars-bold-duotone",
  tv: "solar:tv-bold-duotone",
  ranking: "solar:ranking-bold-duotone",
  carteira: "solar:wallet-money-bold-duotone",
  // ações (Phosphor Fill / Bold)
  play: "ph:play-fill",
  pausa: "ph:pause-fill",
  mais: "ph:plus-bold",
  check: "ph:check-bold",
  fechar: "ph:x-bold",
  esquerda: "ph:caret-left-bold",
  direita: "ph:caret-right-bold",
  cima: "ph:caret-up-bold",
  baixo: "ph:caret-down-bold",
  voltar: "ph:arrow-left-bold",
  enviar: "ph:share-fat-fill",
  coracao: "ph:heart-bold",
  coracaoCheio: "ph:heart-fill",
  gostei: "ph:thumbs-up-fill",
  grade: "ph:squares-four-fill",
  // player
  somLigado: "ph:speaker-high-fill",
  somDesligado: "ph:speaker-slash-fill",
  telaCheia: "ph:corners-out-bold",
  sairTelaCheia: "ph:corners-in-bold",
  velocidade: "ph:gauge-fill",
  acelerar: "ph:fast-forward-fill",
  repetir: "ph:arrow-counter-clockwise-bold",
  proximo: "ph:skip-forward-fill",
};

function pegar(id) {
  const [prefixo, chave] = id.split(":");
  const conjunto = conjuntos[prefixo];
  let nome = chave;
  // alguns nomes são apelidos de outro ícone
  for (let i = 0; i < 4 && !conjunto.icons[nome] && conjunto.aliases?.[nome]; i++) nome = conjunto.aliases[nome].parent;
  const icone = conjunto.icons[nome];
  if (!icone) throw new Error(`Ícone não encontrado: ${id}`);
  return { body: icone.body, v: icone.width ?? conjunto.width ?? 24 };
}

const saida = Object.fromEntries(Object.entries(MAPA).map(([nome, id]) => [nome, pegar(id)]));

const arquivo = `// GERADO por scripts/gerar_icones.mjs — não editar à mão.
// Solar Icons (CC BY 4.0, 480 Design) e Phosphor Icons (MIT).
export const ICONES = ${JSON.stringify(saida, null, 2)} as const;

export type NomeIcone = keyof typeof ICONES;
`;
writeFileSync(new URL("../src/components/icones.gerado.ts", import.meta.url), arquivo);
console.log(`${Object.keys(saida).length} ícones gerados em src/components/icones.gerado.ts`);
