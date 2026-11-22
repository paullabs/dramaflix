"use client";

import Link from "next/link";
import { usePathname } from "next/navigation";
import { cx } from "@/lib/marca";
import { abasInferiores, estaAtivo } from "./navegacao";
import styles from "./BottomTabs.module.css";

/** Barra de abas inferior (<960px). A marquinha desliza até a aba aberta. */
export function BottomTabs() {
  const pathname = usePathname();
  const indice = abasInferiores.findIndex(({ href }) => estaAtivo(pathname, href));

  return (
    <nav className={styles.tabs} aria-label="Navegação principal">
      {indice >= 0 && <span className={styles.indicador} style={{ "--i": indice } as React.CSSProperties} aria-hidden="true" />}
      {abasInferiores.map(({ href, rotulo, Icone }) => {
        const ativo = estaAtivo(pathname, href);
        return (
          <Link key={href} href={href} className={cx(styles.tab, ativo && styles.ativo)} aria-current={ativo ? "page" : undefined}>
            <Icone size={26} className={styles.icone} />
            <span>{rotulo}</span>
          </Link>
        );
      })}
    </nav>
  );
}
