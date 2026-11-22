// Catálogo da plataforma.
// A fonte é ../../../capas/catalogo.json (sessão de capas). O script scripts/importar_catalogo.py
// otimiza as imagens em /public e gera ./titulos.gerado.json — este arquivo só aplica as regras de UI
// (classificação, selos, ranking, categorias). Novos lotes entram sozinhos: rode o script de novo.
import gerados from "./titulos.gerado.json";
import videosGerados from "./videos.gerado.json";

export type Classificacao = "L" | "A10" | "A12" | "A14" | "A16" | "A18";
export type Selo = "novo" | "exclusivo" | "dublado" | "completo";

export interface Logo {
  src: string;
  w: number;
  h: number;
}

export interface Drama {
  id: string;
  numero: number;
  lote: string;
  titulo: string;
  genero: string;
  tropos: string[];
  sinopse: string;
  /** uma frase curta para o destaque e o feed */
  gancho: string;
  episodios: number;
  gratisAte: number;
  moedasPorEpisodio: number;
  classificacao: Classificacao;
  selo?: Selo;
  dublado: boolean;
  /** posição no ranking "Em alta hoje" */
  emAlta: number;
  /** capa 3:4 com título (fileiras, cards) */
  capa: string;
  /** foto 3:4 sem texto (destaque no celular, player) */
  foto: string;
  /** banner 16:9 sem texto (destaque no desktop/tablet, modal) */
  banner: string;
  logo: Logo;
  cor: string;
}

interface TituloGerado {
  numero: number;
  id: string;
  arquivo: string;
  titulo: string;
  genero: string;
  tags: string[];
  sinopse: string;
  gancho: string;
  episodios: number;
  dublado: boolean;
  lote: string;
  logo: { w: number; h: number };
  cor: string;
}

const titulos = gerados as TituloGerado[];

// ---------- regras ----------
const normalizar = (s: string) =>
  s
    .normalize("NFD")
    .replace(/[̀-ͯ]/g, "")
    .toLowerCase();

const capitalizar = (s: string) => (s === s.toUpperCase() ? s : s.charAt(0).toUpperCase() + s.slice(1));

function temAlgum(t: { genero: string; tags?: string[]; tropos?: string[] }, termos: string[]) {
  const texto = normalizar([t.genero, ...(t.tags ?? t.tropos ?? [])].join(" "));
  return termos.some((termo) => texto.includes(normalizar(termo)));
}

function classificar(t: TituloGerado): Classificacao {
  if (temAlgum(t, ["terror"])) return "A16";
  if (temAlgum(t, ["policial", "crime", "suspense"])) return "A14";
  if (temAlgum(t, ["comédia", "sorte", "pet"])) return "A10";
  if (temAlgum(t, ["jovem", "universit", "faculdade"])) return "A12";
  return "A14";
}

/** Decisões editoriais que não estão no catálogo de capas. */
const ajustes: Record<string, { selo?: Selo; classificacao?: Classificacao }> = {
  "ele-me-trocou": { selo: "exclusivo" },
  "o-genro-humilhado": { selo: "exclusivo" },
  "a-delegada-que-prendeu-o-proprio-pai": { selo: "exclusivo" },
  "rejeitada-pelo-alfa": { selo: "completo" },
};

const loteMaisNovo = titulos.map((t) => t.lote).sort().at(-1) ?? "";

/** Ordem "Em alta hoje": a lista manda; quem não está nela vem depois, por número. */
const rankingHoje = [
  "ganhei-na-mega-sena",
  "o-motoboy-que-eu-humilhei",
  "ele-me-trocou",
  "a-faxineira-herdou-80-bilhoes",
  "nao-atenda-depois-da-meia-noite",
  "casei-com-o-mendigo",
  "o-genro-humilhado",
  "minha-sogra-me-expulsou",
  "gravida-de-trigemeos",
  "largada-no-altar",
];

function ordenar(preferidos: string[]): string[] {
  const existentes = new Set(titulos.map((t) => t.id));
  const primeiro = preferidos.filter((id) => existentes.has(id));
  const resto = titulos
    .filter((t) => !primeiro.includes(t.id))
    .sort((a, b) => a.numero - b.numero)
    .map((t) => t.id);
  return [...primeiro, ...resto];
}

const ordemHoje = ordenar(rankingHoje);

export const dramas: Drama[] = titulos.map((t) => {
  const ajuste = ajustes[t.id] ?? {};
  const selo: Selo | undefined = ajuste.selo ?? (t.dublado ? "dublado" : t.lote === loteMaisNovo ? "novo" : undefined);
  return {
    id: t.id,
    numero: t.numero,
    lote: t.lote,
    titulo: t.titulo,
    genero: t.genero,
    tropos: t.tags.map(capitalizar),
    sinopse: t.sinopse,
    gancho: t.gancho,
    episodios: t.episodios,
    gratisAte: 10,
    moedasPorEpisodio: 40,
    classificacao: ajuste.classificacao ?? classificar(t),
    selo,
    dublado: t.dublado,
    emAlta: ordemHoje.indexOf(t.id) + 1,
    capa: `/capas/${t.arquivo}.jpg`,
    foto: `/fotos/${t.arquivo}.jpg`,
    banner: `/banners/${t.arquivo}.jpg`,
    logo: { src: `/logos/${t.arquivo}.webp`, w: t.logo.w, h: t.logo.h },
    cor: t.cor,
  };
});

const porId = new Map(dramas.map((d) => [d.id, d]));

export function getDrama(id: string): Drama {
  const d = porId.get(id);
  if (!d) throw new Error(`Drama não encontrado: ${id}`);
  return d;
}

export function existeDrama(id: string) {
  return porId.has(id);
}

/** Destaques do billboard (giram a cada ~9 s). */
export const destaques = [
  "ganhei-na-mega-sena",
  "ele-me-trocou",
  "o-motoboy-que-eu-humilhei",
  "nao-atenda-depois-da-meia-noite",
  "rejeitada-pelo-alfa",
].filter(existeDrama);

// ---------- onde a pessoa parou (vem do histórico deste navegador) ----------
export interface Progresso {
  id: string;
  episodio: number;
  /** quanto já assistiu desse episódio (0–1) */
  andamento: number;
}

// ---------- categorias ----------
export interface Categoria {
  slug: string;
  /** nome curto: aparece em chips, fileiras e no título da página */
  titulo: string;
  itens: string[];
}

const idsOrdenados = ordemHoje;
const filtrar = (teste: (d: Drama) => boolean) => idsOrdenados.filter((id) => teste(getDrama(id)));
const porTermos = (termos: string[]) => filtrar((d) => temAlgum(d, termos));

const novos = [...dramas].sort((a, b) => (a.lote === b.lote ? b.numero - a.numero : b.lote.localeCompare(a.lote))).map((d) => d.id);
const maisLongos = [...dramas].sort((a, b) => b.episodios - a.episodios).map((d) => d.id);
const termosRomance = ["romance", "namoro", "casamento", "noiva", "companheira", "ódio ao amor"];
const termosComedia = ["comédia"];

export const categorias: Categoria[] = [
  { slug: "novos", titulo: "Novos", itens: novos },
  { slug: "dinheiro", titulo: "Bilionários", itens: porTermos(["bilionário", "herança", "sorte", "dinheiro", "ceo"]) },
  { slug: "vinganca", titulo: "Vingança", itens: porTermos(["vingança", "virada", "humilha"]) },
  { slug: "suspense", titulo: "Suspense e terror", itens: porTermos(["suspense", "terror", "policial", "crime", "mistério"]) },
  { slug: "romance", titulo: "Romance", itens: porTermos(termosRomance) },
  { slug: "comedia", titulo: "Comédia", itens: porTermos(termosComedia) },
  { slug: "leve", titulo: "Rir e se apaixonar", itens: porTermos([...termosComedia, ...termosRomance]) },
  { slug: "fantasia", titulo: "Fantasia", itens: porTermos(["fantasia", "lobisomem", "época", "sobrenatural", "renascimento"]) },
  { slug: "dublados", titulo: "Dublados", itens: filtrar((d) => d.dublado) },
  { slug: "maratonar", titulo: "Para maratonar", itens: maisLongos },
].filter((c) => c.itens.length > 0);

export function getCategoria(slug: string): Categoria | undefined {
  return categorias.find((c) => c.slug === slug);
}

/** Chips de navegação (barra do celular e busca). `id` escolhe o ícone. */
export const atalhos = [
  { id: "para-voce", rotulo: "Para você", href: "/para-voce" },
  { id: "em-alta", rotulo: "Em alta", href: "/em-alta" },
  ...categorias
    .filter((c) => ["novos", "dinheiro", "romance", "vinganca", "suspense", "comedia", "fantasia", "dublados"].includes(c.slug))
    .map((c) => ({ id: c.slug, rotulo: c.slug === "suspense" ? "Suspense" : c.titulo, href: `/categoria/${c.slug}` })),
];

// ---------- ranking (/em-alta) ----------
export type Periodo = "hoje" | "semana" | "mes";

export const rankings: Record<Periodo, string[]> = {
  hoje: ordemHoje,
  semana: ordenar([
    "o-motoboy-que-eu-humilhei",
    "a-faxineira-herdou-80-bilhoes",
    "ele-me-trocou",
    "ganhei-na-mega-sena",
    "o-genro-humilhado",
    "rejeitada-pelo-alfa",
    "casei-com-o-mendigo",
    "nao-atenda-depois-da-meia-noite",
    "largada-no-altar",
    "a-concubina-que-renasceu",
  ]),
  mes: ordenar([
    "rejeitada-pelo-alfa",
    "a-concubina-que-renasceu",
    "o-genro-humilhado",
    "ele-me-trocou",
    "o-motoboy-que-eu-humilhei",
    "a-segunda-familia-do-meu-marido",
    "nao-atenda-depois-da-meia-noite",
    "a-faxineira-herdou-80-bilhoes",
    "troquei-de-corpo-com-a-minha-sogra",
    "fingi-namorar-meu-pior-inimigo",
  ]),
};

/** Ordem do feed "Para você" (variando os gêneros). */
export const paraVoce = ordenar([
  "o-motoboy-que-eu-humilhei",
  "nao-atenda-depois-da-meia-noite",
  "ganhei-na-mega-sena",
  "a-delegada-que-prendeu-o-proprio-pai",
  "o-cachorro-herdou-tudo",
  "a-segunda-familia-do-meu-marido",
  "casei-com-o-mendigo",
  "rejeitada-pelo-alfa",
  "troquei-de-corpo-com-a-minha-sogra",
  "a-faxineira-herdou-80-bilhoes",
  "fingi-namorar-meu-pior-inimigo",
  "a-concubina-que-renasceu",
]);

// ---------- fileiras da home ----------
export type TipoFileira = "padrao" | "top" | "continuar";

export interface Fileira {
  id: string;
  titulo: string;
  tipo: TipoFileira;
  itens: string[];
  verTudo?: string;
}

const daCategoria = (slug: string, titulo?: string): Fileira | null => {
  const c = getCategoria(slug);
  return c ? { id: slug, titulo: titulo ?? c.titulo, tipo: "padrao", itens: c.itens, verTudo: `/categoria/${slug}` } : null;
};

export const fileiras: Fileira[] = [
  // preenchida pelo histórico real; some quando a pessoa ainda não assistiu nada
  { id: "continuar", titulo: "Continuar", tipo: "continuar" as const, itens: [] },
  { id: "em-alta", titulo: "Top 10 hoje", tipo: "top" as const, itens: ordemHoje.slice(0, 10), verTudo: "/em-alta" },
  daCategoria("novos"),
  daCategoria("dinheiro"),
  daCategoria("vinganca"),
  daCategoria("suspense"),
  daCategoria("leve"),
  daCategoria("maratonar"),
].filter((f): f is Fileira => f !== null && (f.tipo === "continuar" || f.itens.length > 0));

/** Semelhantes: mais tropos em comum primeiro. */
export function semelhantes(id: string, quantos = 6): Drama[] {
  const base = getDrama(id);
  const chave = (s: string) => normalizar(s);
  const meus = new Set(base.tropos.map(chave));
  return dramas
    .filter((d) => d.id !== id)
    .map((d) => ({ d, n: d.tropos.filter((t) => meus.has(chave(t))).length + (d.genero === base.genero ? 1 : 0) }))
    .sort((a, b) => b.n - a.n || a.d.emAlta - b.d.emAlta)
    .slice(0, quantos)
    .map((x) => x.d);
}

export const rotuloSelo: Record<Selo, string> = {
  novo: "Novo",
  exclusivo: "Exclusivo",
  dublado: "Dublado",
  completo: "Completo",
};

/** Busca simples (sem acento, sem maiúscula) por título, gênero, tropos e sinopse. */
export function buscar(termo: string): Drama[] {
  const q = normalizar(termo.trim());
  if (!q) return [];
  return ordemHoje
    .map(getDrama)
    .filter((d) => normalizar([d.titulo, d.genero, ...d.tropos, d.gancho, d.sinopse].join(" ")).includes(q));
}

// ---------- vídeos dos players ----------
type MapaVideos = Record<string, { amostra: string | null; previa?: string | null; episodios: Record<string, string> }>;
const videos = videosGerados as MapaVideos;

/** O drama já tem episódio de verdade (então os que faltam são "em breve", não amostra). */
function temEpisodioReal(id: string): boolean {
  return Object.keys(videos[id]?.episodios ?? {}).length > 0;
}

/**
 * O episódio já saiu? Num drama com episódios de verdade, só os que têm arquivo.
 * Num drama só com amostra (protótipo), todos contam como lançados.
 */
export function episodioSaiu(id: string, ep: number): boolean {
  return !temEpisodioReal(id) || Boolean(videos[id]?.episodios[String(ep)]);
}

/** Último episódio antes de `ep` que já saiu e que a pessoa pode ver (botão "Voltar ao ep. N"). */
export function lancadoAntes(id: string, ep: number, liberado: (n: number) => boolean = () => true): number {
  for (let n = ep - 1; n > 1; n--) if (episodioSaiu(id, n) && liberado(n)) return n;
  return 1;
}

/**
 * Vídeo de um episódio: o arquivo real (public/videos/<id>/ep-001.mp4…) quando existe.
 * Senão: num drama com episódios de verdade, `emBreve` (o player mostra o aviso);
 * num drama só de protótipo, a amostra (`amostra: true` = "vídeo de exemplo").
 */
export function videoDoEpisodio(id: string, ep: number): { src: string | null; amostra: boolean; emBreve: boolean } {
  const v = videos[id];
  const real = v?.episodios[String(ep)];
  if (real) return { src: real, amostra: false, emBreve: false };
  if (temEpisodioReal(id)) return { src: null, amostra: false, emBreve: true };
  return { src: v?.amostra ?? null, amostra: true, emBreve: false };
}

/** Prévia para o feed: um trecho curto do episódio 1 (leve), ou a amostra. Nunca o episódio inteiro. */
export function previaDe(id: string): string | null {
  const v = videos[id];
  return v?.previa ?? v?.amostra ?? null;
}
