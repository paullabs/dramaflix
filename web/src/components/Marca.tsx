import { MARCA } from "@/lib/marca";
import styles from "./Marca.module.css";

/** Wordmark provisório. */
export function Wordmark({ className }: { className?: string }) {
  return (
    <span className={`${styles.wordmark} ${className ?? ""}`} aria-label={MARCA.nome}>
      {MARCA.nome}
    </span>
  );
}

/** Símbolo provisório (quadrado com "play"), usado na barra lateral. */
export function Simbolo({ size = 36 }: { size?: number }) {
  return (
    <span className={styles.simbolo} style={{ width: size, height: size }} aria-label={MARCA.nome}>
      <svg viewBox="0 0 24 24" width={size * 0.5} height={size * 0.5} aria-hidden="true">
        <path d="M8 5.2v13.6c0 .8.9 1.2 1.5.8l10-6.8a1 1 0 0 0 0-1.6l-10-6.8C8.9 4 8 4.4 8 5.2z" fill="currentColor" />
      </svg>
    </span>
  );
}
