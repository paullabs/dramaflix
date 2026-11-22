import { Ambiente } from "@/components/Ambiente";
import { BottomTabs } from "@/components/BottomTabs";
import { SideNav } from "@/components/SideNav";
import { TopBar } from "@/components/TopBar";
import styles from "./shell.module.css";

// Estrutura das páginas com navegação: barra lateral (≥960) ou barras do app (<960).
// O conteúdo começa depois da barra lateral; nada fica por baixo dela.
export default function AppLayout({ children }: { children: React.ReactNode }) {
  return (
    <>
      <Ambiente />
      <SideNav />
      <TopBar />
      <div className={styles.shell}>{children}</div>
      <BottomTabs />
    </>
  );
}
