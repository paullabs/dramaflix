import type { Metadata } from "next";
import { notFound } from "next/navigation";
import { Suspense } from "react";
import { Player } from "@/components/Player";
import { dramas, existeDrama, getDrama } from "@/data/catalogo";
import { MARCA } from "@/lib/marca";

export function generateStaticParams() {
  return dramas.map((d) => ({ id: d.id }));
}

export async function generateMetadata(props: PageProps<"/assistir/[id]">): Promise<Metadata> {
  const { id } = await props.params;
  return { title: existeDrama(id) ? `${getDrama(id).titulo} — ${MARCA.nome}` : MARCA.nome };
}

// Player vertical (fora do grupo (app): tela cheia, sem barras de navegação).
// Os parâmetros da URL são lidos dentro do <Suspense>, para a navegação abrir na hora.
export default function AssistirPage(props: PageProps<"/assistir/[id]">) {
  return (
    <Suspense fallback={<div style={{ position: "fixed", inset: 0, background: "#000" }} />}>
      <PlayerDaRota params={props.params} />
    </Suspense>
  );
}

async function PlayerDaRota({ params }: { params: Promise<{ id: string }> }) {
  const { id } = await params;
  if (!existeDrama(id)) notFound();
  return <Player id={id} />;
}
