import type { Metadata } from "next";
import { notFound } from "next/navigation";
import { Suspense } from "react";
import { Chips } from "@/components/Chips";
import { iconeDe } from "@/components/iconesCategoria";
import { PosterGrid } from "@/components/PosterGrid";
import { categorias, getCategoria } from "@/data/catalogo";
import { MARCA } from "@/lib/marca";
import styles from "./categoria.module.css";

export function generateStaticParams() {
  return categorias.map((c) => ({ slug: c.slug }));
}

export async function generateMetadata(props: PageProps<"/categoria/[slug]">): Promise<Metadata> {
  const { slug } = await props.params;
  const c = getCategoria(slug);
  return { title: c ? `${c.titulo} — ${MARCA.nome}` : MARCA.nome };
}

// Os parâmetros da URL são lidos dentro do <Suspense>, para a navegação abrir na hora.
export default function CategoriaPage(props: PageProps<"/categoria/[slug]">) {
  return (
    <>
      <Suspense fallback={<div className="page" style={{ minHeight: "60vh" }} />}>
        <Conteudo params={props.params} />
      </Suspense>
    </>
  );
}

async function Conteudo({ params }: { params: Promise<{ slug: string }> }) {
  const { slug } = await params;
  const categoria = getCategoria(slug);
  if (!categoria) notFound();

  const Icone = iconeDe[categoria.slug];
  const chips = categorias.map((c) => ({ id: c.slug, rotulo: c.titulo, href: `/categoria/${c.slug}` }));

  return (
    <div className="page">
      <div className="page-head">
        <h1 className="page-title">
          {Icone && <Icone />}
          {categoria.titulo}
          <span className={styles.contagem} aria-label={`${categoria.itens.length} dramas`}>
            {categoria.itens.length}
          </span>
        </h1>
      </div>

      <Chips itens={chips} ativo={slug} rotulo="Outros temas" className={styles.chips} />

      <PosterGrid ids={categoria.itens} />
    </div>
  );
}
