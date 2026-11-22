import { Botao } from "@/components/Botao";
import { IconGhost, IconHome } from "@/components/icons";
import vazio from "@/components/Vazio.module.css";

export default function NaoEncontrado() {
  return (
    <div className="page">
      <div className={vazio.vazio}>
        <span className={vazio.icone} aria-hidden="true">
          <IconGhost size={34} />
        </span>
        <h1 className={vazio.titulo}>Não encontrado</h1>
        <div className={vazio.botoes}>
          <Botao href="/" variante="claro" icone={<IconHome size={20} />}>
            Início
          </Botao>
        </div>
      </div>
    </div>
  );
}
