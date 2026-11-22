import type { Metadata } from "next";
import { MinhaLista } from "@/components/MinhaLista";
import { MARCA } from "@/lib/marca";

export const metadata: Metadata = { title: `Minha lista — ${MARCA.nome}` };

export default function MinhaListaPage() {
  return <MinhaLista />;
}
