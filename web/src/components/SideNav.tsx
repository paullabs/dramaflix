"use client";

import Link from "next/link";
import { usePathname } from "next/navigation";
import { cx } from "@/lib/marca";
import { Simbolo } from "./Marca";
import { estaAtivo, itensLaterais } from "./navegacao";
import styles from "./SideNav.module.css";

/**
 * Barra lateral (desktop/TV, ≥960px), inspirada na referência de TV.
 * É uma coluna própria: o conteúdo começa depois dela, então nada fica por baixo.
 */
export function SideNav() {
  const pathname = usePathname();

  return (
    <nav className={styles.rail} aria-label="Principal">
      <Link href="/" className={styles.marca} aria-label="Início">
        <Simbolo size={40} />
      </Link>

      <ul className={styles.lista}>
        {itensLaterais.map(({ href, rotulo, Icone }) => {
          const ativo = estaAtivo(pathname, href);
          return (
            <li key={href}>
              <Link href={href} className={cx(styles.item, ativo && styles.ativo)} aria-current={ativo ? "page" : undefined}>
                <Icone size={26} />
                <span>{rotulo}</span>
              </Link>
            </li>
          );
        })}
      </ul>

      <Link href="/perfil" className={cx(styles.item, styles.perfil, estaAtivo(pathname, "/perfil") && styles.ativo)}>
        <span className={styles.avatar} aria-hidden="true" />
        <span>Perfil</span>
      </Link>
    </nav>
  );
}
