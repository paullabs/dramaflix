import Link from "next/link";
import type { ComponentProps, ReactNode } from "react";
import { cx } from "@/lib/marca";
import styles from "./Botao.module.css";

type Variante = "claro" | "neutro" | "destaque" | "ouro" | "contorno";
type Tamanho = "p" | "m" | "g";

interface Base {
  variante?: Variante;
  tamanho?: Tamanho;
  icone?: ReactNode;
  bloco?: boolean;
  className?: string;
  children: ReactNode;
}

/**
 * Botão único da plataforma: mesmas alturas e espaçamentos em toda parte.
 * p = 36px · m = 44px · g = 52px (no billboard). Vira link quando recebe `href`.
 */
export function Botao({
  variante = "claro",
  tamanho = "m",
  icone,
  bloco,
  className,
  children,
  ...rest
}: Base & (({ href: string } & Omit<ComponentProps<typeof Link>, "href" | "className" | "children">) | ({ href?: undefined } & Omit<ComponentProps<"button">, "className" | "children">))) {
  const classe = cx(styles.botao, styles[variante], styles[tamanho], bloco && styles.bloco, className);
  const conteudo = (
    <>
      {icone && <span className={styles.icone}>{icone}</span>}
      <span className={styles.rotulo}>{children}</span>
    </>
  );

  if ("href" in rest && rest.href) {
    const { href, ...link } = rest as { href: string } & Omit<ComponentProps<typeof Link>, "href">;
    return (
      <Link href={href} className={classe} {...link}>
        {conteudo}
      </Link>
    );
  }

  const botao = rest as Omit<ComponentProps<"button">, "className" | "children">;
  return (
    <button type="button" className={classe} {...botao}>
      {conteudo}
    </button>
  );
}

/** Botão redondo só com ícone (Minha lista, curtir, compartilhar…). */
export function BotaoIcone({
  rotulo,
  ativo,
  tamanho = "m",
  className,
  children,
  ...rest
}: { rotulo: string; ativo?: boolean; tamanho?: "p" | "m" | "g"; className?: string; children: ReactNode } & Omit<
  ComponentProps<"button">,
  "className" | "children" | "aria-label"
>) {
  return (
    <button
      type="button"
      aria-label={rotulo}
      title={rotulo}
      aria-pressed={ativo}
      className={cx(styles.redondo, styles[`r${tamanho}`], ativo && styles.ativo, className)}
      {...rest}
    >
      {children}
    </button>
  );
}
