import type { Metadata } from "next";
import { Moedas } from "@/components/Moedas";
import { MARCA } from "@/lib/marca";

export const metadata: Metadata = { title: `Moedas e VIP — ${MARCA.nome}` };

export default function MoedasPage() {
  return <Moedas />;
}
