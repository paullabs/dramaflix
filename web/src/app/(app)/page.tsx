import { Billboard } from "@/components/Billboard";
import { Row } from "@/components/Row";
import { fileiras } from "@/data/catalogo";
import styles from "./page.module.css";

// Home: destaque (billboard) + fileiras de capas 3:4.
export default function Home() {
  return (
    <>
      <Billboard />
      <div className={styles.fileiras}>
        {fileiras.map((f) => (
          <Row key={f.id} fileira={f} />
        ))}
      </div>
    </>
  );
}
