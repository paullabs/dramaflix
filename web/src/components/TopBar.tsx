"use client";

import Link from "next/link";
import { usePathname } from "next/navigation";
import { atalhos } from "@/data/catalogo";
import { useCarteira } from "@/lib/estado";
import { Chips } from "./Chips";
import { IconCoin, IconSearch } from "./icons";
import { Wordmark } from "./Marca";
import { useRolou } from "./useReducedMotion";
import styles from "./TopBar.module.css";

/** Barra superior do celular/tablet (<960px). Na home ela fica transparente sobre o destaque. */
export function TopBar() {
  const pathname = usePathname();
  const home = pathname === "/";
  const rolou = useRolou(24);
  const { saldo } = useCarteira();
  const solida = !home || rolou;

  return (
    <header className={styles.top} data-solida={solida || undefined}>
      <div className={styles.linha}>
        <Link href="/" aria-label="Início">
          <Wordmark />
        </Link>
        <div className={styles.acoes}>
          <Link href="/buscar" className={styles.icone} aria-label="Buscar">
            <IconSearch size={24} />
          </Link>
          <Link href="/moedas" className={styles.moedas} aria-label={`Saldo: ${saldo} moedas`}>
            <IconCoin size={20} />
            {/* a chave faz o número "pular" quando o saldo muda */}
            <span key={saldo} className={styles.saldo}>
              {saldo}
            </span>
          </Link>
        </div>
      </div>

      {home && <Chips itens={atalhos} variante={solida ? "solido" : "vidro"} className={styles.chips} />}
    </header>
  );
}
