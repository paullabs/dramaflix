import { getDrama } from "@/data/catalogo";
import { PosterCard } from "./PosterCard";
import styles from "./PosterGrid.module.css";

/** Grade responsiva de capas (categorias, Minha lista, busca). */
export function PosterGrid({ ids }: { ids: string[] }) {
  return (
    <div className={styles.envoltorio}>
      <ul className={styles.grade}>
        {ids.map((id, i) => (
          <li key={id} style={{ "--i": i } as React.CSSProperties}>
            <PosterCard drama={getDrama(id)} layout="grade" mostrarTop={getDrama(id).emAlta <= 3} />
          </li>
        ))}
      </ul>
    </div>
  );
}
