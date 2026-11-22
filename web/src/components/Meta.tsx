import type { Classificacao, Drama } from "@/data/catalogo";
import { cx } from "@/lib/marca";
import { IconClock, IconEpisodios, IconMic } from "./icons";
import styles from "./Meta.module.css";

/** Quadrado da classificação indicativa no padrão brasileiro (cor + idade), que todo mundo reconhece. */
export function Classificacao({ valor, className }: { valor: Classificacao; className?: string }) {
  const idade = valor === "L" ? "L" : valor.slice(1);
  return (
    <span className={cx(styles.classe, styles[`c${idade}`], className)} title={valor === "L" ? "Livre" : `Não recomendado para menores de ${idade} anos`}>
      {idade}
    </span>
  );
}

/**
 * Linha curta de informações, igual em todo o site: classificação · episódios (· duração · dublado · gênero).
 * Ícone + número no lugar de frases.
 */
export function Meta({
  drama: d,
  duracao,
  genero,
  tamanho = "m",
  className,
}: {
  drama: Drama;
  duracao?: boolean;
  genero?: boolean;
  tamanho?: "p" | "m";
  className?: string;
}) {
  const icone = tamanho === "p" ? 15 : 18;
  return (
    <ul className={cx(styles.meta, tamanho === "p" && styles.pequena, className)}>
      <li>
        <Classificacao valor={d.classificacao} />
      </li>
      <li aria-label={`${d.episodios} episódios`}>
        <IconEpisodios size={icone} className={styles.icone} />
        {d.episodios} ep.
      </li>
      {duracao && (
        <li aria-label="1 a 2 minutos por episódio">
          <IconClock size={icone} className={styles.icone} />
          1–2 min
        </li>
      )}
      {d.dublado && (
        <li>
          <IconMic size={icone} className={styles.icone} />
          Dublado
        </li>
      )}
      {genero && <li className={styles.genero}>{d.genero}</li>}
    </ul>
  );
}
