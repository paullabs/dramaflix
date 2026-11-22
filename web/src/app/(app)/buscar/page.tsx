import type { Metadata } from "next";
import { Busca } from "@/components/Busca";
import { MARCA } from "@/lib/marca";

export const metadata: Metadata = { title: `Buscar — ${MARCA.nome}` };

export default function BuscarPage() {
  return <Busca />;
}
