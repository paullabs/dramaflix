import type { ComponentType } from "react";
import { IconBolt, IconFeed, IconFlame, IconGhost, IconHistory, IconLaugh, IconMic, IconMoneyBag, IconMoon, IconRomance, IconStars, IconSun, IconTv } from "./icons";

type Icone = ComponentType<{ size?: number; className?: string }>;

/** Um desenho para cada tema: quem lê pouco reconhece a categoria pela figura. */
export const iconeDe: Record<string, Icone> = {
  "para-voce": IconFeed,
  "em-alta": IconFlame,
  continuar: IconHistory,
  novos: IconStars,
  dinheiro: IconMoneyBag,
  vinganca: IconBolt,
  suspense: IconGhost,
  romance: IconRomance,
  comedia: IconLaugh,
  leve: IconSun,
  fantasia: IconMoon,
  dublados: IconMic,
  maratonar: IconTv,
};
