import Link from "next/link";
import { cx } from "@/lib/marca";
import { iconeDe } from "./iconesCategoria";
import styles from "./Chips.module.css";

export interface Chip {
  id: string;
  rotulo: string;
  href: string;
}

/**
 * Fileira de atalhos com figura + uma palavra. Rola para o lado no celular.
 * `vidro`: por cima do destaque da home (transparente); `solido`: nas páginas.
 */
export function Chips({ itens, ativo, variante = "solido", rotulo = "Categorias", className }: { itens: Chip[]; ativo?: string; variante?: "vidro" | "solido"; rotulo?: string; className?: string }) {
  return (
    <nav className={cx(styles.chips, styles[variante], className)} aria-label={rotulo}>
      {itens.map((c) => {
        const Icone = iconeDe[c.id];
        const on = c.id === ativo;
        return (
          <Link key={c.id} href={c.href} className={cx(styles.chip, on && styles.on)} aria-current={on ? "page" : undefined}>
            {Icone && <Icone size={18} className={styles.icone} />}
            {c.rotulo}
          </Link>
        );
      })}
    </nav>
  );
}
