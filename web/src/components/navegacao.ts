import { IconBookmark, IconCoin, IconFeed, IconFlame, IconHome, IconSearch, IconUser } from "./icons";

export const itensLaterais = [
  { href: "/buscar", rotulo: "Buscar", Icone: IconSearch },
  { href: "/", rotulo: "Início", Icone: IconHome },
  { href: "/para-voce", rotulo: "Para você", Icone: IconFeed },
  { href: "/em-alta", rotulo: "Em alta", Icone: IconFlame },
  { href: "/minha-lista", rotulo: "Minha lista", Icone: IconBookmark },
  { href: "/moedas", rotulo: "Moedas", Icone: IconCoin },
];

export const abasInferiores = [
  { href: "/", rotulo: "Início", Icone: IconHome },
  { href: "/para-voce", rotulo: "Para você", Icone: IconFeed },
  { href: "/em-alta", rotulo: "Em alta", Icone: IconFlame },
  { href: "/minha-lista", rotulo: "Minha lista", Icone: IconBookmark },
  { href: "/perfil", rotulo: "Perfil", Icone: IconUser },
];

/** Item ativo: "/" só na home; os demais também valem para subpáginas. */
export function estaAtivo(pathname: string, href: string) {
  return href === "/" ? pathname === "/" : pathname === href || pathname.startsWith(`${href}/`);
}
